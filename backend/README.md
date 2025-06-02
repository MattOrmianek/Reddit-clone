# Backend

This directory contains the Flask backend for the Reddit clone.

## Setup

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and adjust the `DATABASE_URL` for your MariaDB instance.

3. Initialize the database tables:

```bash
python -c "from app import db, app; app.app_context().push(); db.create_all()"
```

4. Run the development server:

```bash
flask --app app run
```
