import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = torch.nn.Linear(model.last_channel, 4)
model.load_state_dict(torch.load("covid_classifier.pth", map_location='cpu'))
model.eval()

LABELS = ['COVID-19', 'Normal', 'Viral Pneumonia', 'Lung Opacity']

def predict_class(image_path):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    img = Image.open(image_path).convert('RGB')
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(img)
        pred_class = output.argmax(dim=1).item()

    return LABELS[pred_class]