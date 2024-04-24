import numpy as np
from PIL import Image

def apply_sharpening_filter(image, kernel):
    """Applies a sharpening filter to an image using the specified kernel."""
    # Convert the image to a numpy array
    image_array = np.array(image)

    # Kernel size and image dimensions
    kernel_size = len(kernel)
    height, width = image_array.shape[:2]

    # Calculate margin for the kernel
    margin = kernel_size // 2

    # Initialize the result array
    result = np.zeros_like(image_array)

    # Apply the kernel to each pixel in the image
    for y in range(margin, height - margin):
        for x in range(margin, width - margin):
            sum = 0
            for i in range(kernel_size):
                for j in range(kernel_size):
                    sum += image_array[y + i - margin, x + j - margin] * kernel[i][j]
            result[y, x] = sum

    # Clipping the result to stay within valid color ranges
    result = np.clip(result, 0, 255)

    # Convert to uint8 if necessary
    result = result.astype(np.uint8)

    return Image.fromarray(result)

# Load an image and convert to grayscale
image_path = "images\\Lenna512.jpg"  # Adjust the path to your image
image = Image.open(image_path).convert("L")  # Convert to grayscale

# Define the sharpening kernel
sharpening_kernel = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

# Apply the sharpening filter
sharpened_image = apply_sharpening_filter(image, sharpening_kernel)

# Display or save the resulting image
sharpened_image.show()
# Optionally save to a file
sharpened_image.save("sharpened_output.jpg")
