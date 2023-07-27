import sys
import os
import time
from builtins import str

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMainWindow

from d import detectPlate, formatImage


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.image_dir = None
        self.image_paths = []
        self.current_index = 0
        # set size of window
        self.resize(800, 600)

        # self.model_plate_number = YOLO("model/lb_288_n.onnx")  # initialize
        # self.model_2 = YOLO("model/ORC_480_n.onnx")  # initialize

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.change_button = QPushButton("next Image")
        self.change_button.clicked.connect( self.change_image)
        self.layout.addWidget(self.change_button)

        self.check_button = QPushButton("previous Image")
        self.check_button.clicked.connect( self.change_image_2)
        self.layout.addWidget(self.check_button)

        # self.load_model_button = QPushButton("Load Model")
        # self.load_model_button.clicked.connect(self.load_model)
        # self.layout.addWidget(self.load_model_button)
        self.model_plate_number = None
        self.model_2 = None

        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        self.timeLabel = QLabel()
        self.timeLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.timeLabel)

        self.setLayout(self.layout)

    def load_model(self):
        from ultralytics import YOLO

        self.model_plate_number = YOLO("Plate.pt")  # initialize


    def change_image(self):
        if self.image_dir is None:
            return
        if self.current_index >= len(self.image_paths):
            return
        image_path = self.image_paths[self.current_index]
        import cv2
        if self.model_plate_number is None or self.model_2 is None:
            self.load_model()

        if self.image_dir is None:
            return

        current_image_path = self.image_paths[self.current_index]
        image = detectPlate(self.model_plate_number, current_image_path)
        #convert image to pixmap and set it to the label
        self.image_label.setPixmap(formatImage(image, self.image_label))
        self.current_index += 1


    def change_image_2(self):
            from src.utils.FormatImage import formatImage
            if self.image_dir is None:
                return
            image_path = self.image_paths[self.current_index]
            import cv2
            if self.model_plate_number is None or self.model_2 is None:
                self.load_model()

            if self.image_dir is None:
                return

            current_image_path = self.image_paths[self.current_index]

            # Thực hiện kiểm tra kết quả dựa trên current_image_path
            # result = f"Result for {os.path.basename(current_image_path)}"
            # self.result_label.setText(result)
            imageDetectPlateNumber = cv2.imread(current_image_path)
            startTime = time.time()
            results2 = self.model_plate_number.predict(source=imageDetectPlateNumber, imgsz=288,
                                                       agnostic_nms=True, conf=0.4)
            box_plate_number = None
            for result in results2:
                boxes = result.boxes.numpy()
                names = result.names
                for box in boxes:
                    xyxy = box.xyxy
                    box_plate_number = box

            if box_plate_number is not None:
                # save image
                # ve khung
                cv2.rectangle(imageDetectPlateNumber,
                              (int(box_plate_number.xyxy[0][0]), int(box_plate_number.xyxy[0][1])),
                              (int(box_plate_number.xyxy[0][2]), int(box_plate_number.xyxy[0][3])), (0, 255, 0), 2)

                # cv2.imwrite("image.jpg", image)
                # cv2.imwrite("imageDetect.jpg", imageDetect)
                # cv2.imwrite("imageDetectPlateNumber.jpg", imageDetectPlateNumber)
                boxImage = imageDetectPlateNumber[int(box_plate_number.xyxy[0][1]):int(box_plate_number.xyxy[0][3]),
                           int(box_plate_number.xyxy[0][0]):int(box_plate_number.xyxy[0][2])]
                # cv2.imwrite("boxImage"+str(self.current_index)+".jpg", boxImage)

                results3 = self.model_2.predict(source=boxImage, conf=0.4, imgsz=288, agnostic_nms=True)
                endTime = time.time()

                t = detect_plate(results3)
                self.result_label.setText("ket qua: " + t)
                self.timeLabel.setText("Thoi gian xu ly: " + str(endTime - startTime))


            self.current_index -= 1
            if self.current_index < 0:
                self.current_index = len(self.image_paths) - 1
            self.image_label.setPixmap(formatImage(imageDetectPlateNumber, self.image_label))

    def open_image_directory(self):

        directory = r"C:\Users\Admin\Downloads\data\HoSoBenhAn\data2"
        self.image_dir = ""
        self.image_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)
                            if filename.endswith(('.jpg', '.jpeg', '.png'))]
        self.current_index = 0

        if self.image_paths:
            image_path = self.image_paths[self.current_index]
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap.scaledToWidth(self.image_label.width()))
            self.result_label.clear()
        else:
            self.image_label.clear()
            self.result_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    window.open_image_directory()
    sys.exit(app.exec_())