from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

from src.constants.Global import NGOAI_TRU, NOI_TRU
from src.model.Member import Member


def getText(text):
    if text == None or text == "":
        return "Chưa có thông tin"
    return text


def write_line(title, content, c, x, x2, y):
    c.setFont("Roboto-Black", 12)
    c.drawString(x, y, title)
    c.setFont("Roboto-Light", 12)
    c.drawString(x2, y, f"{getText(content)}")
    if x != 10:
        y -= 30
    else:
        y -= 20
    if y < 100:
        c.showPage()
        y = 800
    return y


def getType(type):
    if type == NGOAI_TRU:
        return "Ngoại trú"
    return "Nội trú"


def getAddress(member: Member):
    address = ""
    if member.Address != None and member.Address != "":
        address += member.Address
    if member.Ward != None and member.Ward != "":
        address += ", " + member.Ward
    if member.District != None and member.District != "":
        address += ", " + member.District
    if member.Province != None and member.Province != "":
        address += ", " + member.Province
    return address


def write_to_pdf_with_image_and_content(file_name, member: Member, nameManager, nameDoctor):
    font_path1 = r"res/drawable/font/Roboto-Black.ttf"  # Điều chỉnh đường dẫn phù hợp
    font_path2 = r"res/drawable/font/Roboto-Light.ttf"  # Điều chỉnh đường dẫn phù hợp
    # Cài đặt font "Arial Unicode MS"
    pdfmetrics.registerFont(TTFont("Roboto-Black", font_path1))
    pdfmetrics.registerFont(TTFont("Roboto-Light", font_path2))

    # Tạo một file PDF mới
    c = canvas.Canvas(file_name, pagesize=A4)

    # Vẽ hình ảnh bên phải
    c.drawInlineImage(member.Avatar, 10, 670, width=150, height=160)

    y = 820
    x = 200
    x2 = 270
    y = write_line("Họ tên: ", member.FullName, c, x, x2, y)
    y = write_line("Ngày sinh: ", member.Birthday, c, x, x2, y)
    y = write_line("CCCD: ", member.CCCD, c, x, x2, y)
    y = write_line("Ngày vào: ", member.DateIn, c, x, x2, y)
    y = write_line("Loại: ", getType(member.Type), c, x, x2, y)
    y = write_line("Người thân: ", member.Relatives, c, x, x2, y)
    x = 10
    y = write_line("Địa chỉ: ", getAddress(member), c, x, 60, y)

    y = write_line("Thông tin người thân: ", " ", c, x, x2, y)
    lines = getText(member.InfoRelatives).split("\n")
    for line in lines:
        y = write_line(" ", f"{line}", c, x, 10, y)

    y = write_line("Chuẩn đoán bệnh: ", " ", c, x, x2, y)
    lines = getText(member.CDB).split("\n")
    for line in lines:
        y = write_line(" ", f"{line}", c, x, 10, y)

    y = write_line(f"Sức khỏe theo tháng: ", " ", c, x, x, y)

    dataTable = []

    CN = member.CN
    DH = member.DH
    HA = member.HA
    listCN = CN.split('*&**&*')
    listHD = DH.split('*&**&*')
    listHP = HA.split('*&**&*')
    listHP = listHP[:-1]
    listHD = listHD[:-1]
    listCN = listCN[:-1]
    listNames = []
    listNames.append("")
    for i in range(12):
        listNames.append(f"T {i + 1}")
    # add fist
    listHD.insert(0, "Đường huyết")
    listHP.insert(0, "Huyêt áp")
    listCN.insert(0, "Cân nặng")
    dataTable.append(listNames)
    dataTable.append(listCN)
    dataTable.append(listHD)
    dataTable.append(listHP)

    table = Table(dataTable, colWidths=40, rowHeights=30)
    # set width for first column
    table._argW[0] = 80

    style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Đường kẻ chữ đen cho toàn bộ bảng
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Màu nền cho hàng đầu tiên (tiêu đề)
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Màu chữ cho hàng đầu tiên (tiêu đề)
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Canh giữa nội dung trong bảng
        ('FONTNAME', (0, 0), (-1, 0), 'Roboto-Black'),  # Đặt kiểu font cho hàng đầu tiên (tiêu đề)
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Đặt size cho hàng đầu tiên (tiêu đề)
        # font cho cac hang con lai
        ('FONTNAME', (0, 1), (-1, -1), 'Roboto-Light'),  # Đặt kiểu font cho hàng đầu tiên (tiêu đề)
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Đặt khoảng cách dưới cho hàng đầu tiên (tiêu đề)
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Màu nền cho các hàng còn lại
        # set font cot dau tien
        ('FONTNAME', (0, 1), (0, -1), 'Roboto-Black'),  # Đặt kiểu font cho hàng đầu tiên (tiêu đề)
    ])

    y -= 110
    if y < 100:
        c.showPage()
        y = 800

    table.setStyle(style)

    table.wrapOn(c, 10, y)
    table.drawOn(c, 10, y)

    Medicine = getText(member.Medicine)
    Symptoms = getText(member.Symptoms)
    OtherMedicalConditions = getText(member.OtherMedicalConditions)
    listMedicine = Medicine.split('*&**&*')
    listSymptoms = Symptoms.split('*&**&*')
    listOtherMedicalConditions = OtherMedicalConditions.split('*&**&*')

    y = write_line(" ", " ", c, x, x2, y)

    y = write_line("Triệu chứng bệnh: ", " ", c, x, x2, y)
    for item in listSymptoms:
        if item != "":
            y = write_line(f"", f"- {item}", c, x, 10, y)

    y = write_line("Chứng bệnh lý khác kèm theo: ", " ", c, x, x2, y)
    for item in listOtherMedicalConditions:
        if item != "":
            y = write_line(" ", f"- {item}", c, x, 10, y)

    y = write_line("Thuốc điều trị: ", " ", c, x, x2, y)
    for item in listMedicine:
        if item != "":
            y = write_line(" ", f"- {item}", c, x, 10, y)

    y = write_line("Ghi chú: ", " ", c, x, x2, y)
    lines = getText(member.Note).split("\n")
    for line in lines:
        y = write_line(" ", f"{line}", c, x, 10, y)

    y = write_line(" ", " ", c, x, x2, y)

    ycurrent = y
    # chu ky
    y = write_line("BÁC SĨ ĐIỀU TRỊ", " ", c, 50, x2, y)
    y = write_line(" ", "(ký và ghi rõ họ tên)", c, 45, 44, y + 10)
    y = ycurrent
    y = write_line("GIÁM ĐỐC", " ", c, 400, x2, y)
    y = write_line(" ", "(ký và ghi rõ họ tên)", c, 400, 380, y + 10)

    y = write_line(" ", " ", c, x, x2, y)

    write_line(nameDoctor, " ", c, 50, x2, y)
    y = write_line(nameManager, " ", c, 380, x2, y)

    c.save()
