# KeyForge

KeyForge is a secure personal vault for API keys, token & secrets. Built with Django, it allows you create private dashboard where you can store your credentials in an encrypted format, update them whenever needed, & keep your project environment organised without hardcoding secrets into your code.

## What is KeyForge?

Most of the developers keep API keys in `.env` files, config files, or scattered notes. That works for a small project, but it gets messy as the project grows. So, KeyForge gives you a single place to manage credentials with a clean interface and strong encryption at rest.

Easch User has their own vault, and every saved secret is encrypted before it is stored in the database using Python's `cryptography.fernet` library.

## How it works?

1. Create an account and login.
2. Open your personal vault dashboard.
3. Add a key with a name, provider and secret value.
4. KeyForge encrypts the value before saving it.
5. Update, delete, or manage keys from the same vault/dashboard.

## Features

- User authentication and account management
- Per user vaults with separate data
- Encrypted API key storage using Fernet
- Add, update and delete credentials
- Password change and email update flows
- Ready for local SQLite development and PostgreSQL in production
- Railway deployment configuration included

## Project Structue

```text
keyforge/               # Django project's settings and config
vault/                  # app's logic, views, models, templates
manage.py               # project's entry point
requirements.txt        # Python Libraries
railway.toml             # Railway deployment config
```

## Local Development

1. Create and activate a virtual env:

    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Setup environment variables in a `.env` file:

    ```env
    DJANGO_SECRET_KEY=replace-with-development-secret
    FERNET_KEY=replace-with-generated-fernet-key
    DJANGO_DEBUG=True
    ```

    Generate Fernet key with:

    ```bash
    python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
    ```
4. Run database migrations and start the app:

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```
5. Open the app in your browser at:

    ```text
    http://127.0.0.1:8000/
    ```

## Deployment on Railway

This repo includes a [`railway.toml`](./railway.toml) configuration for Railway.
Railway keeps the service running instead of putting it to sleep after inactivity.

To deploy:

1. Push this repo to GitHub.
2. In Railway, create a new project and deploy this repository.
3. Add a PostgreSQL service and provide its connection string as `DATABASE_URL`.
4. Add `DJANGO_SECRET_KEY` and `FERNET_KEY` as Railway variables.
5. Set `DJANGO_ALLOWED_HOSTS` to the Railway domain (for example,
   `.up.railway.app`) and `DJANGO_CSRF_TRUSTED_ORIGINS` to the matching
   HTTPS origin (for example, `https://*.up.railway.app`).
6. Generate a Railway domain, then deploy and verify the app is running.

Note: Don't rotate `FERNET_KEY` after keys have been stored. Doing so makes
previously encrypted secrets unreadable.

## Built with

- Python
- Django
- PostgreSQL /SQLite
- Fernert encryption
- Railway deployment support

# License

This project is licensed under the [MIT License](./LICENSE)