from io import BytesIO

from PIL import Image
from PyQt5.QtCore import QThread
from dotenv import load_dotenv
from flask import Flask, Blueprint, send_from_directory, request, send_file
import os
from flask import jsonify

import uuid
from datetime import datetime


class Server(QThread):
    def __init__(self):
        QThread.__init__(self)
        load_dotenv()

    def run(self):

        app = Flask(__name__)

        @app.route('/getImage', methods=['GET'])
        def get_image():
            if request.method == 'GET':
                path = request.args.get('path')
                img = Image.open(path)
                img_io = BytesIO()
                img.save(img_io, 'PNG')
                img_io.seek(0)
                return send_file(img_io, mimetype='image/png')

        def getUrl():
                pathRoot = "assets/images/"
                if not os.path.exists(pathRoot):
                    os.makedirs(pathRoot)
                date = datetime.now()
                path = pathRoot + date.strftime("%Y%m%d")
                if not os.path.exists(path):
                    os.makedirs(path)
                name = uuid.uuid4().hex
                path = path + "/" + name + "_" + date.strftime("%H%M%S") + ".jpg"
                return path

        # upload file
        @app.route('/upload', methods=['POST'])
        def upload_file():
            print("upload file")
            if request.method == 'POST':
                file = request.files['file']
                path = getUrl()
                file.save(path)
                return jsonify(path)

        # delete file
        @app.route('/delete', methods=['GET'])
        def delete_file():
            print("delete file")
            if request.method == 'GET':
                path = request.args.get('path')
                if os.path.exists(path):
                    os.remove(path)
                return jsonify(path)

        # Đăng ký Blueprint
        port = os.getenv("PORT_API")
        app.run(host='0.0.0.0', port=int(port))

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5874)
