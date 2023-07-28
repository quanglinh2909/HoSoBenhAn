import cv2
import numpy as np

def align_license_plate(image, mask_points):
    # Tính toán tọa độ trung bình của mask_points để xác định điểm trung tâm của biển số
    center_x = sum(x for x, y in mask_points) / len(mask_points)
    center_y = sum(y for x, y in mask_points) / len(mask_points)

    # Xác định chiều cao và chiều rộng của biển số
    height = max(mask_points, key=lambda x: x[1])[1] - min(mask_points, key=lambda x: x[1])[1]
    width = max(mask_points, key=lambda x: x[0])[0] - min(mask_points, key=lambda x: x[0])[0]

    # Tọa độ của điểm trung tâm mới (vị trí muốn căn chỉnh biển số vào)
    new_center_x = image.shape[1] // 2
    new_center_y = image.shape[0] // 2

    # Tính toán di chuyển cần thiết để đưa biển số về vị trí mới
    dx = new_center_x - center_x
    dy = new_center_y - center_y

    # Tính toán tỷ lệ thay đổi kích thước cần thiết để căn chỉnh biển số vào vị trí và kích thước mong muốn
    scale_x = image.shape[1] / width
    scale_y = image.shape[0] / height

    # Áp dụng biến đổi hình học (di chuyển và thay đổi kích thước)
    M = np.array([[scale_x, 0, dx], [0, scale_y, dy]], dtype=np.float32)
    aligned_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    return aligned_image

# Đọc hình ảnh
image = cv2.imread('data/img_2.png')

# List điểm mask của biển số
mask_points = [(293, 391), (291, 393), (281, 393), (279, 395), (279, 397), (277, 399),
               (277, 485), (279, 487), (336, 487), (338, 485), (344, 485), (346, 483),
               (348, 483), (350, 481), (352, 481), (354, 479), (362, 479), (364, 477),
               (364, 393), (362, 391)]

# Căn chỉnh biển số
aligned_image = align_license_plate(image, mask_points)

# Hiển thị hình ảnh đã căn chỉnh
cv2.imshow('Aligned License Plate', aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
