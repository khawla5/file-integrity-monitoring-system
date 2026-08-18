# 🔐 File Integrity Monitoring System (FIM)

A File Integrity Monitoring (FIM) system developed using **Python**, **Flask**, and **React** to monitor critical files, detect unauthorized modifications, and display file integrity status through a real-time dashboard.

---

## 📖 Project Overview

File Integrity Monitoring (FIM) is an essential cybersecurity technique used to verify that important files have not been modified, deleted, or tampered with without authorization.

This project monitors selected files by generating a **SHA-256 hash** for each file and comparing it with the previously stored hash value. Any modification is detected and displayed through a web dashboard.

The system was implemented and tested using sample data to simulate real-world file monitoring scenarios.

---

## ✨ Features

- 🔍 Monitor important files.
- 🔐 Generate SHA-256 hashes.
- 🚨 Detect file modifications.
- 📁 Detect newly added files.
- 📊 Interactive dashboard using React.
- 🔄 Automatic refresh every 5 seconds.
- 🌐 REST API using Flask.
- 💾 Store file information using SQLite and SQLAlchemy.

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- SQLAlchemy
- SQLite

### Frontend
- React.js
- JavaScript
- HTML
- CSS

### Security
- SHA-256 Hashing

---

## 📂 Project Structure

```
file-integrity-monitoring-system
│
├── backend
│   ├── app.py
│   ├── scanner.py
│   ├── watcher.py
│   ├── database.py
│   ├── hash_utils.py
│   └── fim.db
│
├── frontend
│
├── important-files
│   ├── config.txt
│   ├── settings.json
│   └── database.sql
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/khawla5/file-integrity-monitoring-system.git
```

### Backend

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python3 scanner.py

python3 app.py
```

Backend runs on

```
http://127.0.0.1:5000
```

---

### Frontend

```bash
cd frontend

npm install

npm start
```

Frontend runs on

```
http://localhost:3000
```

---

## 🚀 How It Works

1. Select files to monitor.
2. Generate SHA-256 hashes.
3. Save hashes in the database.
4. Continuously monitor files.
5. Detect file changes.
6. Update the dashboard automatically.
7. Notify the user when modifications occur.

---

## 📷 Screenshots

### Dashboard Home

![Dashboard Home](screenshots/dashboard-home.png)

---

### Monitoring Dashboard

![Monitoring Dashboard](screenshots/dashboard-monitoring.png)

---

### Modified Files Detection

![Modified Files](screenshots/dashboard-modified-files.png)

---

### Alert Notification

![Alert Notification](screenshots/dashboard-alerts.png)

---

### Final Dashboard UI

![Final Dashboard](screenshots/dashboard-final-ui.png)

### Dashboard

> Screenshots will be added soon.

---

## 🧪 Testing

The system was successfully tested using sample files.

Test scenarios included:

- ✅ Creating new files
- ✅ Modifying existing files
- ✅ Verifying file integrity
- ✅ Real-time dashboard updates

---

## 🚀 Future Improvements

- 🔐 User Authentication
- 📊 Analytics Dashboard
- 📈 Charts and Statistics
- 📜 File Change History
- 📄 Export Reports (PDF/CSV)
- 📧 Email Notifications
- 🔔 Real-time Notifications
- 🌙 Dark/Light Mode
- ☁️ Cloud Database Support

---
## How to Run the Project

### Frontend

Open a terminal and run:

```bash
cd frontend
npm install
npm start
```

### Backend

Open another terminal and run:

```bash
cd backend
pip install flask flask-cors sqlalchemy watchdog
python scanner.py
python app.py
```

### Notes

* Run the Frontend and Backend in separate terminals.
* Make sure Node.js and Python are installed before running the project.



## 👩‍💻 Author

**Khawla**

Computer Science Graduate

Interested in Cybersecurity, Information Security, Data Analysis, and Web Development.

GitHub:
https://github.com/khawla5

---

## 📄 License

This project is developed for educational and learning purposes.
