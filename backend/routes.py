from flask import jsonify, request,render_template
from backend.image_processor import ImageProcessor
from backend.cloudinary_manager import CloudinaryManager
from backend.scheduler import ImageScheduler
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import send_file
import os


limiter = Limiter(get_remote_address, default_limits=["3 per minute"])

def init_routes(app):
    @app.route('/process-image', methods=['POST'])
    @limiter.limit("3 per minute")
    def process_image():
        data = request.get_json()

        if not data or 'image_url' not in data or 'bounding_box' not in data:
            return jsonify({"error": "Missing 'image_url' or 'bounding_box' in request body"}), 400

        image_url = data['image_url']
        bounding_box = data['bounding_box']

        result = ImageProcessor.remove_background_and_crop(image_url, bounding_box)

        if result.startswith("Failed") or result.startswith("Error"):
            return jsonify({"error": result}), 500

        cloudinary_manager = CloudinaryManager()
        public_url, public_id = cloudinary_manager.upload_image(result)

        return jsonify({"orignal_image":image_url, "processed_image_url": public_url}), 200
