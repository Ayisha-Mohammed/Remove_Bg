from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os, base64, re
from io import BytesIO
from PIL import Image

# Import your functions
from src.remove_bg import remove_background
from src.utils import load_image_from_url

app = FastAPI()
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CORS (for Chrome extension)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["chrome-extension://dnknnafilfolcojcmindcmlbdmmiekga"],  # your extension id
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageRequest(BaseModel):
    url: str   # can be http(s)://... OR data:image/...

def load_image(req_url: str) -> Image.Image:
    """
    Handle both normal URLs and base64 data URLs.
    """
    if req_url.startswith("data:image/"):
        # extract base64 string
        header, encoded = req_url.split(",", 1)
        img_bytes = base64.b64decode(encoded)
        return Image.open(BytesIO(img_bytes)).convert("RGB")
    else:
        return load_image_from_url(req_url)

@app.post("/remove_bg")
def remove_bg_endpoint(req: ImageRequest):
    try:
        # Load image (works with url or base64)
        img = load_image(req.url)

        # Remove background
        output_img = remove_background(img)

        # Save output
        output_path = os.path.join(OUTPUT_DIR, "bg_removed.png")
        output_img.save(output_path)

        return FileResponse(output_path, media_type="image/png", filename="bg_removed.png")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
