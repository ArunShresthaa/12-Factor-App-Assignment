# 12 Factor App Calculator API

A simple calculator microservice built with FastAPI, showcasing [12 Factor App](https://12factor.net/) best practices.

## Features
- RESTful calculator endpoints (add, subtract, multiply, divide)
- Health check endpoint
- FastAPI documentation at `/docs`

## API Endpoints
- `/calc/add` - Adds two numbers
- `/calc/sub` - Subtracts the second number from the first
- `/calc/mul` - Multiplies two numbers
- `/calc/div` - Divides the first number by the second
- `/health` - Health check endpoint

All calculator endpoints accept POST requests with JSON body containing two numerical values (`a` and `b`).

## 12 Factor App Highlights
- Configuration via environment variables
- Stateless processes
- Dockerized + Docker Compose
- Dependency declaration (requirements.txt)

## Getting Started

### Running Locally

1. Ensure you have Python 3.10 or newer installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app/main.py
   ```
4. Access the API at http://localhost:4444
5. For API documentation, visit http://localhost:4444/docs

### Running with Docker

1. Create a `.env` file in the root directory (optional)
2. Build and run with Docker Compose:
   ```bash
   docker-compose up
   ```
3. Access the API at http://localhost:2222
4. For API documentation, visit http://localhost:2222/docs

## Configuration

The application uses environment variables for configuration:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | The port on which the application runs | 4444 |
| `LOG_LEVEL` | Logging level | "info" |
| `REDIS_URL` | Redis connection URL if needed | "None" |

## Documentation

Full documentation is available in the `docs` directory and can be built using MkDocs.
