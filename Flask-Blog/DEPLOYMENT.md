# Deployment Guide

## Files Ready for Deployment ✅

Your Flask blog application is now ready for deployment! Here are the key files:

### Core Files:
- `main.py` - Your main Flask application
- `forms.py` - Form definitions
- `requirements.txt` - Dependencies for your app
- `templates/` - HTML templates
- `static/` - CSS, JS, and images

### Deployment Files Created:
- `Procfile` - Tells deployment platform how to run your app
- `runtime.txt` - Specifies Python version
- `requirements-production.txt` - Production dependencies (includes PostgreSQL support)

## Deployment Options:

### 1. Heroku
1. Create account at heroku.com
2. Install Heroku CLI
3. Run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku main
   ```

### 2. Railway
1. Create account at railway.app
2. Connect your GitHub repository
3. Railway will automatically deploy using your Procfile

### 3. Render
1. Create account at render.com
2. Connect your GitHub repository
3. Choose "Web Service" and configure

## Environment Variables to Set:

For production deployment, set these environment variables:

- `SECRET_KEY` - A secure random string for session security
- `DATABASE_URL` - PostgreSQL URL (provided by hosting platform)

## Database:
- Development: Uses SQLite (posts.db)
- Production: Will use PostgreSQL when DATABASE_URL is set

Your requirements.txt is correct and includes all necessary dependencies!