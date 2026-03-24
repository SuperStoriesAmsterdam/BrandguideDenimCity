import boto3
import os
from pathlib import Path

PROJECT_NAME = os.getenv("PROJECT_NAME")
R2_BUCKET = os.getenv("R2_BUCKET_NAME")

def get_content_type(suffix):
    types = {
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".png": "image/png", ".webp": "image/webp",
        ".gif": "image/gif", ".svg": "image/svg+xml",
    }
    return types.get(suffix.lower(), "application/octet-stream")

def upload_media():
    client = boto3.client(
        "s3",
        endpoint_url=os.getenv("R2_ENDPOINT_URL"),
        aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
        region_name="auto"
    )

    media_dir = Path("Beeld")
    if not media_dir.exists():
        print("Geen Beeld map gevonden.")
        return

    for file in media_dir.rglob("*"):
        if file.is_file() and file.name != ".DS_Store":
            key = f"{PROJECT_NAME}/{file.relative_to(media_dir)}"
            print(f"Uploading {key}...")
            client.upload_file(
                str(file), R2_BUCKET, key,
                ExtraArgs={"ContentType": get_content_type(file.suffix)}
            )
            print(f"✓ https://media.superstories.com/{key}")

if __name__ == "__main__":
    upload_media()
