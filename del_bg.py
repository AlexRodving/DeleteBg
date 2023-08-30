#pip install Pillow rembg

from rembg import remove
from PIL import Image

input_patch = 'img_input.jpg'
output_patch = 'img_output.png'

open_image = Image.open(input_patch)
output = remove(open_image)

output.save(output_patch)