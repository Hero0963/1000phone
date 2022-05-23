# ref=https://www.geeksforgeeks.org/how-to-open-an-image-from-the-url-in-pil/

# importing modules
import urllib.request
from PIL import Image

urllib.request.urlretrieve(
    'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
    "gfg001.png")

# img = Image.open("gfg.png")
# img.show()
