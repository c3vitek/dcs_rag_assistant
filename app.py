"""
DCS Flight Reference — Streamlit UI.
Run:  streamlit run app.py
"""

import streamlit as st
import dcs_rag

st.set_page_config(
    page_title="F-16C Flight guide",
    page_icon="◾",
    layout="centered",
)

# ---------- global CSS -------------------------------------------------------
st.markdown("""
<style>
/* hide Streamlit chrome */
footer { visibility: hidden; }
#MainMenu { visibility: hidden; }
[data-testid="stHeader"] { background: transparent; }

/* title rule */
.ref-title {
    font-size: 1.1rem;
    font-weight: 400;
    letter-spacing: .18em;
    text-transform: uppercase;
    border-bottom: 1px solid #c8962e;
    padding-bottom: .6rem;
    margin-bottom: .2rem;
}
.ref-title span {
    color: #c8962e;
    margin-left: 1.2rem;
    font-size: .82rem;
    letter-spacing: .12em;
}

/* chat messages — square, no rounded bubbles */
[data-testid="stChatMessage"] {
    border-radius: 0 !important;
    border-left: 2px solid #2a2d35;
    padding: .8rem 1rem;
    margin-bottom: .4rem;
}
/* user message: amber left rule */
[data-testid="stChatMessage"][data-testid*="user"],
div[class*="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    border-left-color: #c8962e !important;
}

/* input box */
[data-testid="stChatInput"] textarea {
    border-radius: 0 !important;
    border: 1px solid #2a2d35 !important;
    font-family: monospace !important;
}
[data-testid="stChatInput"] textarea:focus {
    border-color: #c8962e !important;
    box-shadow: none !important;
}

/* buttons — squared */
.stButton button {
    border-radius: 0 !important;
    font-family: monospace !important;
    font-size: .8rem;
    letter-spacing: .06em;
    border: 1px solid #2a2d35 !important;
    background: transparent !important;
    text-transform: uppercase;
}
.stButton button:hover {
    border-color: #c8962e !important;
    color: #c8962e !important;
}

/* expander — no rounded corners */
details {
    border-radius: 0 !important;
    border: 1px solid #2a2d35 !important;
}

/* sidebar section headers */
.sidebar-section {
    font-size: .72rem;
    letter-spacing: .16em;
    text-transform: uppercase;
    color: #c8962e;
    border-bottom: 1px solid #2a2d35;
    padding-bottom: .3rem;
    margin: 1rem 0 .6rem 0;
}
</style>
""", unsafe_allow_html=True)

# ---------- examples & session state ----------------------------------------
EXAMPLES = [
    "How do I start the engine?",
    "How do I use an AMRAAM missile?",
    "How do I employ a JDAM?",
]

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- header ----------------------------------------------------------
st.markdown(
    '<p class="ref-title">F-16C VIPER<span>// Flight Reference</span></p>',
    unsafe_allow_html=True,
)
st.caption("Answers drawn from Chuck's Guide — every claim includes a page reference.")

# ---------- sidebar ---------------------------------------------------------
clicked = None
with st.sidebar:
    st.markdown('<p class="sidebar-section">Aircraft</p>', unsafe_allow_html=True)
    guide = st.selectbox(
        "guide",
        list(dcs_rag.GUIDES.keys()),
        label_visibility="collapsed",
    )

    st.markdown('<p class="sidebar-section">Settings</p>', unsafe_allow_html=True)
    k = st.slider("Manual sections per answer", 1, 8, dcs_rag.TOP_K,
                  label_visibility="visible")
    compare = st.toggle("Show baseline comparison", value=False,
                        help="Side-by-side: answer with the manual vs. without.")

    st.markdown('<p class="sidebar-section">Example questions</p>',
                unsafe_allow_html=True)
    for ex in EXAMPLES:
        if st.button(ex, use_container_width=True):
            clicked = ex

    st.markdown('<p class="sidebar-section">Session</p>', unsafe_allow_html=True)
    if st.button("Clear", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ---------- helpers ---------------------------------------------------------
def render_extras(msg):
    if msg.get("low_conf"):
        st.warning("This topic may not be covered in the manual — "
                   "answer is based on general knowledge.")
    if msg.get("sources"):
        st.caption(f"References: {msg['sources']}")
    if msg.get("hits"):
        with st.expander("Source excerpts"):
            for i, h in enumerate(msg["hits"], 1):
                st.markdown(
                    f"**Page {h['meta']['page']} — {h['meta']['section']}**"
                )
                st.text(h["text"][:500] + ("…" if len(h["text"]) > 500 else ""))
                if i < len(msg["hits"]):
                    st.markdown('<hr style="border-color:#2a2d35; margin:.4rem 0">',
                                unsafe_allow_html=True)
    if msg.get("plain"):
        st.markdown("**Baseline — without manual:**")
        st.write(msg["plain"])


# ---------- render history --------------------------------------------------
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])
        if m["role"] == "assistant":
            render_extras(m)

# ---------- input -----------------------------------------------------------
prompt = st.chat_input("Query the F-16C manual…") or clicked

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner(""):
            rag, sources, hits, low = dcs_rag.answer(
                prompt, guide=guide, k=k, fallback=True
            )
        st.write(rag)
        msg = {"role": "assistant", "content": rag,
               "sources": sources, "hits": hits, "low_conf": low}
        if compare:
            with st.spinner(""):
                msg["plain"] = dcs_rag.answer_plain_llm(prompt, guide)
        render_extras(msg)
    st.session_state.messages.append(msg)