# Machine Learning-Based IDS/IPS System

## Overview

This project is a Machine Learning-Based Intrusion Detection and Prevention System (IDS/IPS) developed using Python and Scikit-learn. The system analyzes network traffic and classifies it as **Normal** or **Anomalous (Attack)**. Based on the prediction, suspicious traffic is automatically blocked and logged.

The project includes a Streamlit dashboard for real-time traffic simulation, attack monitoring, alert generation, and visualization of security events.

---

## Features

* Network Traffic Classification
* Intrusion Detection System (IDS)
* Intrusion Prevention System (IPS)
* Real-Time Traffic Simulation
* Security Alert Generation
* Traffic Statistics Dashboard
* Event Logging
* Interactive Data Visualization
* Machine Learning-Based Attack Detection

---

## Dataset

**Dataset Used:** NSL-KDD

The NSL-KDD dataset is a benchmark dataset widely used for intrusion detection research and machine learning-based cybersecurity applications.

### Classes

* Normal Traffic
* Anomalous Traffic

---

## Machine Learning Model

### Algorithm

Random Forest Classifier

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

### Performance

* Accuracy: ~77%
* Attack Detection Recall: ~97%

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* SciPy
* Pickle

---

## Project Structure

```text
IDS AND IPS SIMULATOR
│
├── app.py
│
├── data
│   ├── idsipsKDDTrain+.arff
│   └── idsipsKDDTest+.arff
│
├── models
│   ├── model.pkl
│   └── encoders.pkl
│
├── logs
│   └── alerts.csv
│
├── src
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── data_loader.py
│   ├── ids_engine.py
│   ├── ips_engine.py
│   ├── logger.py
│   └── traffic_generator.py
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### Navigate To Project Folder

```bash
cd your-repository-name
```

### Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit matplotlib scipy
```

---

## Training The Model

Run:

```bash
python src/train_model.py
```

Output:

```text
Model trained and saved successfully.
```

Saved Files:

```text
models/model.pkl
models/encoders.pkl
```

---

## Evaluating The Model

Run:

```bash
python src/evaluate_model.py
```

Output:

* Accuracy Score
* Classification Report
* Confusion Matrix

---

## Running The Dashboard

Run:

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Dashboard Features

### Traffic Simulation

Generates simulated network traffic including:

* Web Browsing
* FTP Download
* SSH Login
* Port Scan
* DoS Attack
* SQL Injection
* XSS Attack

### Detection & Prevention

Traffic is classified as:

```text
NORMAL  → ALLOWED

ANOMALY → BLOCKED
```

### Visualizations

* Allowed vs Blocked Traffic
* Attack Distribution
* Traffic Statistics
* Security Alerts
* Event Logs

---

## Sample Output

| IP Address   | Traffic Type  | Prediction | Action  |
| ------------ | ------------- | ---------- | ------- |
| 192.168.1.10 | Web Browsing  | NORMAL     | ALLOWED |
| 192.168.1.20 | SQL Injection | ANOMALY    | BLOCKED |
| 192.168.1.35 | Port Scan     | ANOMALY    | BLOCKED |

---

## Future Improvements

* Real Packet Capture using Scapy
* Deep Learning-Based Detection
* Multi-Class Attack Classification
* Real-Time Network Monitoring
* Cloud Deployment
* Advanced Threat Intelligence Integration

---

## Learning Outcomes

This project demonstrates:

* Data Preprocessing
* Feature Encoding
* Machine Learning Model Development
* Model Evaluation
* Cybersecurity Fundamentals
* Dashboard Development
* Data Visualization
* Event Logging and Monitoring

---

## Author

Omkar Shitole

Machine Learning | AI | Python Developer
