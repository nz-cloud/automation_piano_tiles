from PIL import Image, ImageDraw, ImageFont
import matplotlib.font_manager as fm

# Defining the image size and colors
image_size = (1080, 1080)
background_color = (240, 248, 255)  # Light blue
text_color = (25, 25, 112)  # Midnight blue
icon_color = (30, 144, 255)  # Dodger blue

# Create a new image with the background color
image = Image.new('RGB', image_size, background_color)
draw = ImageDraw.Draw(image)

# Define paths to the fonts
font_path = fm.findfont(fm.FontProperties(family='DejaVu Sans'))
font_large = ImageFont.truetype(font_path, 60)
font_medium = ImageFont.truetype(font_path, 40)
font_small = ImageFont.truetype(font_path, 30)

# Add the text to the image
draw.text((90, 150), "💡 Dica do Dia: Como Precificar Seus Serviços 💡", fill=text_color, font=font_large)
draw.text((90, 300), "Defina seu preço com base no valor que você oferece,", fill=text_color, font=font_medium)
draw.text((90, 360), "não apenas nas horas trabalhadas.", fill=text_color, font=font_medium)
draw.text((90, 450), "Considere seu tempo, habilidades e a qualidade que você entrega!", fill=text_color, font=font_medium)

# Save the image to a file
image_path = "cd:/codes"
image.save(image_path)

image.show()  # Display the image

image_path
