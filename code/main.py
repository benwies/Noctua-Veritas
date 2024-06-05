def embed_text_in_existing_image(image_path, text, output_path):
    """Embed plain text at the end of an existing image file."""
    # Read the original image data
    with open(image_path, 'rb') as f:
        image_data = f.read()
    
    # Convert the text to bytes and add a delimiter to mark the end of the text
    text_bytes = text.encode('utf-8') + b'\x00'
    
    # Append the text bytes to the image data
    combined_data = image_data + text_bytes
    
    # Save the new image file with the embedded text
    with open(output_path, 'wb') as f:
        f.write(combined_data)
    
    print(f"Text embedded in {output_path}")

# Example usage
image_path = 'input_image.png'  # Replace with the path to your uploaded image
text = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vOTNzdFNpUnE='  # Your text message
output_path = 'output_image.png'  # Output file path

embed_text_in_existing_image(image_path, text, output_path)
