import uuid
from datetime import datetime
from io import BytesIO

from flask import Flask, Blueprint, send_from_directory, request, abort, send_file
import os
from flask import jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.constants.Global import PATH_DATABASE
from src.model.Base import Base
from src.model.Member import MemberSchema, Member
from src.service.ConfigService import ConfigService
from src.service.MemberService import MemberService
from src.service.UserService import UserService
from marshmallow import Schema, fields
from PIL import Image

app = Flask(__name__)

# Tạo Blueprint cho thư mục assets
assets_bp = Blueprint('assets', __name__, static_folder='assets', static_url_path='/assets')
# engine = create_engine('sqlite:///{}'.format(PATH_DATABASE))
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# Đường dẫn đến thư mục bạn muốn công khai
public_folder_path = os.path.dirname(__file__)


# Route để phục vụ các tệp tĩnh từ thư mục assets

@assets_bp.route('/<path:filename>')
def serve_assets(filename):
    # Sử dụng hàm send_from_directory để phục vụ các tệp từ thư mục assets
    return send_from_directory(assets_bp.static_folder, filename)

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
#delete file
@app.route('/delete', methods=['GET'])
def delete_file():
    print("delete file")
    if request.method == 'GET':
        path = request.args.get('path')
        if os.path.exists(path):
            os.remove(path)
        return jsonify(path)


# Đăng ký Blueprint
app.register_blueprint(assets_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
