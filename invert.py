import sys
from PIL import Image
import PIL.ImageOps    

if __name__=="__main__":
    input_image = sys.argv[1]

    img = Image.open(input_image)
    img = PIL.ImageOps.invert(img)
    img.save('inverted.jpg')