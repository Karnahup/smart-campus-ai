# Smart Campus AI 🎓

**An AI-Based Smart Campus Intelligence System**

Smart Campus AI is an individual final-year Bachelor of Computer Applications (BCA) project developed to simplify academic monitoring and campus management through a web-based application.

The system provides separate dashboards for students, faculty members, and administrators. It includes academic performance analysis, student risk assessment, placement predictions, and feedback sentiment analysis.

## 🚀 Features

### 👨‍🎓 Student Module
- Student login.
- Personalized student dashboard.
- View attendance and subject-wise marks.
- Calculate overall academic performance.
- Academic failure risk assessment.
- Placement probability category.
- Personalized study suggestions.
- View and update student profile.
- Submit feedback.

### 👨‍🏫 Faculty Module
- Faculty login.
- View student records.
- View and update faculty profile.

### 👨‍💼 Admin Module
- Admin login.
- View student records.
- Select and inspect individual student performance.
- View student attendance and marks.
- Update student academic records.
- View student feedback and sentiment results.

### 🤖 AI and Intelligence Features
- Academic risk assessment based on attendance and marks.
- Placement chance categorization.
- Automated study recommendations.
- Feedback sentiment analysis using TextBlob.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Database management |
| HTML | Frontend structure |
| CSS | Frontend styling |
| TextBlob | Feedback sentiment analysis |
| Machine Learning concepts | Academic analysis and predictions |

## 📂 Project Structure

```text
smart-campus-ai/
│
├── app.py
├── model.py
├── sentiment.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── student_dashboard.html
│   ├── faculty_dashboard.html
│   ├── admin_dashboard.html
│   ├── student_profile.html
│   └── faculty_profile.html
│
├── static/
│   └── CSS and other static assets
│
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Karnahup/smart-campus-ai.git
```

### 2. Navigate to the project folder

```bash
cd smart-campus-ai
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

- Install and start MySQL Server.
- Create a database named `smartcampus`.
- Create the required database tables and columns used by the application.
- Configure your local MySQL connection details in `app.py`.

**Note:** The database schema is not currently included in this repository.

Do not upload your personal database password or credentials to GitHub.

### 5. Run the application

```bash
python app.py
```

### 6. Open in your browser

```text
http://127.0.0.1:5000/
```

## 📊 Project Modules

| Module | Description |
|---|---|
| Authentication | Role-based login |
| Student Management | Academic records and profiles |
| Faculty Management | Faculty information |
| Administration | Student record management |
| Academic Analysis | Risk assessment and study suggestions |
| Placement Analysis | Placement chance categorization |
| Sentiment Analysis | Feedback classification |

## 🎯 Project Objective

The primary objective of Smart Campus AI is to demonstrate how web technologies, database management, and basic AI-based analysis can be combined to support academic monitoring and improve campus information management.

## 📌 Project Information

- **Project Name:** Smart Campus AI
- **Project Type:** Individual Academic Project
- **Degree:** Bachelor of Computer Applications (BCA)
- **Project Level:** Final Year
- **Repository:** [GitHub - Smart Campus AI](https://github.com/Karnahup/smart-campus-ai)

## 👨‍💻 Developer

Developed as an individual final-year BCA academic project.

---

*Smart Campus AI – Bringing Intelligence to Campus Management.*
