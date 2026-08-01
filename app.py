import streamlit as st

st.set_page_config(
    page_title="BookForge AI",
    page_icon="📚",
    layout="wide"
)

# ------------------------------
# Sidebar
# ------------------------------

with st.sidebar:
    st.title("📚 BookForge AI")
    st.markdown("---")

    st.success("AI Publishing Engine")

    st.write("Version 1.0")

    st.markdown("---")

    st.write("### Export")

    st.button("📄 DOCX")
    st.button("📕 PDF")

    st.markdown("---")

    st.write("Status")

    st.progress(0)

# ------------------------------

st.title("📚 BookForge AI")

st.caption("Transform Raw AI Text into a Beautiful Book")

st.markdown("---")

left,right=st.columns([2,1])

with left:

    book_title=st.text_input(
        "Book Title (Optional)"
    )

    author=st.text_input(
        "Author (Optional)"
    )

    raw_text=st.text_area(
        "Paste Raw AI Text",
        height=400,
        placeholder="Paste your ChatGPT or Gemini generated text here..."
    )

with right:

    cover=st.file_uploader(
        "Upload Cover Image",
        type=["png","jpg","jpeg"]
    )

    language=st.selectbox(
        "Language",
        [
            "English",
            "Hindi",
            "Urdu"
        ]
    )

    theme=st.selectbox(
        "Book Theme",
        [
            "Classic",
            "Modern",
            "Minimal",
            "Novel",
            "Academic"
        ]
    )

    export=st.selectbox(
        "Export Format",
        [
            "DOCX",
            "PDF"
        ]
    )

st.markdown("---")

col1,col2,col3=st.columns(3)

with col1:

    if st.button("🚀 Analyze Book",use_container_width=True):
        st.info("AI analysis will be added in the next step.")

with col2:

    if st.button("📖 Generate Book",use_container_width=True):
        st.info("Book generation will be added in the next step.")

with col3:

    if st.button("📥 Export",use_container_width=True):
        st.info("Export engine coming soon.")

st.markdown("---")

st.subheader("Preview")

st.info(
"""
After clicking **Generate Book**, BookForge AI will automatically:

✅ Detect Book Type

✅ Detect Chapters

✅ Create Table of Contents

✅ Create Headings

✅ Create Subheadings

✅ Format Paragraphs

✅ Insert Cover

✅ Export Professional DOCX/PDF
"""
)
