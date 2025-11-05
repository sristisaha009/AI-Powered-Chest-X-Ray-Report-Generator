from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
def generate_report(condition):
    reports = {
        "COVID-19": "The X-ray shows ground-glass opacities consistent with COVID-19 infection. Patient monitoring and isolation advised.",
        "Normal": "The lungs appear clear with no signs of abnormal opacities or infections. No immediate concerns.",
        "Viral Pneumonia": "Findings are suggestive of viral pneumonia. Bilateral patchy opacities may be present.",
        "Lung Opacity": "Localized or diffuse lung opacities observed, could be due to infection, fluid, or inflammation. Further evaluation needed."
    }
    return reports.get(condition, "No abnormalities detected.")