import os
import random
from PIL import Image

folder_name = "bears"

file_names = os.listdir(folder_name)

random_file_name = random.choice(file_names)

img_name = folder_name + "/" + random_file_name

img = Image.open(img_name)

img.show()
