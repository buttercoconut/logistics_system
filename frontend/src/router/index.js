import { createRouter, createWebHistory } from 'vue-router';
import ProductList from '@/components/ProductList.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ProductList,
  },
  // 추가 라우트는 필요에 따라 확장
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
