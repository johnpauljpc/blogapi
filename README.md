# 📝 Blog API — Versioned with Django REST Framework

This project is a learning-focused implementation of a Blog API using **Django REST Framework (DRF)**. It is structured into five versions, each demonstrating a different style of API view construction. The goal is to help developers understand the progression from simple to advanced techniques in DRF.

---

## 🔁 Version Overview

- **version1** uses **Function-Based Views** with the `@api_view` decorator. This version is the most explicit and suitable for understanding how DRF handles requests under the hood.

- **version2** adopts **Class-Based Views** using the `APIView` class. It introduces object-oriented design and separates logic into class methods like `get()`, `post()`, `put()`, and `delete()`.

- **version3** implements **Generic Views** provided by DRF such as `ListCreateAPIView` and `RetrieveUpdateDestroyAPIView`. These views offer significant code reduction and automatic behavior for common API patterns.

- **version4** combines **Generic Views with Mixins**, allowing you to compose only the functionality you need, providing more control while still reducing boilerplate.

- **version5** takes advantage of **ViewSets and Routers**, the most concise and DRF-idiomatic way to build fully RESTful APIs with automatic URL routing.

Each version is isolated in its own folder and contains its own README, views, URLs, and test files.



---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/johnpauljpc/blogapi.git
   cd blogapi

2. Set up a virtual environment (optional but recommended):
    `python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate`


3. Install dependencies: 
    `pip install -r requirements.txt`

4. Run migrations and start the development server:
    ```bash
    python manage.py migrate
    python manage.py runserver

5. Access different versions via versioned API paths:

-   /api/v1/

-   /api/v2/

-   /api/v3/

-   /api/v4/

-   /api/v5/

## 🎯 Goals
This project is ideal for:

- Comparing DRF view styles side-by-side

* Teaching DRF in a layered, progressive manner

+ Understanding trade-offs between verbosity, control, and automation in API design




