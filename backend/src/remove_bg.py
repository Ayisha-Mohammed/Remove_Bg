import os
import torch
from PIL import Image
from src.utils import load_image_from_url, preprocess, apply_mask
from src.u2net import U2NET

# --------- Config ---------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "u2net.pth")
MODEL_PATH = os.path.normpath(MODEL_PATH)

OUTPUT_DIR = os.path.join(BASE_DIR, "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --------- Load Model ---------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = U2NET(3, 1)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# --------- Remove Background Function ---------
def remove_background(img: Image.Image) -> Image.Image:
    input_tensor = preprocess(img).to(device)
    with torch.no_grad():
        d1, *_ = model(input_tensor)
        pred = d1[:, 0, :, :]
        pred = (pred - pred.min()) / (pred.max() - pred.min())
        mask = pred.squeeze().cpu().numpy()
    return apply_mask(img, mask)

# --------- CLI ---------
if __name__ == "__main__":
    image_url = input("Enter image URL: ")
    img = load_image_from_url(image_url)
    output_img = remove_background(img)
    output_path = os.path.join(OUTPUT_DIR, "bg_removed.png")
    output_img.save(output_path)
    print(f"Background removed! Saved at {output_path}")
