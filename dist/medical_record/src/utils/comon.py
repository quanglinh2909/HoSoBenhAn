
from PyQt5.QtGui import QPixmap

import os
import requests
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO


def uploadfile(urlFile):
    load_dotenv()

    try:
        address = os.getenv("ADDRESS")
        port = os.getenv("PORT_API")

        # Build the upload URL
        url = f"http://{address}:{port}/upload"

        # Load SVG data
        with open(urlFile, 'rb') as svg_file:
            svg_data = svg_file.read()

        # Convert SVG to PNG and resize
        svg_bytes = BytesIO(svg_data)
        img = Image.open(svg_bytes)
        img = img.resize((200, 200))

        # Convert the resized image to bytes (PNG format)
        png_bytes = BytesIO()
        img.save(png_bytes, format='PNG')

        # Upload the resized image (as bytes) to the server
        files = {'file': png_bytes.getvalue()}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            return response.json()
        else:
            print("Upload file fail")

    except Exception as e:
        print(e)



def readImage(image_url):
    try:
        load_dotenv()
        address = os.getenv("ADDRESS")
        port = os.getenv("PORT_API")
        image_url = f"http://{address}:{port}/getImage?path=" + image_url
        response = requests.get(image_url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            return pixmap
        else:
            return None
    except Exception as e:
        return None
def removeImage(image_url):
    try:
        load_dotenv()
        address = os.getenv("ADDRESS")
        port = os.getenv("PORT_API")
        image_url = f"http://{address}:{port}/delete?path=" + image_url
        response = requests.get(image_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None
