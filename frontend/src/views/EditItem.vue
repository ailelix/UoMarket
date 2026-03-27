<template>
  <div class="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-2xl mx-auto bg-white rounded-3xl shadow-sm border border-slate-200 p-8">
      <h2 class="text-2xl font-bold text-slate-900 mb-6">Edit Item</h2>
      <form @submit.prevent="submitItem" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-slate-700">Title</label>
          <input v-model="form.title" required class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700">Description</label>
          <textarea v-model="form.description" rows="3" class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm"></textarea>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-slate-700">Price (£)</label>
            <input v-model.number="form.price" type="number" step="0.01" required min="0" class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700">Condition</label>
            <select v-model="form.condition" required class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
              <option value="new">New</option>
              <option value="like_new">Like New</option>
              <option value="good">Good</option>
              <option value="fair">Fair</option>
              <option value="poor">Poor</option>
            </select>
          </div>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-slate-700">Categories (comma separated)</label>
          <input v-model="form.categories" type="text" placeholder="e.g. Textbooks, Electronics" class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
        </div>

        <div class="flex items-center gap-2 border-t border-slate-200 pt-6">
          <input type="checkbox" v-model="form.is_auction" class="h-4 w-4 rounded border-gray-300 text-uom-purple focus:ring-uom-purple">
          <label class="text-sm font-medium text-slate-700">Is Auction?</label>
        </div>

        <div v-if="form.is_auction" class="mt-4">
          <label class="block text-sm font-medium text-slate-700">Auction End Time</label>
          <input v-model="form.endtime" type="datetime-local" :required="form.is_auction" class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
        </div>

        <div class="mt-4">
          <label class="block text-sm font-medium text-slate-700">Status</label>
          <select v-model="form.status" required class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
            <option value="active">Active</option>
            <option value="reserved">Reserved</option>
            <option value="sold">Sold</option>
            <option value="removed">Removed</option>
          </select>
        </div>

        <div class="flex gap-4">
            <button type="button" @click="router.back()" class="w-full flex justify-center py-3 px-4 border border-slate-300 rounded-xl shadow-sm text-sm font-bold text-slate-700 bg-white hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-500">
            Cancel
            </button>
            <button type="submit" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-xl shadow-sm text-sm font-bold text-white bg-uom-purple hover:bg-uom-purple/90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-uom-purple">
            Save Changes
            </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const route = useRoute();

const form = reactive({
  title: '',
  description: '',
  price: 0,
  condition: 'good',
  status: 'active',
  is_auction: false,
  endtime: '',
  categories: ''
});

onMounted(async () => {
  try {
    const itemId = route.query.id;
    if (!itemId) {
      router.push('/profile');
      return;
    }
    const itemRes = await axios.get(`/api/items/${itemId}`);
    
    const currentCats = itemRes.data.categories || [];
    const catString = currentCats.join(', ');

    let et = '';
    if (itemRes.data.ddl) {
        et = itemRes.data.ddl.slice(0, 16);
    }
      
    Object.assign(form, {
      title: itemRes.data.name,
      description: itemRes.data.description,
      price: (itemRes.data.bid || 0) / 100, 
      condition: itemRes.data.condition,
      status: itemRes.data.status,
      is_auction: itemRes.data.auction === 'auction',
      endtime: et,
      categories: catString
    });
  } catch (err) {
    console.error("Failed to load item data", err);
  }
});

const submitItem = async () => {
  try {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    const payload = { ...form };
    payload.price_cents = Math.round(payload.price * 100);
    payload.categories = payload.categories.split(',').map(c => c.trim()).filter(Boolean);
    delete payload.price;

    if (!payload.is_auction) {
      payload.endtime = null;
    } else if (payload.endtime) {
      payload.endtime = new Date(payload.endtime).toISOString();
    }
    
    const itemId = route.query.id;
    const res = await axios.patch(`/api/items/${itemId}`, payload);
    if (res.data.status === 'updated') {
      router.push('/profile');
    }
  } catch (err) {
    alert("Failed to edit item.");
  }
};
</script>
