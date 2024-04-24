import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, convolve

def apply_laplacian_filter(image, pre_blur=False):
    """Applies a Laplacian filter to detect edges in an image, with optional Gaussian pre-blurring."""
    # Convert the image to a numpy array if not already
    image_array = np.array(image)

    # Optional Gaussian blur to reduce noise
    if pre_blur:
        image_array = gaussian_filter(image_array, sigma=1)  # sigma controls the degree of blurring

    # Laplacian kernel
    laplacian_kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    # Apply the Laplacian kernel
    result = convolve(image_array, laplacian_kernel, mode='reflect')

    # Enhance the output by scaling (simple contrast enhancement)
    result = np.clip(result, 0, 255)

    # Convert to uint8
    result = result.astype(np.uint8)

    return Image.fromarray(result)

# Load an image
image_path = "images/Lenna512.jpg"  # Adjust the path to your image
image = Image.open(image_path).convert("L")  # Convert to grayscale for edge detection

# Apply the Laplacian filter with pre-blurring
laplacian_image = apply_laplacian_filter(image, pre_blur=True)

# Display or save the resulting image
laplacian_image.show()
# Optionally save to a file
# laplacian_image.save("laplacian_output.jpg")
