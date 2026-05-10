# Frontend API interface
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
});

export const getProducts = () => apiClient.get('/products');
export const createProduct = (product) => apiClient.post('/products', product);
export const getRoute = (start, goal) => apiClient.get('/route', { params: { start, goal } });
