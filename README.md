# KeyForge

KeyForge is a Django application for securely storing API keys.

## Local development

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the required environment variables:

   ```text
   DJANGO_SECRET_KEY=replace-with-a-development-secret
   FERNET_KEY=replace-with-a-generated-fernet-key
   DJANGO_DEBUG=true
   ```

   Generate a Fernet key with:

   ```bash
   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
   ```

4. Apply migrations and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Deploy to Render

This repository includes [`render.yaml`](./render.yaml), which configures a native
Python web service. In Render, create a Blueprint from the repository and provide
the `DATABASE_URL` environment variable for a managed PostgreSQL database.

The Blueprint automatically generates `DJANGO_SECRET_KEY`, collects static files
during the build, runs migrations when the service starts, and launches Gunicorn.
Set `FERNET_KEY` to a value generated with the command above before the first
deploy. Do not regenerate it after deployment: changing it makes existing
encrypted API keys unreadable.

Render provides `RENDER_EXTERNAL_HOSTNAME` automatically. The Django settings use
it to allow the deployed host and trust its HTTPS origin for CSRF protection.