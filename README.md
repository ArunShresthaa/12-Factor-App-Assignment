# FastAPI 12‑Factor Demo

A simple calculator microservice built with FastAPI, showcasing Twelve‑Factor best practices.

## Features
- Add, subtract, multiply, divide operations
- Health check endpoint

## Twelve‑Factor Highlights
- Config via environment variables
- Stateless processes
- Dockerized + Docker Compose
- GitHub Actions CI

## Getting Started
1. Copy `.env.example` to `.env` and set `PORT` (e.g. 8000).
2. Build and run with Docker:
   ```bash
   docker build -t fastapi-12factor-demo .
   docker run -e PORT=8000 fastapi-12factor-demo