import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)

def upload_image(file_bytes: bytes, folder: str = "horses") -> dict:
    return cloudinary.uploader.upload(
        file_bytes,
        folder=folder,
        transformation=[
            {"width": 800, "crop": "limit"},
            {"quality": "auto"},
            {"fetch_format": "auto"},
        ],
    )

def delete_image(public_id: str) -> None:
    cloudinary.uploader.destroy(public_id)
