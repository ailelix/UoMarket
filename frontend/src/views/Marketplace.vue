<template>
  <marketplace_header />
  <div class="bg-white">
    <div class="mx-auto max-w-10xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900">
        <span v-if="route.query.keyword">Search Results for "{{ route.query.keyword }}"</span>
        <span v-else-if="route.query.category">Category: {{ route.query.category }}</span>
        <span v-else>Recently Added</span>
      </h2>
      
      <div v-if="items.length === 0" class="mt-12 text-center text-gray-500">
        <p class="text-lg">No items available in the marketplace yet.</p>
      </div>

      <div v-else class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div v-for="item in items" :key="item.id" class="group relative">
          <img :src="item.image || 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg'" :alt="item.name" class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80" />
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm text-gray-700">
                <router-link :to="'/item?id=' + item.id">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  {{ item.name }}
                </router-link>
              </h3>
              <p class="mt-1 text-sm text-gray-500">Item #{{ item.id }}</p>
            </div>
            <p class="text-sm font-medium text-gray-900">£{{ (item.price_cents || 0) / 100 }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import marketplace_header from '@/components/MarketPlace-header.vue';
import axios from 'axios';

const items = ref([]);
const route = useRoute();

const fetchItems = async () => {
  try {
    let url = '/api/items?open=true';
    if (route.query.keyword) {
      url += `&keyword=${encodeURIComponent(route.query.keyword)}`;
    }
    if (route.query.category) {
      url += `&category=${encodeURIComponent(route.query.category)}`;
    }
    const res = await axios.get(url);
    items.value = res.data;
  } catch (err) {
    console.error("Failed to load items");
  }
};

onMounted(fetchItems);
watch(() => route.query, fetchItems, { deep: true });
</script>