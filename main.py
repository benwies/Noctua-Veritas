def embed_text_in_existing_image(image_path, text, output_path):
    """Embed plain text at the beginning of an existing image file."""
    # Read the original image data
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Convert the text to bytes and add a delimiter to mark the end of the text
    text_bytes = text.encode('utf-8') + b'\x00'

    # Check the PNG header (first 8 bytes)
    png_signature = b'\x89PNG\r\n\x1a\n'
    if image_data.startswith(png_signature):
        # Find the end of the IHDR chunk (which is the first chunk in a PNG file)
        ihdr_end = image_data.find(b'\x00\x00\x00\x00IEND') + 12  # Adding 12 to include the length of the IEND chunk header

        # Insert text bytes right after the IHDR chunk
        combined_data = image_data[:ihdr_end] + text_bytes + image_data[ihdr_end:]
    else:
        # If not a PNG, prepend the text
        combined_data = text_bytes + image_data

    # Save the new image file with the embedded text
    with open(output_path, 'wb') as f:
        f.write(combined_data)

    print(f"Text embedded in {output_path}")

# Example usage
image_path = '1dapetoN.jpg'  # Replace with the path to your uploaded image
text = 'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vN2lWNmY5VGc='  # Your text message
output_path = 'dapetoN.jpg'  # Output file path

embed_text_in_existing_image(image_path, text, output_path)
