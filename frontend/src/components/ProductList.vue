<template>
  <div>
    <h1>Product List</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        {{ product.name }} - ${{ product.price }}
      </li>
    </ul>
    <h2>Add Product</h2>
    <form @submit.prevent="addProduct">
      <input v-model="newProduct.name" placeholder="Name" required />
      <input v-model.number="newProduct.price" placeholder="Price" required />
      <button type="submit">Add</button>
    </form>
    <h2>Route Optimization</h2>
    <form @submit.prevent="findRoute">
      <input v-model="routeStart" placeholder="Start" required />
      <input v-model="routeGoal" placeholder="Goal" required />
      <button type="submit">Find Route</button>
    </form>
    <div v-if="routeResult">
      <p>Cost: {{ routeResult.cost }}</p>
      <p>Path: {{ routeResult.path.join(' -> ') }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { getProducts, createProduct, getRoute } from '@/api/api.js';

const products = ref([]);
const newProduct = ref({ name: '', price: 0 });
const routeStart = ref('');
const routeGoal = ref('');
const routeResult = ref(null);

const loadProducts = async () => {
  const res = await getProducts();
  products.value = res.data;
};

const addProduct = async () => {
  await createProduct(newProduct.value);
  newProduct.value = { name: '', price: 0 };
  await loadProducts();
};

const findRoute = async () => {
  const res = await getRoute(routeStart.value, routeGoal.value);
  routeResult.value = res.data;
};

onMounted(loadProducts);
</script>
