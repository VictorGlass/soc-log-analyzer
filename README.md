# 🛡️ SOC Log Analyzer (Python)

A simple but powerfull **Security Operations Center (SOC)** simulation tool built with Python.

This project analyzes log files and detects suspicious activities such as brute force attacks and abnormal login behavior.


## 🚀 Features

- Detects multiple failed login attempts (Brute Force)
- Identifies successful logins after multiple failures
- Flags suspicious activity based on thresholds
- Generates a simple SOC-style analysis report


## 🧠 What I Learned

- Log analysis fundamentals
- Event correlation (failed + successful logins)
- Basic threat detection logic
- Writing clean and readable Python code


## 📦 Technologies

- Python 3
- File handling
- Basic data structures (dictionaries)


## ▶️ Usage

1. Clone the repository

````
git clone https://github.com/VictorGlass/soc-log-analyzer.git
````

2. Run the script

````
python analyzer.py
````


## 📊 Example Output

````

ALERT: Possible brute force attack from 192.168.1.10

ALERT: Successful login AFTER multiple failures -> 192.168.1.10

ALERT: High suspicious activity from 192.168.1.20

````


## 🎯 Purpose

This project was created to simulat how a SOC analyst detects threats using log analysis and patterne recognition.


## 🛡️ Disclaimer

This project is for educational purposes only.


## 👨‍💻 Author

Victor Carrera
Junior Cybersecurity Analyst