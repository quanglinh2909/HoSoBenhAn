import math

from ultralytics import YOLO
import cv2
import numpy as np


def draw_quadrilateral(image, points):
    # Chuyển đổi danh sách 4 điểm thành mảng NumPy
    points = np.array(points, np.int32)
    points = points.reshape((-1, 1, 2))

    # Vẽ đoạn thẳng nối các điểm
    cv2.polylines(image, [points], isClosed=True,
                  color=(0, 255, 0), thickness=2)




def draw_quadrilateral(image, points):
    points = np.array(points, np.int32)
    points = points.reshape((-1, 1, 2))

    # Vẽ đoạn thẳng nối các điểm
    cv2.polylines(image, [points], isClosed=True,
                  color=(0, 255, 0), thickness=2)


def find_square_vertices(points):
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    return (min_x, min_y), (max_x, max_y)


def getPoiter(array, top_left):
    l = [0, 0]
    count = 0
    for i in array:
        if count == 0:
            l = i
        else:
            if abs(i[0] - top_left[0]) < abs(l[0] - top_left[0]):
                l = i
        count += 1
    return l


def getPoiter2(array, top_right):
    r = [0, 0]
    count = 0
    for i in array:
        if count == 0:
            r = i
        else:
            if abs(i[1] - top_right[1]) <= abs(r[1] - top_right[1]):
                r = i
        count += 1
    return r



def formatImage(image, label=None):
    import cv2
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QImage, QPixmap
    rgbImage = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, ch = rgbImage.shape
    bytesPerLine = ch * w
    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
    if label is None:
        pixmap = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(pixmap)
    else:
        # pixmap = convertToQtFormat.scaled(label.width(), label.height(), Qt.KeepAspectRatio)
        pixmap = QPixmap.fromImage(convertToQtFormat)
        label.setAlignment(Qt.AlignCenter)  # Canh giữa hình ảnh trong QLabel

        pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap


def detectPlate(model, image):
    results = model(task='segment', mode='predict',
                    source=image)
    crop_img = None
    for result in results:
        image = result.orig_img

        h = image.shape[0]
        w = image.shape[1]
        for mask in result.masks:
            pointsx = []
            for array in mask.xy:
                for point in array:
                    x = int(point[0])
                    y = int(point[1])
                    pointsx.append((x, y))
                # draw_quadrilateral(image, pointsx)

                top_left, bottom_right = find_square_vertices(array)

                # Convert points to integers
                top_left = (int(top_left[0]), int(top_left[1]))
                bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
                top_right = (bottom_right[0], top_left[1])
                bottom_left = (top_left[0], bottom_right[1])

                #crop image
                crop_img = image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                # cv2.imshow("cropped", crop_img)
                # cv2.waitKey(0)
                # cv2.circle(image, top_right, 3, (0, 0, 255), -1)
                # cv2.circle(image, top_left, 3, (0, 0, 255), -1)
                # cv2.circle(image, bottom_right, 3, (0, 0, 255), -1)
                # cv2.circle(image, bottom_left, 3, (0, 0, 255), -1)

                l1 = getPoiter2(array, top_left)
                r1 = getPoiter(array, top_right)

                l2 = getPoiter(array, top_left)
                r2 = getPoiter2(array, top_right)
                if (abs(l1[1] - r1[1])) > (abs(l2[1] - r2[1])):
                    l = l2
                    r = r2
                    a = int(r[1]) - int(l[1])
                    b = int(l[0]) - int(r[0])
                    angle_C_rad = math.atan(a / b)
                    angle_C_deg = math.degrees(angle_C_rad)
                    angle = angle_C_deg
                else:
                    l = l1
                    r = r1
                    a = int(r[0]) - int(l[0])
                    b = int(l[1]) - int(r[1])
                    angle_C_rad = math.atan(a / b)
                    angle_C_deg = math.degrees(angle_C_rad)
                    angle = 90 - angle_C_deg

                # if int(angle) != 1:
                #     cv2.circle(image, (int(l[0]), int(l[1])), 3, (0, 255, 255), -1)
                #     cv2.circle(image, (int(r[0]), int(r[1])), 3, (0, 111, 255), -1)
                #
                #     # xoay anh
                #     (h, w) = crop_img.shape[:2]
                #     center = (w / 2, h / 2)
                #     M = cv2.getRotationMatrix2D(center, -angle, 1.0)
                #     crop_img = cv2.warpAffine(crop_img, M, (w, h))

        return crop_img

model_plate_number = YOLO("Plate.pt")  # initialize
image = detectPlate(model_plate_number, "test.jpg")
cv2.imwrite("test3.jpg", image)
cv2.imshow("test", image)
cv2.waitKey(0)
