# Real-Time Object Detection using YOLOv8

## 📌 Overview
This project implements a real-time object detection system using **YOLOv8** and **OpenCV**.  
It captures live video from a webcam, detects multiple objects in each frame, and displays bounding boxes with confidence scores in real time.

The project focuses on simplicity, performance, and practical computer vision application using modern deep learning models.


## 🚀 Features
- Real-time webcam-based object detection
- YOLOv8 Nano model for fast inference on laptops
- Detection of 80 COCO object classes (e.g., person, mobile phone, laptop, bottle)
- Automatic bounding box and label rendering
- Confidence score display for detected objects
- Easy to run and extend


## 🧠 Technologies Used
- Python  
- Ultralytics YOLOv8  
- OpenCV  
- NumPy  


## 📂 Project Structure

yolo-v8-realtime-object-detection/
│
├── main.py               # Main application file
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
├── assets/
│   └── demo.png          # Screenshot of live detection
└── .gitignore


## 🖥 Demo

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/37a23c19-f664-4e5e-8f2b-14767a8121e3" />



## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository


https://github.com/Kpellehboy/Real-Time-Object-Detection-using-YOLOv8.git


### 2️⃣ Install Dependencies

pip install -r requirements.txt

> ⚠️ The YOLOv8 model (`yolov8n.pt`) will be automatically downloaded on first run.

## ▶️ How to Run

python main.py


## ⌨ Controls

* Press **`q`** to quit the application

## 📈 Performance Notes

* Uses YOLOv8 Nano for real-time performance on CPU
* Inference speed may vary depending on hardware
* Webcam resolution: `640×480` (default)


## 🔮 Future Improvements

* FPS counter for performance monitoring
* Video file and IP camera support
* Cloud integration (AWS / Azure / GCP)
* Web-based dashboard using Flask or FastAPI
* Docker containerization


## 👤 Author

**Elijah M. Flomo**
Computer Science Student


## 📄 License

This project is open-source and available for educational and portfolio purposes.



