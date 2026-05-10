import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000/api',
  timeout: 10000,
});

export default {
  getProducts: () => apiClient.get('/products/'),
  // 추가 API 엔드포인트는 필요에 따라 확장
};