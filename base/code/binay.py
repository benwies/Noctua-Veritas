def embed_text_in_existing_image(image_path, text, output_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
    

    text_bytes = text.encode('utf-8') + b'\x00'
    

    combined_data = image_data + text_bytes
    

    with open(output_path, 'wb') as f:
        f.write(combined_data)
    
    print(f"Text embedded in {output_path}")


image_path = 'input_image.png'  
text = 'Q2FscHVybmlhIG9uZSBzYWlkIGt3d3N2Oi8vc2R2d2hlbHEuZnJwL01KcXM4VGt3=='  
output_path = 'output_image.png'  

embed_text_in_existing_image(image_path, text, output_path)
