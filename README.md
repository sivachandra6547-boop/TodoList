# ✅ Django TODO App

A simple and clean Task Management web application built with Django.
Users can create, update, mark complete, and delete tasks.

---

## 🚀 Features

- Add new tasks
- Mark tasks as complete / incomplete
- Edit existing tasks
- Delete tasks
- View all tasks and completed tasks separately
- Django Admin panel support

---

## 🛠️ Tech Stack

- **Language** — Python 3.x
- **Framework** — Django
- **Database** — SQLite (default)
- **Frontend** — HTML, Bootstrap 5
- **Version Control** — Git & GitHub

---

## 📁 Project Structure

```
TODO/
├── env/                    ← virtual environment (not committed)
├── todo/                   ← main Django app
│   ├── migrations/
│   ├── templates/
│   │   └── home.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todomain/               ← Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/todo-django.git
cd todo-django
```

**2. Create and activate virtual environment**
```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac / Linux
python -m venv env
source env/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create superuser (optional — for admin panel)**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Open in browser**
```
http://127.0.0.1:8000/
```

---

## 📋 Task Model

```python
class Task(models.Model):
    task       = models.CharField(max_length=250)
    is_created = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
```

---

## 📸 Screenshots

> Add your screenshots here after running the project.

---

## 🔑 Admin Panel

Visit `http://127.0.0.1:8000/admin/` and login with your superuser credentials to manage tasks directly.

---

## 📦 Requirements

Generate with:
```bash
pip freeze > requirements.txt
```

---

## 🌱 Future Improvements

- [ ] User authentication — each user sees only their own tasks
- [ ] Due dates for tasks
- [ ] Task priority levels
- [ ] REST API with Django REST Framework
- [ ] Deploy to Railway / Render

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).