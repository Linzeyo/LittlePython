from PIL import Image

def create_blank_image(width, height, color):
    image = Image.new("RGBA", (width, height), color)
    return image

def save_image(image, path, format):
    image.save(path, format)