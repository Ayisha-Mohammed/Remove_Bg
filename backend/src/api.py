from fastapi import FastAPI
<<<<<<< HEAD
from fastapi.responses import FileResponse
=======
from fastapi.responses import FileResponse, JSONResponse
>>>>>>> origin/sam-backend
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# Import your functions
from src.remove_bg import remove_background
from src.utils import load_image_from_url

# Config
app = FastAPI()
<<<<<<< HEAD
OUTPUT_DIR = "../output"
=======
OUTPUT_DIR = "output"
>>>>>>> origin/sam-backend
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CORS (for Chrome extension)
app.add_middleware(
    CORSMiddleware,
<<<<<<< HEAD
    allow_origins=["chrome-extension://gfpjinpofbeimpkoflhofafenionhkpj"],  # your extension id
=======
    allow_origins=["chrome-extension://dnknnafilfolcojcmindcmlbdmmiekga"],  # your extension id
>>>>>>> origin/sam-backend
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
<<<<<<< HEAD
        img = load_image_from_url(req.url)
        output_img = remove_background(img)
        output_path = os.path.join(OUTPUT_DIR, "bg_removed.png")
        output_img.save(output_path)
        return FileResponse(output_path, media_type="image/png", filename="bg_removed.png")
    except Exception as e:
        return {"error": str(e)}
=======
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

>>>>>>> origin/sam-backend
