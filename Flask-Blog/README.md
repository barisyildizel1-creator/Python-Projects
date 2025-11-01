# Flask Blog Application 📝

A full-featured blog application built with Flask, featuring user authentication, admin controls, and a rich text editor.

## Features ✨

- **User Authentication**: Register, login, and logout functionality
- **Admin Controls**: Admin-only post creation, editing, and deletion
- **Rich Text Editor**: CKEditor integration for blog content
- **Comments System**: Users can comment on blog posts
- **Responsive Design**: Bootstrap-powered responsive UI
- **Gravatar Integration**: Profile pictures from Gravatar

## Tech Stack 🛠️

- **Backend**: Flask (Python)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Forms**: Flask-WTF with WTForms
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy
- **Frontend**: Bootstrap 5, CKEditor
- **Deployment**: Gunicorn ready

## Project Structure 📁

```
├── main.py                 # Main Flask application
├── forms.py               # WTForms definitions
├── requirements.txt       # Dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version specification
├── templates/            # HTML templates
│   ├── index.html        # Home page
│   ├── post.html         # Blog post view
│   ├── login.html        # Login form
│   ├── register.html     # Registration form
│   └── ...
├── static/               # Static assets
│   ├── css/
│   ├── js/
│   └── assets/img/
└── instance/             # Database files (gitignored)
    └── posts.db
```

## Installation & Setup 🚀

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd day71
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Generate a secure SECRET_KEY (required!)
   python -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))" >> .env
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Visit** `http://localhost:5001`

## 🔐 Environment Variables & Security

### How .env Files Work

- **`.env`** - Your local secrets (git-ignored, never shared)
- **`.env.example`** - Template for others (shared in repository)

### For New Developers

If you clone this repository, the app will fail with:
```
ValueError: SECRET_KEY environment variable must be set!
```

This is intentional! Follow step 4 above to create your own `.env` file.

### For Production Deployment

Set these environment variables in your deployment platform:
- `SECRET_KEY` - Generate a secure random string
- `DATABASE_URL` - Will be provided automatically by most platforms

### Admin Access

The first user registered (ID: 1) automatically becomes the admin and can:
- Create new blog posts
- Edit existing posts
- Delete posts

## Environment Variables 🔧

For production deployment, set these environment variables:

- `SECRET_KEY`: Secure random string for session security
- `DATABASE_URL`: PostgreSQL connection URL (auto-provided by hosting platforms)

## Deployment 🌐

This application is ready for deployment on:

- **Heroku**
- **Railway**  
- **Render**
- **PythonAnywhere**

See `DEPLOYMENT.md` for detailed deployment instructions.

## Dependencies 📦

Key dependencies include:
- Flask 3.1.2
- Flask-SQLAlchemy 3.1.1
- Flask-Login 0.6.3
- Flask-WTF 1.2.2
- Flask-CKEditor 1.0.0
- Bootstrap-Flask 2.5.0
- SQLAlchemy 2.0.44

See `requirements.txt` for complete list.

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Screenshots 📸

### Home Page
The main blog feed showing all published posts.

### Blog Post
Individual blog post view with comments section.

### Admin Panel
Admin users can create, edit, and delete posts.

---

Built with ❤️ using Flask and Bootstrap