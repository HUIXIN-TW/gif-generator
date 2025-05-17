from PIL import Image
import datetime
import os
import re

def create_gif_from_folder(folder_path, duration=1500):
    # Regex to match files like "1.png", "2.png", etc.
    number_png_pattern = re.compile(r'^(\d+)\.png$')

    # List and sort image files by numeric filename
    image_filenames = sorted(
        (f for f in os.listdir(folder_path) if number_png_pattern.match(f)),
        key=lambda x: int(number_png_pattern.match(x).group(1))
    )

    if not image_filenames:
        raise ValueError("No numbered PNG files found in the folder.")

    # Full paths to the images
    image_paths = [os.path.join(folder_path, f) for f in image_filenames]

    # Load and convert images to RGB
    images = [Image.open(p).convert("RGB") for p in image_paths]

    # Use folder name and timestamp for output filename
    folder_name = os.path.basename(os.path.normpath(folder_path))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{folder_name}_demo-{timestamp}.gif"
    gif_path = os.path.join(folder_path, output_filename)

    # Save GIF
    images[0].save(gif_path, save_all=True, append_images=images[1:], duration=duration, loop=0)

    print(f"GIF saved at: {gif_path}")
    return gif_path

# Example usage:
create_gif_from_folder("notionsyncgcal/")
