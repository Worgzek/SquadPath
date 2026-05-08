# ITCareer Lab

ITCareer Lab is a career intelligence platform that combines:

- IT job aggregation
- Personalized career quizzes
- Learning roadmaps
- Daily learning tasks
- Job recommendation matching

The system collects IT job data from Vietnamese job platforms, analyzes roadmap data from roadmap.sh, and recommends suitable career paths based on user preferences and interests.

---

# Features

## Career Quiz Engine
Users answer a set of questions about:

- Interests
- Preferred work style
- Technical preferences
- Math/logic affinity
- Infrastructure vs frontend/backend inclination

The system returns:

- Top matching IT career paths
- Recommended learning roadmap
- Suggested jobs

---

## Learning Roadmaps

Integrated with roadmap.sh data.

Supported career paths include:

- Data Engineer
- Backend Developer
- Frontend Developer
- Fullstack Developer
- DevOps Engineer
- Data Scientist
- Machine Learning Engineer
- Mobile Developer
- Cybersecurity Engineer
- Cloud Engineer
- UI/UX Designer
- QA Engineer
- Game Developer
- Blockchain Developer
- AI Engineer
- Site Reliability Engineer
- Software Architect
- Product Manager
- Business Analyst
- Embedded Engineer

---

## Daily Learning Tasks

Users receive daily learning tasks generated from roadmap topics.

Features:

- Task completion tracking
- User progress tracking
- Topic-based learning progression

---

## IT Job Aggregation

The system scrapes and processes IT jobs from platforms such as:

- TopDev
- ITviec (planned)
- TopCV (planned)

Job data includes:

- Title
- Company
- Salary
- Skills
- Location
- Experience level

---

## Job Recommendation System

Recommended jobs are matched against:

- User career path
- Required skills
- Roadmap progress
- Skill overlap score

---

# Architecture

```text
                +-------------------+
                |   roadmap.sh API  |
                +---------+---------+
                          |
                          v
                 +----------------+
                 | Airflow DAG    |
                 | Roadmap ETL    |
                 +--------+-------+
                          |
                          v
+-------------+   +---------------+   +-------------+
| Job Scraper |-> | PostgreSQL DB | <-| Quiz Engine |
+-------------+   +---------------+   +-------------+
                          |
                          v
                   +-------------+
                   | FastAPI API |
                   +------+------+ 
                          |
                          v
                   +-------------+
                   | Flask Front |
                   +-------------+
```

---

# Tech Stack

## Backend

- Python
- FastAPI
- Flask

---

## Data Engineering

- Apache Airflow
- PostgreSQL
- Pandas
- BeautifulSoup
- Requests

---

## Infrastructure

- Docker
- Docker Compose

---

## Frontend

- HTML
- CSS
- Jinja2 Templates

---

# Project Structure

```text
ITCAREER_LAB/
│
├── api/
│   ├── routers/
│   └── main.py
│
├── dags/
│   ├── job_DAG.py
│   └── roadmap_DAG.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sql/
│
├── frontend/
│   ├── templates/
│   └── app.py
│
├── scripts/
│   ├── jobs/
│   │   ├── scrape_jobs.py
│   │   ├── transform_jobs.py
│   │   └── load_jobs.py
│   │
│   └── roadmap/
│       ├── fetch_roadmap.py
│       ├── transform_roadmap.py
│       ├── validate_roadmap.py
│       └── load_roadmap.py
│
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.frontend
└── requirements.txt
```

---

# Database Schema

## Main Tables

### career_paths
Stores supported IT career paths.

### roadmaps
Stores roadmap metadata.

### topics
Stores roadmap learning topics.

### daily_tasks
Stores generated learning tasks.

### jobs
Stores scraped IT job postings.

### skills
Stores normalized technical skills.

### job_skills
Many-to-many relationship between jobs and skills.

### roadmap_skills
Many-to-many relationship between roadmaps and skills.

### user_progress
Tracks user learning progress.

---

# Data Pipeline

## Roadmap Pipeline

```text
Fetch roadmap.sh
        ↓
Validate data
        ↓
Transform roadmap structure
        ↓
Load into PostgreSQL
```

Scheduled using Apache Airflow.

---

## Job Pipeline

```text
Scrape jobs
      ↓
Clean and normalize data
      ↓
Extract skills
      ↓
Load into PostgreSQL
```

Runs daily using Apache Airflow.

---

# API Endpoints

## Quiz

### Submit Quiz

```http
POST /quiz/submit
```

Returns:
- Top matching career paths
- Recommendation scores

---

## Roadmaps

### Get Roadmap

```http
GET /roadmap/{career_path}
```

---

## Daily Tasks

### Get Daily Tasks

```http
GET /daily-task/{user_id}
```

### Complete Task

```http
POST /daily-task/complete
```

---

## Jobs

### Get Recommended Jobs

```http
GET /jobs/{career_path}
```

---

# Setup

## Clone Repository

```bash
git clone <your-repo-url>
cd ITCAREER_LAB
```

---

## Environment Variables

Create `.env` file:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=itcareerlab
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

---

## Run with Docker

```bash
docker compose up --build
```

---

# Airflow

Access Airflow UI:

```text
http://localhost:8080
```

Available DAGs:

- roadmap_DAG
- job_DAG

---

# FastAPI Docs

Swagger documentation:

```text
http://localhost:8000/docs
```

---

# Future Improvements

- Skill extraction using NLP
- Elasticsearch job search
- AI-powered roadmap recommendation
- Resume analysis
- Kafka streaming pipeline
- Redis caching
- User authentication
- Analytics dashboard
- Skill gap analysis

---

# Contributors

## Data Engineering / Backend
- hieu.wz

## Backend / Frontend
- Thanh mau sac

---

# License

MIT License
