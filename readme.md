# 🎓 Student Exam Performance Predictor
## End to end ML Project

> An end-to-end Machine Learning web application that predicts student math scores based on various demographic and academic factors — fully containerized with Docker and deployed on AWS ECS Fargate via CI/CD pipeline.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)
![AWS](https://img.shields.io/badge/AWS-ECS%20Fargate-FF9900?style=flat-square&logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=flat-square&logo=scikitlearn)

---

## 📸 Preview

| Home Page | Prediction Result |
|---|---|
| Fill in student details | Get predicted math score instantly |

---

## 🧠 What It Does

Given a student's:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Writing score
- Reading score

The model predicts their **Math Score** using a trained ML pipeline.

---

## 🏗️ Project Architecture

```
Student Input (Web Form)
        ↓
Flask Web App (application.py)
        ↓
Custom Data Pipeline (src/pipeline/predict_pipeline.py)
        ↓
Preprocessor (artifacts/preprocessor.pkl)
        ↓
Trained ML Model (artifacts/model.pkl)
        ↓
Predicted Math Score
```

### Deployment Architecture
```
Push to GitHub (main branch)
        ↓
GitHub Actions triggered
        ↓
Docker image built on EC2 self-hosted runner
        ↓
Image pushed to AWS ECR
        ↓
ECS Task Definition updated
        ↓
ECS Fargate Service redeployed
        ↓
App live on public IP :8080
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Web Framework | Flask |
| ML Library | scikit-learn |
| Data Processing | pandas, numpy |
| Containerization | Docker |
| Container Registry | AWS ECR |
| Deployment | AWS ECS Fargate |
| CI/CD | GitHub Actions |
| Runner | Self-hosted EC2 (Ubuntu) |

---

## ⚙️ Run Locally

### Prerequisites
- Python 3.8+
- Git
- pip

### Step 1 — Clone the repository
```bash
git clone https://github.com/RaviNamdeoo/mlproject.git
cd mlproject
```

### Step 2 — Create and activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Train the model (generates pkl files)
```bash
python -m src.components.data_ingestion
```

### Step 5 — Run the Flask app
```bash
python application.py
```

### Step 6 — Open in browser
```
http://localhost:8080/predictdata
```

---

## 🐳 Run with Docker

### Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))

### Step 1 — Clone the repo
```bash
git clone https://github.com/RaviNamdeoo/mlproject.git
cd mlproject
```

### Step 2 — Build Docker image
```bash
docker build -t student-performance .
```

### Step 3 — Run the container
```bash
docker run -p 8080:8080 student-performance
```

### Step 4 — Open in browser
```
http://localhost:8080/predictdata
```

---

## ☁️ AWS Deployment Setup (CI/CD)

### Prerequisites
- AWS Account
- GitHub repository
- Docker installed on local machine

### Step 1 — AWS Setup

**Create ECR Repository**
```
AWS Console → ECR → Create Repository
Name: student-performance
```

**Create ECS Cluster**
```
AWS Console → ECS → Clusters → Create Cluster
Name: Student-cluster-2026
Type: AWS Fargate (serverless)
```

**Create Task Definition**
```
AWS Console → ECS → Task Definitions → Create
Family: student-performance-task
Launch type: Fargate
CPU: 512 | Memory: 1024
Container name: student-performance-container
Port: 8080
```

**Create ECS Service**
```
Inside your cluster → Services → Create
Name: student-performance-service
Desired tasks: 1
```

### Step 2 — IAM User for GitHub Actions
```
AWS Console → IAM → Users → Create User
Name: github-actions-user

Attach these policies:
✅ AmazonECS_FullAccess
✅ AmazonEC2ContainerRegistryFullAccess
✅ AmazonEC2FullAccess
✅ IAMFullAccess

Generate Access Keys → copy both keys
```

### Step 3 — GitHub Secrets
```
GitHub Repo → Settings → Secrets → Actions

Add:
AWS_ACCESS_KEY_ID     = <your-access-key>
AWS_SECRET_ACCESS_KEY = <your-secret-key>
```

### Step 4 — Add task definition JSON
Create `.aws/task_definition.json` in your repo with your ECS task definition (get it from AWS Console → Task Definitions → JSON tab, remove auto-generated fields).

### Step 5 — Push to main branch
```bash
git add .
git commit -m "deploy"
git push origin main
```

GitHub Actions will automatically build, push to ECR, and deploy to ECS Fargate! ✅

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers:

```
1. Checkout code
2. Configure AWS credentials
3. Login to Amazon ECR
4. Build Docker image
5. Push image to ECR
6. Update ECS task definition with new image
7. Deploy to ECS Fargate service
8. Wait for service stability
```

---

## 💰 Cost Management

To avoid AWS charges when not using:

```
ECS → Services → student-performance-service
→ Update → Desired tasks: 0

EC2 → Instances → Stop your runner instance
```

Restart when needed:
```
EC2 → Start instance
ECS → Update service → Desired tasks: 1
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Ravi Namdeoo**  
[![GitHub](https://img.shields.io/badge/GitHub-RaviNamdeoo-181717?style=flat-square&logo=github)](https://github.com/RaviNamdeoo)

---

> ⭐ If this project helped you, please give it a star!
