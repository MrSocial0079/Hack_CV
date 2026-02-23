# 👁️ Blink Behaviour Analysis using Computer Vision

This project analyzes how blinking patterns differ when a person is:

📖 Reading a document  
🎬 Watching a video  

Using computer vision, we detect blink events from prerecorded videos and compare behavioral patterns across tasks.

---

## 🧠 Objective

To determine how blink frequency and timing change based on cognitive activity using:

- Facial landmark detection
- Eye Aspect Ratio (EAR)
- Temporal blink logging

---

## 📁 Project Structure

blink_research/
├── videos/
│     ├── reading.MOV
│     ├── movie.MOV
├── logs/
├── eye_utils.py
├── video_blink_logger.py
├── comparison.py
└── README.md

---

## ⚙️ Installation

Install dependencies:

```bash
pip install opencv-python mediapipe numpy pandas matplotlib
```
⸻

🎥 Step 1 — Add Videos

Place your videos inside the videos/ folder:

videos/
 ├── reading.MOV
 ├── movie.MOV

These should be recordings of:
	•	You reading
	•	You watching a video

⸻

🔍 Step 2 — Extract Blink Logs

Run:

python video_blink_logger.py

This will:

✔ Detect blink events
✔ Log them frame-by-frame
✔ Save results to:

logs/reading.csv
logs/movie.csv


⸻

📊 Step 3 — Compare Behaviour

Run:

python comparison.py

This generates:
	•	📈 Line graph → Blink progression over time
	•	📊 Bar graph → Total blink comparison

⸻

📉 Output Interpretation

Metric	Meaning
Blink Progression	Temporal behavior of blinking
Total Blink Count	Overall cognitive effect

Typical observation:
	•	Reading → more frequent blinking
	•	Watching → reduced blinking

⸻

⚠️ Research Note

Under conditions of burning eye sensation, increased blinking frequency may occur as a normal physiological response.

⸻

🧪 Methodology

Blink detection is performed using:

Eye Aspect Ratio (EAR):

EAR = (vertical eye distance) / (horizontal eye distance)

A blink is detected when EAR falls below a threshold for consecutive frames.

⸻

📌 Applications
	•	Cognitive load analysis
	•	Human-computer interaction studies
	•	Eye fatigue monitoring
	•	Behavioral research

⸻

🚀 Future Work
	•	Blink rate per minute analysis
	•	Eye strain detection
	•	Real-time webcam experiments

---

You can paste this directly into GitHub 👍
