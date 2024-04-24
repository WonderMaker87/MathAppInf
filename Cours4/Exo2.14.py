from PIL import Image
import numpy as np
from scipy.ndimage import convolve

def enhance_edges(image):
    # Convert the image to a numpy array
    pixel_array = np.array(image)

    # Image dimensions
    height, width = pixel_array.shape[:2]

    # Edge enhancement kernel
    kernel = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

    # Apply the edge enhancement kernel to the image
    edges_array = np.zeros_like(pixel_array, dtype=np.float32)
    for c in range(3):
        edges_array[:,:,c] = np.abs(convolve(pixel_array[:,:,c], kernel, mode='reflect'))

    # Convert values to integers between 0 and 255
    edges_array = (edges_array - np.min(edges_array)) / (np.max(edges_array) - np.min(edges_array)) * 255
    edges_array = edges_array.astype(np.uint8)

    # Create an image from the edge values array
    edges_image = Image.fromarray(edges_array)

    return edges_image

def main():
    # Load the original image
    original_image = Image.open("images\\Lenna512.png")

    # Enhance the edges of the image
    edges_image = enhance_edges(original_image)

    # Display the enhanced edges image
    edges_image.show()

if __name__ == "__main__":
    main()
