import numpy as np
import cv2


def calculate_rotation_angle_from_corners(corners):
    # Tính trung tâm hình học của danh sách điểm
    center_x = sum(x for x, y in corners) / len(corners)
    center_y = sum(y for x, y in corners) / len(corners)

    # Tính góc giữa mỗi góc và trung tâm hình học
    angles = []
    for corner in corners:
        dx = corner[0] - center_x
        dy = corner[1] - center_y
        angle = np.degrees(np.arctan2(dy, dx))
        angles.append(angle)

    # Tính góc trung bình
    average_angle = sum(angles) / len(angles)

    return average_angle


def xoayHinh(image,random_points,type):
    if type == 1:
        angle_to_rotate = calculate_rotation_angle_from_corners(random_points)
    else:
        angle_to_rotate = calculate_rotation_angle_from_lines(image)

    rows, cols = image.shape[:2]
    image_center = (cols // 2, rows // 2)
    M = cv2.getRotationMatrix2D(image_center, -angle_to_rotate, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))

    return rotated_image


def calculate_rotation_angle_from_lines(image):
    edges = cv2.Canny(image, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    # Tính góc giữa mỗi đường thẳng và trục X (góc trục của ảnh)
    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angles.append(angle)

    # Tính góc trung bình
    average_angle = sum(angles) / len(angles)

    return average_angle
