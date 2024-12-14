from rembg import remove
from PIL import Image
import hashlib
import os

class ImageProcessor:
    @staticmethod
    def generate_random_hash(data: str) -> str:
        """Generate a unique hash based on the input string."""
        return hashlib.sha256(data.encode()).hexdigest()[:20]

    @staticmethod
    def download_public_image(image_url: str, output_dir: str = "./images") -> str:
        """Download the image from a public URL."""
        import requests
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

        try:
            response = requests.get(image_url, stream=True, timeout=10, headers=headers)
            response.raise_for_status()

            file_extension = image_url.split(".")[-1].split("?")[0]
            filename = f"{ImageProcessor.generate_random_hash(image_url)}.{file_extension}"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, filename)

            with open(output_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)

            return output_path
        except requests.exceptions.RequestException as e:
            return f"Failed to download the image: {str(e)}"

    @staticmethod
    def remove_background_and_crop(image_url: str, bounding_box: dict) -> str:
        """Remove background and crop the image."""
        try:
            image_path = ImageProcessor.download_public_image(image_url)
            if "Failed" in image_path:
                return image_path

            crop_coordinates = (
                bounding_box['x_min'], bounding_box['y_min'],
                bounding_box['x_max'], bounding_box['y_max']
            )

            with open(image_path, "rb") as inp_file:
                output_image = remove(inp_file.read())

            temp_output_path = "temp_output_image.png"
            with open(temp_output_path, "wb") as temp_file:
                temp_file.write(output_image)

            with Image.open(temp_output_path) as img:
                cropped_image = img.crop(crop_coordinates)
                cropped_image = cropped_image.convert("RGBA")
                output_path = os.path.join(
                    "processed_images", ImageProcessor.generate_random_hash(image_path) + "_processed.png"
                )
                cropped_image.save(output_path)

            os.remove(temp_output_path)
            return output_path
            
        except Exception as e:
            return f"Error: {e}"
