#!/bin/python3

from PIL import Image
import requests
from io import BytesIO
import sys

if len(sys.argv) < 1:
    url = "https://cataas.com/cat"
else:
    url = ("https://cataas.com/cat/says/" + str(sys.argv[1]))

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()