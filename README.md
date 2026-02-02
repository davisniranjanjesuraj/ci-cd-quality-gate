# CI/CD Quality Gate Implementation

##  Overview
This project demonstrates an **enterprise-grade CI/CD quality gate pipeline** that enforces automated testing, UI validation, and code coverage thresholds before allowing a build to pass.

The system integrates **PyTest**, **Selenium**, **Docker**, and **GitHub Actions** to simulate a real-world DevOps release validation process used in production environments.

---

##  Objectives
- Enforce **automated quality gates** in CI/CD
- Block builds if:
  - Tests fail
  - Coverage falls below threshold
- Generate **release-grade test artifacts**
- Align with **enterprise DevOps & QA standards**

---

##  Tech Stack

| Category         | Tools                                |
|------------------|--------------------------------------|
| Language         | Python 3.10                          |
| Backend          | Flask                                |
| Testing          | PyTest, PyTest-Cov, PyTest-HTML      |
| UI Automation    | Selenium (Headless Chrome)           |
| Containerization | Docker, Docker Compose               |
| CI/CD            | GitHub Actions                       |
| Reporting        | HTML Report, JUnit XML, Coverage XML |

---
##  Application Under Test
A lightweight Flask application exposing:
- `/health` → Health check endpoint
- `/login` → Authentication endpoint

The application is **bootstrapped by PyTest itself** to allow accurate coverage measurement.

---

##  Test Strategy

### Test Types Implemented
- **API Tests**
  - Health endpoint validation
- **UI Tests**
  - Login validation using Selenium (headless Chrome)

### Why Selenium?
UI validation ensures:
- Frontend–backend integration works
- API responses render correctly in browser context
- CI stability with real browser execution

---

##  Quality Gates Enforced

| Gate | Rule |
|----|----|
| Test Execution | All tests must pass |
| Coverage | Minimum **80%** required |
| Reports | HTML + XML artifacts must be generated |

Configured in `pytest.ini`:
```ini
--cov=app
--cov-fail-under=80
--html=reports/test_report.html
--junitxml=reports/junit_report.xml

```
## How to Run Locally

###Prerequisites
Docker Desktop
Docker Compose
Git (optional)

#Step 1: Clone Repository
git clone <your-repo-url>
cd ci-cd-quality-gate

#Step 2: Ensure Reports Directory Exists
mkdir -p reports

# Step 3: Build and Run Tests
```
docker-compose down -v
docker-compose build --no-cache
docker-compose run tests
```

