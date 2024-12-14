const API_URL = "http://127.0.0.1:5500/process-image";

async function processImage() {
  const imageUrl = document.getElementById("image-url").value;
  const xMin = parseInt(document.getElementById("x-min").value, 10);
  const yMin = parseInt(document.getElementById("y-min").value, 10);
  const xMax = parseInt(document.getElementById("x-max").value, 10);
  const yMax = parseInt(document.getElementById("y-max").value, 10);

  if (!imageUrl || isNaN(xMin) || isNaN(yMin) || isNaN(xMax) || isNaN(yMax)) {
    alert("Please provide a valid image URL and bounding box coordinates.");
    return;
  }

  toggleLoading(true);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        image_url: imageUrl,
        bounding_box: { x_min: xMin, y_min: yMin, x_max: xMax, y_max: yMax },
      }),
    });

    if (response.ok) {
      const data = await response.json();
      displayProcessedImage(data.processed_image_url);
    } else {
      const error = await response.json();
      alert(`Error: ${error.error}`);
    }
  } catch (error) {
    console.error("Error processing image:", error);
    alert("Failed to process the image. Please try again.");
  } finally {
    toggleLoading(false);
  }
}

function displayProcessedImage(imageUrl) {
  const resultContainer = document.getElementById("result-container");
  document.getElementById("processed-image").src = imageUrl;
  document.getElementById("processed-image-link").href = imageUrl;
  resultContainer.style.display = "block";
}

function toggleLoading(isLoading) {
  document.getElementById("loader").style.display = isLoading
    ? "block"
    : "none";
}

/**
 * Downloads the processed image displayed in the result container.
 */
function downloadImage() {
    const processedImage = document.getElementById("processed-image");
    const imageUrl = processedImage.src;
  
    if (!imageUrl) {
      alert("No processed image available to download.");
      return;
    }
  
    // Create a temporary anchor element for downloading
    const anchor = document.createElement("a");
    anchor.href = imageUrl;
    anchor.download = "processed-image.png"; // Default file name
    document.body.appendChild(anchor);
  
    // Trigger the download and clean up
    anchor.click();
    document.body.removeChild(anchor);
  }
  

document
  .getElementById("process-button")
  .addEventListener("click", processImage);
