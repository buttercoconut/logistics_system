# FastAPI application entry point
from fastapi import FastAPI
from .api.routers import items, route

app = FastAPI(title="Logistics System API")
app.include_router(items.router)
app.include_router(route.router)

# For demonstration, include Dijkstra logic in main
from .main import graph

@app.get("/route")
def get_route(start: str, goal: str):
    cost, path = graph.dijkstra(start, goal)
    return {"cost": cost, "path": path}
