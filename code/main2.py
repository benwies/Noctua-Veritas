from PIL import Image
import stepic

def embed_text_in_image(image_path, text, output_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Encode the text into the image
    encoded_img = stepic.encode(img, text.encode('utf-8'))
    
    # Save the new image with the embedded text
    encoded_img.save(output_path, 'PNG')
    
    print(f"Text embedded in {output_path}")

# Example usage
image_path = 'input_image.png'  # Replace with the path to your uploaded image
text = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vN2lWNmY5VGc='  # Your text message
output_path = 'output_image.png'  # Output file path

embed_text_in_image(image_path, text, output_path)
