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
# Run this from the project root so the `backend` package can be imported
python -c "from backend.app import db, app; app.app_context().push(); db.create_all()"
```

4. Run the development server:

```bash
# Run this from the project root so Flask can import the backend package
flask --app backend.app run
```
