<template>
  <div class="product-list">
    <h2>Product List</h2>
    <ul>
      <li v-for="product in products" :key="product.id">
        {{ product.name }} - {{ product.price }}원
      </li>
    </ul>
  </div>
</template>

<script>
import api from '@/api/api.js';
export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
    };
  },
  async created() {
    try {
      const response = await api.getProducts();
      this.products = response.data;
    } catch (err) {
      console.error('Failed to fetch products', err);
    }
  },
};
</script>

<style scoped>
.product-list {
  padding: 1rem;
}
</style>