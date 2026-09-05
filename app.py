import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(page_title="AgriN - AI Agro Intelligence", layout="wide", page_icon="🌱")

# API Configuration
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)

st.title("🌱 AgriN: Regenerative Agro-Intelligence Platform")
st.caption("Empowering Smallholder Farmers with Multimodal AI & Soil Health Analytics")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🍃 Crop Disease Diagnostic", "🌍 Regenerative Soil Advisor", "🌐 BRICS Data Exchange"])

# TAB 1: Multimodal Disease Detection
with tab1:
    st.subheader("Visual Crop Disease Diagnostic")
    lang = st.selectbox("Preferred Advisory Language", ["Tamil", "English", "Hindi", "Telugu"])
    uploaded_file = st.file_uploader("Upload leaf image for inspection", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Crop Leaf", width=300)
        
        if st.button("Analyze Crop Health"):
            with st.spinner("Analyzing leaf with Gemini AI..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    prompt = f"""
                    You are an agricultural expert. Analyze this crop image.
                    Respond in {lang} language:
                    1. Crop Name & Condition (Healthy or Diseased)
                    2. Disease Name & Severity
                    3. Organic / Bio-fertilizer Remedy
                    4. Regenerative farming advice to prevent future recurrence
                    """
                    response = model.generate_content([prompt, image])
                    st.success("Analysis Complete!")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")

# TAB 2: Soil & Crop Recommendation
with tab2:
    st.subheader("Regenerative Crop & Soil Advisor")
    col1, col2, col3 = st.columns(3)
    with col1:
        nitrogen = st.number_input("Nitrogen (N) level", 0, 200, 50)
    with col2:
        phosphorus = st.number_input("Phosphorus (P) level", 0, 200, 50)
    with col3:
        potassium = st.number_input("Potassium (K) level", 0, 200, 50)
        
    soil_type = st.selectbox("Soil Type", ["Alluvial", "Black Soil", "Red Soil", "Clayey", "Sandy Loam"])
    
    if st.button("Generate Crop Recommendation"):
        with st.spinner("Calculating sustainable crop rotation..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                soil_prompt = f"""
                Provide regenerative crop rotation advice for a farmer with:
                - Soil Type: {soil_type}
                - NPK Values: N={nitrogen}, P={phosphorus}, K={potassium}
                Suggest suitable regenerative crops, cover cropping methods, and natural nitrogen-fixing plants.
                """
                res = model.generate_content(soil_prompt)
                st.markdown(res.text)
            except Exception as e:
                st.error(f"Error: {e}")

# TAB 3: BRICS Collaboration Mock Hub
with tab3:
    st.subheader("BRICS Agro-Climatic Intelligence Exchange")
    st.info("Demonstrating cross-border disease surveillance and climate-resilient crop model sharing.")
    st.write("Cross-referencing agro-climatic zones between India (Deccan Plateau) and Brazil (Cerrado biome).")
