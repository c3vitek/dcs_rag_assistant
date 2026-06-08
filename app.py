"""
Streamlit UI for the DCS F-16C RAG assistant (polished version).
Run:  streamlit run app.py
(First build the index once:  python dcs_rag.py build)
"""

import streamlit as st
import dcs_rag

st.set_page_config(page_title="DCS F-16 Assistant", page_icon="✈️", layout="centered")

EXAMPLES = [
    "How do I start the engine?",
    "How do I align the INS?",
    "What does TMS forward do?",
    "How do I employ a JDAM?",
]

# --- session state ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- header ----------------------------------------------------------------
st.title("✈️ DCS F-16C Viper — RAG Assistant")
st.caption("Grounded in Chuck's Guide • answers cite the page they come from")

# --- sidebar ---------------------------------------------------------------
clicked = None
with st.sidebar:
    st.subheader("⚙️ Settings")
    k = st.slider("Excerpts retrieved (top-k)", 1, 8, dcs_rag.TOP_K)
    compare = st.toggle("Compare with plain LLM", value=False)
    st.caption(f"Model: `{dcs_rag.LLM_PROVIDER} / {dcs_rag.LLM_MODEL}`")

    st.markdown("---")
    st.subheader("💡 Try one")
    for ex in EXAMPLES:
        if st.button(ex, use_container_width=True):
            clicked = ex

    st.markdown("---")
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- render history --------------------------------------------------------
def render_sources(msg):
    if msg.get("sources"):
        st.caption(f"📄 Sources: {msg['sources']}")
    if msg.get("hits"):
        with st.expander("Show retrieved excerpts"):
            for rank, h in enumerate(msg["hits"], 1):
                st.markdown(
                    f"**Match #{rank} — Page {h['meta']['page']} · {h['meta']['section']}**"
                )
                st.caption(f"distance {h['distance']:.3f} (lower = closer)")
                st.text(h["text"][:500] + ("…" if len(h["text"]) > 500 else ""))
                st.markdown("---")
    if msg.get("plain"):
        st.markdown("**🆚 Plain LLM (no retrieval):**")
        st.write(msg["plain"])

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])
        if m["role"] == "assistant":
            render_sources(m)

# --- input -----------------------------------------------------------------
prompt = st.chat_input("Type your question…") or clicked

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching the guide…"):
            rag, sources, hits = dcs_rag.answer(prompt, k=k)
        st.write(rag)

        msg = {"role": "assistant", "content": rag, "sources": sources, "hits": hits}
        if compare:
            with st.spinner("Generating answer without the guide…"):
                msg["plain"] = dcs_rag.answer_plain_llm(prompt)
        render_sources(msg)

    st.session_state.messages.append(msg)
