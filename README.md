# Background Removal API for Product Images

NEW - You can now visit our website to remove backgrounds from your images!  
Visit [AI Artisans Background Remover](https://example.com/images).

---

## Overview

This API enhances e-commerce platforms by automating the process of removing backgrounds from product images. With the ability to specify coordinates for a targeted area, it ensures clean and professional images, improving the visual appeal of product listings.

---

## Features

- **Accepts Public Image URLs**: Input an image from any publicly accessible URL.
- **Custom Cropping**: Specify bounding box coordinates for targeted background removal.
- **Outputs Transparent PNG**: Processed images with transparent backgrounds are saved as PNGs.
- **Public Access**: Returns a publicly accessible URL for the processed image.
- **Simple and Fast**: Lightweight and easy-to-use API for seamless integration.

---

## Project Structure

The repository is organized into the following files:

1. **`__init__.py`**
   - Sets up the Flask application, enabling CORS and initializing routes.

2. **`cloudinary_manager.py`**
   - Manages image uploads to Cloudinary and handles cleanup of old images.

3. **`config.py`**
   - Centralized configuration for Cloudinary credentials and API limits.

4. **`image_processor.py`**
   - Handles image downloading, background removal, and cropping using `rembg` and `Pillow`.

5. **`routes.py`**
   - Defines the API routes, including input validation, image processing, and response handling.

6. **`scheduler.py`**
   - Uses `APScheduler` to periodically remove old images from Cloudinary.

7. **`run.py`**
   - Entry point to start the Flask application.

---

## How to Set Up and Run Locally

### Prerequisites

1. Ensure you have the following installed:
   - Python 3.8 or higher
   - pip (Python package manager)
   - Git
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/background-removal-api.git
   cd background-removal-api
   ```
3. Set up a virtual environment (recommended):
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

### Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up the `.env` file for environment variables:
   - Example `.env` file:
     ```
     CLOUD_NAME=your-cloudinary-cloud-name
     API_KEY=your-cloudinary-api-key
     API_SECRET=your-cloudinary-api-secret
     ```

3. Start the API:
   ```bash
   python run.py
   ```

4. The API will be accessible at `http://localhost:5500`.

---

## API Usage Instructions

### API Endpoints

#### 1. **Process Image**
**Endpoint**:  
`POST /process-image`

**Request Body** (JSON):
```json
{
  "image_url": "https://example.com/sample-image.jpg",
  "bounding_box": {
    "x_min": 50,
    "y_min": 50,
    "x_max": 300,
    "y_max": 300
  }
}
```

**Response** (JSON):
```json
{
  "original_image": "https://example.com/sample-image.jpg",
  "processed_image_url": "https://cloudinary.com/processed-image.png"
}
```

#### 2. **Health Check**
**Endpoint**:  
`GET /health`

**Response**:
```json
{
  "status": "healthy"
}
```

---

## Postman Collection

A Postman collection with example requests and responses is included in the repository under the name `Test objects.postman_collection.json`.  
To use it:
1. Import the collection into Postman.
2. Update the environment variables to match your API’s host (e.g., `http://localhost:5500`) and endpoints.


---

## Deployment

The API is hosted on [Hosting Platform] and accessible via the following live endpoint:  
**[Live API Endpoint](https://your-live-api-endpoint.com)**  

---

## Tools and Frameworks Used

- **Flask**: Lightweight web framework for the API.
- **Cloudinary**: For image storage and management.
- **Pillow (PIL)**: Image processing library for cropping and manipulation.
- **rembg**: Pre-trained background removal model.
- **APScheduler**: Scheduler for periodic tasks like image cleanup.
- **Flask-Limiter**: Enforces rate limits for API endpoints.

---

## Author

Developed by **Harshit Soni**  
[GitHub Profile](https://github.com/programmarly)
