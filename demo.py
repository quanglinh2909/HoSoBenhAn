from flask import Flask, Blueprint, send_from_directory, request, abort
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

app = Flask(__name__)

# Tạo Blueprint cho thư mục assets
assets_bp = Blueprint('assets', __name__, static_folder='assets', static_url_path='/assets')
# engine = create_engine('sqlite:///{}'.format(PATH_DATABASE))
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# Đường dẫn đến thư mục bạn muốn công khai
public_folder_path = os.path.dirname(__file__)

memberService = MemberService()
userService = UserService()
configService = ConfigService()


# Route để phục vụ các tệp tĩnh từ thư mục assets

@assets_bp.route('/<path:filename>')
def serve_assets(filename):
    # Sử dụng hàm send_from_directory để phục vụ các tệp từ thư mục assets
    return send_from_directory(assets_bp.static_folder, filename)


# get member by id
@app.route('/member/<id>')
def get_member(id):
    member = memberService.getById(id)
    if member:
        member_schema = MemberSchema()
        member_dict = member_schema.dump(member)
        return jsonify(member_dict)
    else:
        return "Member not found", 404


# get getPage member (page, limit, type) param
@app.route('/member/getPage/<page>/<limit>/<type>')
def get_page_member(page, limit, type):
    members = memberService.getPage(page, limit, type)
    if members:
        member_schema = MemberSchema(many=True)
        member_dict = member_schema.dump(members)
        return jsonify(member_dict)
    else:
        return "Member not found", 404


@app.route('/member/getTotal/<type>')
def get_total_member(type):
    total = memberService.getTotal(type)
    if total:
        return jsonify(total)
    else:
        return "Member not found", 404


@app.route('/member/search/<page>/<limit>/<type>/<key>')
def search_member(page, limit, type, key):
    page = int(page)
    limit = int(limit)
    members = memberService.search(key, page, limit, type)
    if members:
        member_schema = MemberSchema(many=True)
        member_dict = member_schema.dump(members)
        return jsonify(member_dict)
    else:
        return "Member not found", 404

@app.route('/member/create', methods=['POST'])
def create_member():
    if not request.json:
        abort(400)
    member = Member()
    member.FullName = request.json['FullName']
    member.Birthday = request.json['Birthday']
    member.CCCD = request.json['CCCD']
    member.Relatives = request.json['Relatives']
    member.InfoRelatives = request.json['InfoRelatives']
    member.DateIn = request.json['DateIn']
    member.Province = request.json['Province']
    member.District = request.json['District']
    member.Ward = request.json['Ward']
    member.Address = request.json['Address']
    member.CDB = request.json['CDB']
    member.Note = request.json['Note']
    member.Avatar = request.json['Avatar']
    member.Type = request.json['Type']
    member.CN = request.json['CN']
    member.DH = request.json['DH']
    member.HA = request.json['HA']
    member.Medicine = request.json['Medicine']
    member.Symptoms = request.json['Symptoms']
    member.OtherMedicalConditions = request.json['OtherMedicalConditions']
    memberService.create(member)
    return jsonify({'status': 'success'})


# Đăng ký Blueprint
app.register_blueprint(assets_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5874)
