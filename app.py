import streamlit as st 
from classifier import predict_class
from report_generator import generate_report

def main():
    st.set_page_config(page_title="X-Ray Report Generator", layout="centered")
    st.title("Lung X-Ray Report Generator")

    uploaded_file = st.file_uploader("Upload Lung X-ray", type=['jpg', 'png', 'jpeg'])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded X-ray", use_container_width=True)
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("🔍 Analyzing X-ray..."):
            condition = predict_class("temp.jpg")

        st.success("Analysis Complete")
        st.subheader("Predicted Condition:")
        st.write(condition)

        report = generate_report(condition)
        st.subheader("📋 AI-Generated Report:")
        st.write(report)

if __name__ == "__main__":
    main()