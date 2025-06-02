# Reddit Clone

This repository contains a very small Reddit-like application split into two directories:

- `backend` – a Flask application with a MariaDB database.
- `frontend` – a React application bundled with webpack.

## Prerequisites

- Python 3
- Node.js (>=16)
- MariaDB server

## Setup

### Backend

See [backend/README.md](backend/README.md) for instructions on setting up the Flask backend and configuring the database connection.

### Frontend

See [frontend/README.md](frontend/README.md) for steps to run the React app.

## Database Models

The backend defines the following main models:

- **User** – stores users with a unique username and password.
- **Subreddit** – groups posts by topic.
- **Post** – created by users within a subreddit and may have many comments.
- **Comment** – text comments associated with a post and user.

These models are defined with SQLAlchemy in `backend/models.py` and map to MariaDB tables.

## Running

1. Start the backend (listening on port 5000 by default).
2. Start the frontend which fetches data from the backend.

This provides a minimal Reddit-style interface displaying posts and supporting basic create operations via the API.
