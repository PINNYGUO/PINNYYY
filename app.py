"""APP：RoleTable：AI深度模拟你指定的角色
邀请你想要的任何人（AI深度模拟，角色任你定义），打造专属讨论组：用AI深度扮演你心中所想，AI精准模拟，让理想角色加入群聊。
突破想象限制：不再是单纯和AI互动，而是创建包含特定对象的“私人群聊”，满足深度交流和多元视角需求。
深度角色模拟：基于强大的AI技术，精准呈现设定角色的语言风格和思维模式，带来更真实的对话体验。
思维碰撞工坊：汇聚不同角色（现实中的、历史中的、虚拟的）在同一空间碰撞思想，激发灵感，辅助决策。
运行：`streamlit run app.py`
"""
from __future__ import annotations
import os, re, requests, streamlit as st
from typing import List, Dict

# ========= 页面 & 样式 =========
st.set_page_config(page_title="RoleTable：AI深度模拟，开启专属群聊！", page_icon="💬", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>
small{font-size:1.1rem}
section[data-testid="stSidebar"] div[class^="block-container"]{padding-top:1rem}
.streamlit-expanderHeader{font-weight:600}
.streamlit-expanderContent{border-left:3px solid #e2e8f0;padding-left:0.6rem}
</style>
""", unsafe_allow_html=True)

st.title("RoleTable：AI深度模拟，开启专属群聊！")
st.markdown("<small>突破时空界限，创建专属讨论组，AI精准扮演角色。RoleTable，把你的“理想会话”变成现实！</small>", unsafe_allow_html=True)

# ========= DeepSeek =========
API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "sk-ad5184cc837d4a6c9860bfa46ddd2c68"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
if not API_KEY:
    st.error("⚠️ 缺少 DeepSeek API Key！"); st.stop()

def call_deepseek(msgs: List[Dict]) -> str:
    r = requests.post(API_URL, headers=HEADERS, json={"model": "deepseek-chat", "messages": msgs, "temperature": 0.6}, timeout=60)
    if r.status_code != 200:
        raise RuntimeError(r.text)
    return r.json()["choices"][0]["message"]["content"].strip()

# ========= 正则工具 =========
_pat_paren = re.compile(r"[（(][^）)]*[）)]")          # 括号动作
_pat_seg   = re.compile(r"\[([^\]]+)\](.*?)(?=\[[^\]]+\]|$)", re.S)  # [名字]段落

def build_prefix_pattern(names: List[str]):
    esc = [re.escape(n) for n in names if n]
    return re.compile(rf"^[\s]*(?:{'|'.join(esc)})[：:]\s*", re.IGNORECASE) if esc else None

def strip_noise(text: str, prefix_pat: re.Pattern | None) -> str:
    text = _pat_paren.sub("", text)  # 括号动作
    if prefix_pat:
        text = prefix_pat.sub("", text)
    return text.strip()

# ========= 侧栏 =========
st.sidebar.header("🌟请在此处定义角色——邀请你想要的任何人，介绍得越详细越有助于AI深度模拟。即刻点燃思想的火花，创建专属思想沙龙。编辑完成后实时生效。")
user_alias = st.sidebar.text_input("我在群里叫什么？", value="群主")
st.sidebar.markdown("---")
roles: List[Dict] = []
for i in range(3):
    with st.sidebar.expander(f"参与角色 {i+1}", expanded=(i == 0)):
        name = st.text_input("名称", key=f"name_{i}", placeholder="例如：Prof. Wang")
        prompt = st.text_area("详细介绍一下TA吧？", key=f"prompt_{i}", height=120, placeholder="例如：香港中文大学教授，人很亲和，业务能力天花板！")
        if name and prompt:
            roles.append({"name": name.strip(), "system": prompt.strip()})

if st.sidebar.button("🗑️ 清空对话", type="primary"):
    st.session_state.history = []
    st.experimental_rerun()

# ========= 会话历史 =========
if "history" not in st.session_state:
    st.session_state.history: List[Dict] = []

for h in st.session_state.history:
    role = "assistant" if h["role_api"] == "assistant" else "user"
    st.chat_message(role).markdown(f"**{h['speaker']}：** {h['content']}")

# ========= 处理输入 =========
placeholder = f"以『{user_alias}』身份说点什么……"
user_msg = st.chat_input(placeholder)
if user_msg:
    st.chat_message("user").markdown(f"**{user_alias}：** {user_msg}")
    st.session_state.history.append({"speaker": user_alias, "role_api": "user", "content": user_msg})

    if not roles:
        st.warning("请先在侧边栏添加至少 1 个角色！")
    else:
        names_pool = [user_alias] + [r["name"] for r in roles]
        prefix_pat = build_prefix_pattern(names_pool)

        BASE = (
            "历史消息用 `[名字]内容` 标签指示发言者，你回复时**不要加入任何标签或姓名前缀**，且禁止括号动作；"
            "一次仅回复 1-2 句；保持角色一致；以用户为中心。"
        )
        for r in roles:
            sys_p = BASE + "\n你的角色设定：" + r["system"]
            msgs = [{"role": "system", "content": sys_p}]
            for h in st.session_state.history:
                msgs.append({"role": h["role_api"], "content": f"[{h['speaker']}] {h['content']}"})

            with st.spinner(f"{r['name']} 正在输入…"):
                try:
                    raw = call_deepseek(msgs)
                except Exception as e:
                    raw = f"⚠️ API 调用失败：{e}"

            # ---- 切分多段 ----
            segments = _pat_seg.findall(raw) or [(r["name"], raw)]
            for seg_name, seg_content in segments:
                seg_name = seg_name.strip()
                seg_content = strip_noise(seg_content, prefix_pat)
                # fallback: 若 seg_name 未知，归到当前角色
                speaker = seg_name if seg_name in names_pool else r["name"]
                role_api = "assistant" if speaker != user_alias else "user"
                st.chat_message("assistant").markdown(f"**{speaker}：** {seg_content}")
                st.session_state.history.append({"speaker": speaker, "role_api": role_api, "content": seg_content})