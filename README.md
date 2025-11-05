# 🩻 Chest X-Ray Report Generator using AI

The **X-Ray Report Generator** is a deep learning prototype that analyzes chest X-rays to detect conditions like **Normal**, **Pneumonia**, or **COVID-19**, and automatically generates a brief **medical-style diagnostic report**.  
It uses **MobileNetV3** for image classification and **Streamlit** for a simple, interactive web interface.

---

## 🚀 Features
- **AI-based X-ray Classification** using MobileNetV3  
- **Automated Medical Report Generation**  
- **Streamlit Web App** for uploading and viewing results  
- **Transfer Learning** for improved accuracy on limited data  
- **Lightweight and Fast**, ideal for real-time predictions  

---

## 🧰 Tech Stack
- **Python 3.10+**
- **PyTorch**
- **TorchVision**
- **Streamlit**
- **scikit-learn**
- **NumPy, Pillow**
- **Transformers**

---

## 🧪 How It Works
1. **Upload a Chest X-ray** using the Streamlit interface.  
2. The image is **preprocessed** (resized, normalized).  
3. The **MobileNetV3 model** analyzes the image and predicts the condition.  
4. A **medical-style report** is automatically generated.  
5. Results are displayed instantly to the user.
