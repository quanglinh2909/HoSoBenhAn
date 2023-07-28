import math

from ultralytics import YOLO
import cv2
import numpy as np

from DetecOrc import detect_plate



def getPoiter(array, top_right):
    r = array[0]
    temp = math.sqrt((r[0] - top_right[0]) ** 2 + (r[1] - top_right[1]) ** 2)
    count = 0
    index = 0
    for i in array:
        kc = math.sqrt((i[0] - top_right[0]) ** 2 + (i[1] - top_right[1]) ** 2)
        if kc < temp:
            temp = kc
            r = i
            index = count
        count += 1

    return r, index


def detectPlate(model, image):
    results = model(task='segment', mode='predict',
                    source=image)
    crop_img = None
    for result in results:
        image = result.orig_img
        boxes = result.boxes.numpy()
        box_plate_number = None
        conf_plate_number = -1
        names = result.names
        for box in boxes:
            conf = box.conf
            if conf > conf_plate_number:
                box_plate_number = box
                conf_plate_number = conf
        if box_plate_number is None:
            return None
        xyxy = box_plate_number.xyxy
        crop_img = image[int(xyxy[0][1]):int(xyxy[0][3]), int(xyxy[0][0]):int(xyxy[0][2])]

        for mask in result.masks:
            pointsx = []
            for array in mask.xy:
                top_left = (int(xyxy[0][0]), int(xyxy[0][1]))
                top_right = (int(xyxy[0][2]), int(xyxy[0][1]))
                l, index = getPoiter(array, top_left)
                r, index2 = getPoiter(array, top_right)
                # cat pointsx thanh 2 phan
                pointsx1 = pointsx[:index2]
                pointsx2 = pointsx[index2:]

                # noi 2 phan lai voi nhau
                pointsx2.extend(pointsx1)
                pointsx = []
                for i in range(len(pointsx2) - 3):
                    check = True
                    for j in range(1, 4):
                        if pointsx2[j + i - 1][1] > pointsx2[j + i][1]:
                            check = False
                            break
                    if check == True:
                        pointsx = pointsx2[i]
                        break
                # if len(pointsx) > 0:
                #     r = pointsx

                a = abs(int(r[0]) - int(l[0]))
                b = abs(int(l[1]) - int(r[1]))
                if b == 0:
                    angle = 0
                else:
                    angle_C_rad = math.atan(a / b)
                    angle_C_deg = math.degrees(angle_C_rad)
                    angle = 90 - angle_C_deg
                (h, w) = crop_img.shape[:2]
                center = (w / 2, h / 2)
                M = cv2.getRotationMatrix2D(center, -angle, 1.0)
                crop_img = cv2.warpAffine(crop_img, M, (w, h))
        return crop_img


model_plate_number = YOLO("Plate.pt")  # initialize
detect_ORC = YOLO("ORC_288_n.onnx")  # initialize
image = detectPlate(model_plate_number, "data/img_0.png")
#show image
cv2.imshow("image", image)
cv2.waitKey(0)
#
# for i in range(0, 12):
#     print("data2/img_" + str(i) + ".png")
#     image, crop_img = detectPlate(model_plate_number, "data2/img_" + str(i) + ".png")
#     # cv2.imwrite("data3/img_" + str(i) + ".png",image)
#     # cv2.imwrite("test3.jpg", crop_img)
#     cv2.imshow("image", image)
#     # # cv2.imshow("crop_img", crop_img)
#     cv2.waitKey(0)
t = ""
for i in range(0, 12):
    image, crop_img = detectPlate(model_plate_number, "data/img_" + str(i) + ".png")

    # cv2.imwrite("test2.jpg", image)
    # cv2.imwrite("test3.jpg", crop_img)

    results3 = detect_ORC.predict(source=crop_img, conf=0.4, imgsz=288, agnostic_nms=True)
    t1 = detect_plate(results3)
    t1 = "ban dau: " + t1
    results3 = detect_ORC.predict(source=image, conf=0.4, imgsz=288, agnostic_nms=True)
    t2 = detect_plate(results3)
    t2 = "sau khi xoay: " + t2
    t += "data/img_" + str(i) + ".png\n" + t1 + "\n" + t2 + "\n"

print(t)
