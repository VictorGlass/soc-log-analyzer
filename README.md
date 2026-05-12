# 🛡️ SOC Log Analyzer (Python)

A Python-based SOC (Security Operations Center) simulation tool designed to analyze authentication logs and detect suspicious activity such as brute force attacks and abnormal login behavior.

This project simulates how SOC analysts and SIEM platforms correlate security events to identify potential threats in a network environment.


🚀 Features
- Detects multiple failed login attempts
- Identifies possible brute force attacks
- Correlates failed and successful login events
- Timestamp-based threat analysis
- Detects suspicious activity within configurable time windows
- Generates SOC-style security reports
- Simulates basic SIEM/SOC detection workflows
- Input validation for more reliable log parsing


## 🧠 What I Learned

Through this project I practiced and improved:

- Log analysis fundamentals
- Event correlation techniques
- Timestamp parsing using Python
- Brute force detection logic
- Basic threat detection workflows
- Python file handling
- Input validation and error handling
- Writing modular and readable Python code
- Git and GitHub workflow for version control


## 📦 Technologies

- Python 3
- File handling
- Dictionaries & Lists
- Datetime Module
- Basic Detection Logic


📂 Project Structure

soc-log-analyzer/
│
├── analyzer.py
├── sample_logs.txt
└── README.md



## ▶️ Usage

1. Clone the repository

````
git clone https://github.com/VictorGlass/soc-log-analyzer.git
````

2. Enter the project directory
````
cd soc-log-analyzer
````

3. Run the analyzer

````
python analyzer.py
````


## 📊 Example Output

====== SOC ANALYSIS REPORT ====== 

[INFO] Failed login from 192.168.1.10 at 2026-05-11 10:01:15 
[INFO] Failed login from 192.168.1.10 at 2026-05-11 10:02:10 
[INFO] Failed login from 192.168.1.10 at 2026-05-11 10:03:02 

[ALERT] Possible brute force attack detected! IP Address: 192.168.1.10 
Failed attempts: 3 
Detection window: 5 minutes 

====== END OF REPORT ======


## 🎯 Purpose

This project was created to simulate how SOC analysts detect threats through log analysis, event correlation, and behavioral pattern recognition.

The goal is to strengthen practical cybersecurity and Blue Team skills through hands-on Python development.


## 🛡️ Disclaimer

This project was developed strictly for educational and learning purposes.

Do not use these techniques against systems or environments without proper authorization.


## 👨‍💻 Author

Victor Carrera
Junior Cybersecurity Analyst
