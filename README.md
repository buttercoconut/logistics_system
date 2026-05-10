# README for logistics_system
# Logistics System

## Overview
This repository contains a simple logistics system with a FastAPI backend and a Vue 3 frontend. The backend provides CRUD operations for products and a route optimization endpoint using Dijkstra's algorithm. The frontend displays products, allows adding new products, and shows the optimal route between two locations.

## Backend
- **Framework**: FastAPI
- **Key Features**:
  - CRUD for products (in-memory store)
  - Route optimization using Dijkstra's algorithm
- **Run**:
  ```bash
  cd backend
  pip install -r requirements.txt
  uvicorn api.main:app --reload
  ```

## Frontend
- **Framework**: Vue 3 + Vite
- **Key Features**:
  - Product list and add form
  - Route optimization form
- **Run**:
  ```bash
  cd frontend
  npm install
  npm run dev
  ```

## Testing
- Backend tests can be added using `pytest`.
- Frontend tests can be added using `vitest`.

## Future Work
- Persist products in a database.
- Add authentication.
- Improve UI/UX.
