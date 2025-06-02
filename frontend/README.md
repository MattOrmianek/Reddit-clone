# Frontend

This directory contains a minimal React setup using webpack.

## Setup

1. Install dependencies:

```bash
npm install
```

This will install React along with the webpack tooling defined in
`package.json` (webpack, webpack-dev-server, Babel, etc.). The `npm start`
command relies on these local packages, so running `npm install` is required
before starting the server.

2. Start the development server:

```bash
npm start
```

The application will be available at `http://localhost:8080` by default.

### Configuring the API URL

The frontend reads the backend's base URL from the environment variable
`REACT_APP_API_URL`. Copy `.env.example` to `.env` and edit it if your backend
is not running on `http://localhost:5000`:

```bash
cp .env.example .env
# then edit .env to point to your backend
```
