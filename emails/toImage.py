import subprocess
import os
from certificate import certificates

def toImage(name):
    html_content = certificates(name)
    html_file = f"{name}_Certificate.html"
    with open(html_file, 'w') as f:
        f.write(html_content)
    
    # Define the output image file
    output_image = f"{name}_Certificate.png"
    
    # Path to wkhtmltoimage executable
    path_to_wkhtmltoimage = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe"

    # Command to convert HTML to image
    command = [
        path_to_wkhtmltoimage,
        "--enable-local-file-access",
        html_file,
        output_image,
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Image generated: {output_image}")
        return output_image
    except subprocess.CalledProcessError as e:
        print(f"Error generating image: {e}")
        return None
    finally:
        # Clean up HTML file after conversion
        if os.path.exists(html_file):
            os.remove(html_file)
