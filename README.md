# UV FastAPI Project

A minimal FastAPI project using UV package installer.

## Setup

1. Install UV if you haven't already:
```bash
pip install uv
```

2. Create and activate a virtual environment:
```bash
uv venv
.venv/Scripts/activate  # On Windows
source .venv/bin/activate  # On Unix/MacOS
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

## Running the Application

Run the application using:
```bash
python main.py
```

The server will start at `http://localhost:8000`

You can access:
- API endpoint: `http://localhost:8000/`
- API documentation: `http://localhost:8000/docs` 