<template>
  <div class="min-h-screen bg-slate-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-2xl mx-auto bg-white rounded-3xl shadow-sm border border-slate-200 p-8">
      <h2 class="text-2xl font-bold text-slate-900 mb-6">Post a New Item</h2>
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
          <input v-model="form.endtime" type="datetime-local" :min="currentDateTime" :required="form.is_auction" class="mt-1 block w-full rounded-xl border border-slate-300 py-2 px-3 shadow-sm focus:border-uom-purple focus:ring-uom-purple sm:text-sm">
        </div>

        <div class="flex gap-4">
            <button type="button" @click="router.back()" class="w-full flex justify-center py-3 px-4 border border-slate-300 rounded-xl shadow-sm text-sm font-bold text-slate-700 bg-white hover:bg-slate-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-500">
            Cancel
            </button>
            <button type="submit" class="w-full flex justify-center py-3 px-4 border border-transparent rounded-xl shadow-sm text-sm font-bold text-white bg-uom-purple hover:bg-uom-purple/90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-uom-purple">
            Post Item
            </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const router = useRouter();

const currentDateTime = computed(() => {
  const now = new Date();
  now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
  return now.toISOString().slice(0, 16);
});

const form = reactive({
  title: '',
  description: '',
  price: 0,
  condition: 'good',
  is_auction: false,
  endtime: '',
  categories: ''
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
    
    const res = await axios.post('/api/items', payload);
    if (res.data.status === 'success') {
      router.push('/marketplace');
    }
  } catch (err) {
    if (err.response && err.response.status === 401) {
      alert("Failed to post item! You must be logged in.");
    } else {
      alert("Failed to post item.");
    }
  }
};
</script>
