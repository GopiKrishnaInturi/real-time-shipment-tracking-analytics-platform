# Real-Time Shipment Tracking Analytics Platform

High-performance shipment tracking analytics platform built using Python, FastAPI, PostgreSQL, Docker, Redis, and AWS-ready deployment architecture.

## Features

- Real-time shipment event ingestion
- Shipment tracking APIs
- Distributed event processing
- Delay analytics
- SQL reporting
- Retry handling
- Dockerized deployment
- AWS-ready infrastructure

## Run

```bash
docker-compose up --build
```

## Endpoints

- POST /shipments
- POST /events
- GET /health