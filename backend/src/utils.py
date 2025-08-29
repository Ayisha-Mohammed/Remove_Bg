import requests
from io import BytesIO
from PIL import Image
import torch
import torchvision.transforms as transforms
import numpy as np
import cv2

# --------- Image Loading ---------
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
    return img

# --------- Preprocessing ---------
def preprocess(img):
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
    ])
    return transform(img).unsqueeze(0)

# --------- Postprocessing ---------
# def apply_mask(img, mask):
#     mask = cv2.resize(mask, (img.width, img.height))
#     mask = (mask * 255).astype(np.uint8)
#     # img_np = np.array(img)
#     # result = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGRA)
#     # result[:,:,3] = mask
#     # return Image.fromarray(result)

#     img_np = np.array(img)
#     h, w = img_np.shape[:2]

#     # Create BGRA image manually
#     bgra = np.zeros((h, w, 4), dtype=np.uint8)
#     bgra[:, :, :3] = img_np  # keep original RGB
#     bgra[:, :, 3] = mask     # alpha channel

#     # Convert back to PIL Image
#     result = Image.fromarray(bgra)

def apply_mask(img, mask):
    mask = cv2.resize(mask, (img.width, img.height))
    mask = (mask * 255).astype(np.uint8)

    img_np = np.array(img)
    h, w = img_np.shape[:2]

    # Create BGRA image manually
    bgra = np.zeros((h, w, 4), dtype=np.uint8)
    bgra[:, :, :3] = img_np  # keep original RGB
    bgra[:, :, 3] = mask     # alpha channel

    # Convert back to PIL Image
    result = Image.fromarray(bgra)
    return result   


# http://127.0.0.1:8000/remove_bg?image_url=YOUR_IMAGE_URL
