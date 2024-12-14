import cloudinary
import cloudinary.uploader
from datetime import datetime, timedelta

class CloudinaryManager:
    def __init__(self):
        cloudinary.config(
            cloud_name="dx3auvjg9",
            api_key="885384425839441",
            api_secret="xVPaiolYyYH-Ok7oysMO3KmLoTM",
            secure=True
        )
        self.uploaded_images = {}

    def upload_image(self, image_path: str) -> str:
        """Upload the processed image to Cloudinary and return its URL and public ID."""
        upload_result = cloudinary.uploader.upload(image_path, format="png")
        public_url = upload_result.get('url')
        public_id = upload_result.get('public_id')

        # Save image public ID and upload timestamp
        self.uploaded_images[public_id] = datetime.utcnow()

        return public_url, public_id

    def remove_old_images(self):
        """Deletes images from Cloudinary that are older than 2 minutes."""
        current_time = datetime.now()
        for public_id, timestamp in list(self.uploaded_images.items()):
            if current_time - timestamp > timedelta(minutes=2):
                try:
                    cloudinary.uploader.destroy(public_id)
                    print(f"Deleted image: {public_id}")
                    del self.uploaded_images[public_id]
                except Exception as e:
                    print(f"Error deleting image {public_id}: {str(e)}")
