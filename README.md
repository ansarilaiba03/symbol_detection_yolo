# Symbol Detection with YOLO

An object detection project that trains and runs a YOLO model to detect and classify symbols in images/video.

## 🌟 Features

- **Custom YOLO training** — Jupyter notebooks for training YOLO models on a custom symbol dataset
- **Train/validation split utility** — Script to organize a dataset into train/val sets
- **Live detection** — Real-time symbol detection from a camera or video feed

## 📂 Structure

```
symbol_detection_yolo/
├── code/
│   ├── live_detect.py           # Real-time inference
│   └── train_val_split.py       # Dataset preparation
├── R2_Train_YOLO_Models.ipynb              # Training notebook (with output)
└── R2_Train_YOLO_Models_NO_OUTPUT.ipynb    # Training notebook (clean version)
```

## 🛠️ Tech

- **Language:** Python
- **Model:** YOLO (You Only Look Once) object detection
- **Environment:** Jupyter Notebook for training

## 🚀 Usage

**1. Prepare your dataset:**
```bash
python code/train_val_split.py
```

**2. Train the model:**
Open and run `R2_Train_YOLO_Models.ipynb` in Jupyter/Colab.

**3. Run live detection:**
```bash
python code/live_detect.py
```

## 📌 Notes

Built to explore YOLO-based object detection end-to-end — from dataset preparation through training to real-time inference.
