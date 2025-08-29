from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# Import your functions
from src.remove_bg import remove_background
from src.utils import load_image_from_url

# Config
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

# Request schema
class ImageRequest(BaseModel):
    url: str

@app.post("/remove_bg")
def remove_bg_endpoint(req: ImageRequest):
    try:
        # Load from URL
        img = load_image_from_url(req.url)
        
        # Remove background
        output_img = remove_background(img)

        # Save output
        output_path = os.path.join(OUTPUT_DIR, "bg_removed.png")
        output_img.save(output_path)

        return FileResponse(output_path, media_type="image/png", filename="bg_removed.png")

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

