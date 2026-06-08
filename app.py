"""
Streamlit UI for the DCS F-16C RAG assistant.
Run:  streamlit run app.py
(First build the index once:  python dcs_rag.py build)
"""

import streamlit as st
import dcs_rag

st.set_page_config(page_title="DCS F-16 Assistant", page_icon="✈️", layout="centered")

st.title("✈️ DCS F-16C Viper — RAG Assistant")
st.caption("Ask anything from Chuck's Guide. Answers are grounded in the guide with page citations.")

with st.sidebar:
    st.header("Settings")
    k = st.slider("Number of excerpts (top-k)", 1, 8, dcs_rag.TOP_K)
    compare = st.toggle("Also show plain LLM (no guide)", value=False)
    st.markdown("---")
    st.markdown(
        "**Example questions:**\n"
        "- How do I start the engine?\n"
        "- How do I align the INS?\n"
        "- How do I employ a JDAM?\n"
        "- How do I lock a target on radar?"
    )

question = st.chat_input("Type your question…")

if question:
    st.chat_message("user").write(question)
    with st.chat_message("assistant"):
        with st.spinner("Searching the guide…"):
            rag, sources, hits = dcs_rag.answer(question, k=k)
        st.write(rag)
        st.caption(f"📄 Sources: {sources}")
        with st.expander("Show retrieved excerpts"):
            for h in hits:
                st.markdown(
                    f"**Page {h['meta']['page']} — {h['meta']['section']}** "
                    f"_(distance {h['distance']:.3f})_"
                )
                st.text(h["text"][:500] + ("…" if len(h["text"]) > 500 else ""))
                st.markdown("---")
        if compare:
            st.markdown("#### 🆚 Plain LLM (no retrieval)")
            with st.spinner("Generating answer without the guide…"):
                st.write(dcs_rag.answer_plain_llm(question))
