"""
FastAPI application for logistics_system.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Logistics System API")

# In-memory product store for demo purposes
products = []

class Product(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

@app.post("/products", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products", response_model=List[Product])
def list_products():
    return products

# Dijkstra's algorithm for route optimization (simplified)
from heapq import heappush, heappop

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, src, dest, weight):
        self.edges.setdefault(src, []).append((dest, weight))

    def dijkstra(self, start, goal):
        queue = [(0, start, [])]
        visited = set()
        while queue:
            cost, node, path = heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            path = path + [node]
            if node == goal:
                return cost, path
            for neighbor, weight in self.edges.get(node, []):
                if neighbor not in visited:
                    heappush(queue, (cost + weight, neighbor, path))
        return float("inf"), []

# Example graph (nodes are location IDs)
graph = Graph()
graph.add_edge("A", "B", 5)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("B", "D", 2)
graph.add_edge("C", "D", 4)

@app.get("/route")
def get_route(start: str, goal: str):
    cost, path = graph.dijkstra(start, goal)
    return {"cost": cost, "path": path}
