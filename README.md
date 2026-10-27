# EXO-gesture-finger

A hand gesture recognition project that summons EXO members using on webcam.

## 📌 About the Project

**EXO Gesture Summoner** is a computer vision project developed as part of my **1W1P (1 Week 1 Project)** journey.

Built with Python, OpenCV, and MediaPipe, this project detects hand gestures through a webcam and displays different EXO members or the group based on the gestures recognized.

Instead of clicking buttons, users can interact with the program using their hands. Each supported gesture triggers a different visual response, turning a simple computer vision experiment into a fun, EXO-themed interactive application.

## 🎯 Project Objectives

- Explore real-time hand gesture recognition using computer vision.
- Learn how to process webcam input with Python.
- Experiment with hand landmark detection using MediaPipe.
- Connect recognized gestures to interactive visual outputs.
- Combine programming practice with my love for EXO.

## ✨ Features

- **Real-Time Hand Tracking** — detects hands through a webcam.
- **Gesture Recognition** — identifies supported hand poses.
- **Member Summoning** — displays a corresponding EXO member based on the detected gesture.
- **Group Summoning** — triggers an EXO group display using a specific two-hand gesture.
- **Interactive Experience** — lets users interact with the program without traditional mouse clicks.

## 🫰 Gesture Guide

| Hand Gesture | Summoned Member(s) |
|---|---|
| 👉🏻 Finger-gun gesture | Suho |
| 👍🏻 Thumbs up | D.O. (Kyungsoo) |
| 👌🏻 OK sign | Kai, Sehun, and Chanyeol (S.K.Y.) |
| ✊🏻 + ✋🏻 Fist and open palm using both hands | EXO OT9 |

*The program's response depends on successfully detecting the supported hand gesture.*

## 🛠️ Tech Stack

- **Python** — main programming language.
- **OpenCV** — webcam input and image processing.
- **MediaPipe** — hand landmark detection and tracking.
- **NumPy** — numerical operations, if used by the implementation.

## ⚙️ How It Works

1. **Webcam Initialization**

   The program accesses the webcam and captures live video frames.

2. **Hand Detection**

   MediaPipe processes the frames to detect hands and identify their landmarks, such as fingertips and finger joints.

3. **Gesture Recognition**

   The program analyzes the detected hand landmarks to determine whether the user's hand matches one of the supported gestures.

4. **Gesture Mapping**

   Each recognized gesture is associated with a specific EXO member or group.

5. **Visual Output**

   The corresponding member image or group visual is displayed when the required gesture is detected.

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer.
- A working webcam.
- Visual Studio Code or another Python-compatible editor.
- Sufficient lighting for reliable hand detection.

### Installation

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd exo-gesture-summoner
   ```

3. Install the required libraries:

   ```bash
   pip install opencv-python mediapipe numpy
   ```

4. Connect your webcam and run the program:

   ```bash
   python main.py
   ```

   Replace `main.py` with the actual entry-point filename if your project uses a different one.

## 🎮 How to Use

1. Start the program and allow access to your webcam if prompted.
2. Position your hand in front of the camera.
3. Make one of the supported gestures.
4. Wait for the program to recognize the gesture.
5. See which EXO member or group appears!

For better detection, keep your hand visible inside the camera frame and avoid poor lighting.

## 📸 Demo

Add screenshots or a demonstration video here to showcase:

- The webcam feed and detected hand landmarks.
- The finger-gun gesture summoning Suho.
- The thumbs-up gesture summoning D.O.
- The OK sign summoning the S.K.Y. trio.
- The two-hand gesture summoning EXO OT9.

## 📚 What I Learned

Through this project, I explored:

- Accessing and processing live webcam video.
- Understanding hand landmarks and gesture recognition.
- Using computer vision libraries in Python.
- Connecting gesture detection to program behavior.
- Building an interactive application around a personal interest.

## ⚠️ Limitations

- Gesture recognition may be affected by lighting, camera quality, and hand positioning.
- Only the gestures implemented in the program can trigger their corresponding outputs.
- Recognition performance depends on the accuracy of hand detection and gesture classification.

## 🔮 Future Improvements

Potential improvements include:

- Adding more recognizable hand gestures.
- Improving gesture classification and recognition stability.
- Adding sound effects when a member is summoned.
- Creating smoother transitions between member displays.
- Expanding the interaction to support more EXO-themed features.


Each project is an opportunity to turn random ideas into little projects while continuously learning and improving my skills. ✨

---

*Made with Python, computer vision, and lots of love for EXO. ♡*
