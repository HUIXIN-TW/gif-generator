from PIL import Image

# Image filenames in the order to appear in the GIF
image_filenames = [
    "1.png",
    "2.png"
]

# Load images
images = [Image.open(fn).convert("RGB") for fn in image_filenames]

# Create and save GIF
gif_path = "notionsyncgcal_demo.gif"
images[0].save(gif_path, save_all=True, append_images=images[1:], duration=1500, loop=0)

