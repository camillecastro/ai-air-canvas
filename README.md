
# 🎨 AI Air Canvas
### Real-Time Hand Gesture Drawing Using Computer Vision

An interactive computer vision application that allows users to draw in the air using hand gestures captured through a webcam.

Built with **Python, OpenCV, and MediaPipe**, this project explores real-time hand tracking, landmark detection, and gesture-based human-computer interaction.

Instead of using a mouse or touchscreen, users can interact with a digital canvas through their hand movements.

---

## ✨ Features

- **Real-Time Hand Tracking:** Detects and tracks hand landmarks using MediaPipe.
- **Gesture-Based Drawing:** Draw on a virtual canvas using hand movements.
- **Multiple Brush Colors:** Switch between five drawing colors.
- **Eraser Mode:** Remove parts of a drawing.
- **Clear Canvas:** Reset the artwork instantly.
- **Background Toggle:** Switch between available display modes.
- **Save Artwork:** Export drawings as PNG images.
- **Live Webcam Integration:** Processes video frames using OpenCV.

---

## 📸 Project Demo

The screenshot below shows the application running with live webcam input and gesture-controlled drawing.

![AI Air Canvas Demo](demo.png)

The project demonstrates real-time video processing, hand landmark detection, and interactive visual feedback.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core application development |
| OpenCV | Webcam capture, image processing, and rendering |
| MediaPipe | Hand landmark detection and tracking |
| NumPy | Numerical operations and image arrays |

---

## 🧠 How It Works

The application follows a computer vision processing pipeline:

**Webcam Input → Frame Processing → Hand Landmark Detection → Gesture Interpretation → Canvas Rendering**

### 1. Video Capture
OpenCV captures frames from the webcam for real-time processing.

### 2. Hand Detection
MediaPipe identifies hand landmarks, including the fingertips and finger joints.

### 3. Gesture Interpretation
The application interprets tracked hand positions to control drawing interactions.

### 4. Canvas Rendering
OpenCV updates the digital canvas based on the detected hand movements.

### 5. Image Export
Users can save their artwork as an image file.

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| 1–5 | Select drawing color |
| E | Toggle eraser |
| C | Clear canvas |
| B | Toggle background |
| S | Save artwork |
| Q | Quit application |

---

## 🚀 Installation and Setup

### Prerequisites

- Python 3.12
- A functioning webcam
- Windows, macOS, or Linux with camera access

### 1. Clone the repository

```bash
git clone https://github.com/camillecastro/ai-air-canvas.git
cd ai-air-canvas
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Allow camera access if prompted.

---

## 📁 Project Structure

```text
ai-air-canvas/
├── app.py
├── requirements.txt
├── README.md
├── demo.png
└── .gitignore
```

---

## 🔬 Engineering Concepts

This project demonstrates practical applications of:

- Computer vision
- Real-time image processing
- Hand landmark tracking
- Human-computer interaction
- Gesture-based interfaces
- Python application development
- Interactive graphical rendering

The application combines computer vision techniques with a responsive user interface to create a hands-free drawing experience.

---

## 🔮 Future Improvements

Potential extensions include:

- Gesture-controlled color selection
- Adjustable brush thickness
- Improved gesture recognition
- Smoother drawing trajectories
- Undo and redo functionality
- Additional drawing tools and shapes
- Improved user interface
- Performance optimization for different webcam resolutions

---

## 👩🏻‍💻 About the Developer

**Camille Castro**

Computer Engineering student at Marian University, with a minor in Mathematics.

Interested in software engineering, artificial intelligence, machine learning, and computer vision.

This project was developed as part of an independent technical portfolio focused on practical, interactive applications of computer engineering concepts.

**GitHub:** [camillecastro](https://github.com/camillecastro)
