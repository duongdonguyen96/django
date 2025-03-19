# 🏗️ Django Project Template 🚀

![Django](https://img.shields.io/badge/Django-5.x-green?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-✔️-blue?style=flat-square&logo=docker)

📌 **Description**  
A Django project running on Docker, following the Django Style Guide, and including structured commit rules and branch naming conventions.


---

## ⚙️ Installation & Setup

### 🏗️ 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo.git
cd your-repo
```

### 🛠️️ 2️⃣ Setup Environment Variables
```bash
cp .env.example .env
```

### 🐳 3️⃣ Build the Docker 
```bash
cp .env.example .env
```
The Django server will be available at: http://localhost:8000/api/docs/#/  🎉

### 🔧 4️⃣ Apply Migrations
```bash
docker-compose exec web python manage.py migrate
```

### 🚀 5️⃣ Create a Superuser
```bash
docker-compose exec web python manage.py createsuperuser
```

---


## 📌 Git Workflow


### 🌿 Branch Naming Conventions

Use **clear and structured branch names** following this pattern:


| 🏷️ **Branch Type** | 🔥 **Pattern**              | 📌 **Example**               |
|----------------|----------------------|--------------------------|
| **Feature**    | `feat/<feature-name>` | `feat/user-authentication` |
| **Bug Fix**    | `fix/<bug-description>` | `fix/login-issue`         |
| **Refactor**   | `refactor/<module>`  | `refactor/db-structure`   |
| **Docs**       | `docs/<section>`     | `docs/api-documentation`  |
| **Hotfix**     | `hotfix/<critical-fix>` | `hotfix/payment-error`    |

### 📌 Example:

```bash
git checkout -b feat/user-profile
```

### 📝 Commit Message Structure

Follow **Conventional Commits** format:


### ✅ Allowed Commit Types:

- [Type][Task_id]: Message

| 🏷️ **Type**     | 🔥 **Usage**                                       | 🎯 **Example**                                |
|---------------|--------------------------------------------|-----------------------------------------------|
| `feat`       | Add a **new feature**                     | `[feat][no_1]: add JWT authentication`        |
| `fix`        | Fix a **bug**                             | `[fix][no_1]: resolve migration issue`        |
| `docs`       | Documentation changes                    | `[docs][no_1]: update installation guide`     |
| `style`      | Code formatting, linting (no logic changes) | `[style][no1]: fix indentation issues`        |
| `refactor`   | Code improvements (without new features or bug fixes) | `[refactor][no_1]: optimize database queries` |
| `test`       | Add or modify **tests**                   | `[test][no_1]: add unit tests for API`        |
| `chore`      | Maintenance tasks (build scripts, dependencies) | `[chore][no_1]: upgrade dependencies`         |

---

### ✨ Commit Example:

```bash
git commit -m "[feat][no_1]: implement OAuth login"
git commit -m "[fix][no_1]: correct total price calculation"
```

---

## 📂 Project Structure

```bash
📦 django/
 ┣ 📂 config/              # Project-level configurations
 ┃ ┣ 📜 __init__.py
 ┃ ┣ 📜 asgi.py
 ┃ ┣ 📜 settings.py        # Main Django settings
 ┃ ┣ 📜 urls.py            # Root URL routing
 ┃ ┗ 📜 wsgi.py
 ┃
 ┣ 📂 src/                 # Source code directory
 ┃ ┣ 📂 core/              # Core utilities
 ┃ ┃ ┣ 📜 base.py
 ┃ ┃ ┗ 📜 until.py
 ┃ ┃
 ┃ ┣ 📂 third_party/       # Integrations with external services
 ┃ ┃ ┗ 📜 __init__.py
 ┃
 ┣ 📂 staticfiles/         # Static assets
 ┃
 ┣ 📂 v1/                  # API Versioning (Organized by domain)
 ┃ ┣ 📂 orders/            # Orders module (To be implemented)
 ┃ ┣ 📂 products/          # Products module
 ┃ ┃ ┣ 📂 migrations/
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 selectors.py     # Query functions for retrieving objects
 ┃ ┃ ┣ 📜 serializers.py   # DRF serializers
 ┃ ┃ ┣ 📜 services.py      # Business logic layer
 ┃ ┃ ┣ 📜 tests.py
 ┃ ┃ ┣ 📜 urls.py
 ┃ ┃ ┗ 📜 views.py
 ┃ ┃
 ┃ ┗ 📂 users/             # Users module (To be implemented)
 ┃




