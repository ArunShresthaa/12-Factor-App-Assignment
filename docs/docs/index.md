# 12 Factor App Calculator API

This project is a simple calculator web API built following the [12 Factor App](https://12factor.net/) methodology. The API provides basic mathematical operations (addition, subtraction, multiplication, and division) through RESTful endpoints.

## What This Project Does

This FastAPI-based application provides a simple calculator service with the following endpoints:

* `/calc/add` - Adds two numbers
* `/calc/sub` - Subtracts the second number from the first
* `/calc/mul` - Multiplies two numbers
* `/calc/div` - Divides the first number by the second
* `/health` - Health check endpoint

All calculator endpoints accept POST requests with JSON body containing two numerical values (`a` and `b`).

## Running the Application

### Running Locally

1. Ensure you have Python 3.10 or newer installed
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app/main.py
   ```
4. Access the API at http://localhost:4444
5. For API documentation, visit http://localhost:4444/docs

### Running with Docker

1. Ensure you have Docker and Docker Compose installed
2. Build and run the container:
   ```
   docker-compose up
   ```
3. Access the API at http://localhost:2222
4. For API documentation, visit http://localhost:2222/docs

## Configuration

The application uses environment variables for configuration following 12 Factor principles:

* `PORT` - The port on which the application runs (default: 4444)
* `LOG_LEVEL` - Logging level (default: "info")
* `REDIS_URL` - Redis connection URL if needed (default: "None")

You can create a `.env` file in the root directory with these variables to configure the application.

## Documentation

The documentation is built using MkDocs
