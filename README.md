# Portfolio

# Django Portfolio

A modern and responsive portfolio website built with Django to showcase projects, skills, and blog posts. Designed for developers, designers, or creatives to highlight their work and connect with visitors.

## Features

- **Project Showcase**: Display your projects with details like title, description, images, and technologies used.
- **Blog Integration**: Share insights, tutorials, or updates with a built-in blog system (CRUD operations).
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices.
- **Contact Form**: Allow visitors to send messages directly to your email.
- **Admin Panel**: Easily manage content (projects, blog posts) via Django's admin interface.
- **SEO-Friendly**: Meta tags, sitemaps, and clean URLs for better search engine visibility.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/django-portfolio.git
   cd django-portfolio

2.**Run the development server:**
python manage.py runserver
Visit http://localhost:8000 in your browser!

3.**Configuration**
Configure your settings in .env:

DEBUG=True
SECRET_KEY=your_django_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (SQLite by default; customize for PostgreSQL/MySQL)
DATABASE_URL=sqlite:///db.sqlite3

# Email settings (for contact form)
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password

**Usage**
Admin Dashboard: Access /admin to add projects, blog posts, or manage content.
Adding Projects: Upload images, add descriptions, and tag technologies.
Blog Management: Write and publish articles with markdown support (optional).
Customization: Modify templates in templates/ or styles in static/css/.

**Technologies Used**
Backend: Django 4.2+, Python 3.10+
Frontend: HTML5, CSS3, JavaScript (with Bootstrap 5 for styling)
Database: SQLite (default), PostgreSQL/MySQL supported
Deployment: Ready for Heroku, Docker, or AWS (add Procfile/Dockerfile as needed)

**Contributing**
Contributions are welcome! Follow these steps:
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.
