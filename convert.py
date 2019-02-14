import sys
from PIL import Image

if __name__=="__main__":
    input_image = sys.argv[1]

    img = Image.open(input_image)
    img = img.convert('RGB')
    img.save('converted.jpg')