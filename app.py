import streamlit as st
import sequence_counter as sc
import ratio_counter as gc
import tempfile
import os

st.set_page_config(
    page_title="Gene Analyser",
    page_icon="🧬",
    layout="wide",
)

st.title("🧬 Gene Analyser")
st.subheader("DNA sequence analysis made simple")
st.caption("Upload a FASTA file to inspect gene lengths, nucleotide distribution, and GC content.")

st.divider()

up_file = st.file_uploader(
    "Upload your FASTA file",
    type=["fasta", "txt"],
    help="Choose a FASTA or TXT file containing gene sequences.",
)

if up_file is not None:
    st.success("File uploaded successfully")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".fasta") as temp_file:
        temp_file.write(up_file.getvalue())
        file_path = temp_file.name

    try:
        st.header("Analysis tools")
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.subheader("📏 Gene length")
                st.caption("Total nucleotides in each gene")
                if st.button("Total count", key="total_count", use_container_width=True):
                    result = sc.counter(file_path)
                    for results in result:
                        st.write(results)

        with col2:
            with st.container(border=True):
                st.subheader("🔬 Base distribution")
                st.caption("Count of A, T, C, and G")
                if st.button("Distribution count", key="distribution_count", use_container_width=True):
                    r = sc.nucleotide_counter(file_path)
                    for result, sequence_count in r.items():
                        result = f"{result} - {sequence_count}"
                        st.write(result)

        with col3:
            with st.container(border=True):
                st.subheader("🧪 GC content")
                st.caption("Guanine-cytosine ratio by gene")
                if st.button("GC count", key="gc_count", use_container_width=True):
                    Gc = gc.GC_count(file_path)
                    for gene, ratio in Gc.items():
                        resultss=f'{gene}-{ratio}%'
                        st.write(resultss)
                        
    except Exception as e:
        st.warning(f"File is not processing: {e}")

    finally:
        os.remove(file_path)

st.divider()
st.caption("1% Biotech • Gene sequence analysis")
with st.expander('About the builder'):
    st.write('High school student' \
    'Coding since 2025' \
    'Curiosity seeker')
st.link_button('To contact,click','https://www.instagram.com/_sidharthh__._/?__pwa=1#')
