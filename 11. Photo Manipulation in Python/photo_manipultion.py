from PIL import Image

def apply_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    image.show(title="Original Image")
    grayscale_image.show(title="Grayscale Image")
apply_grayscale(r"C:\"C:\Users\Anusha\Desktop\newimage.png\input.jpg", r"C:\path\to\your\output_grayscale.jpg")
