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

        <div>
            <label class="block text-sm font-medium text-slate-700">Item Image</label>
            <input @change="handleFileChange" type="file" accept="image/*" class="mt-1 block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-uom-purple/10 file:text-uom-purple hover:file:bg-uom-purple/20">
            <div v-if="imagePreview" class="mt-4">
              <img :src="imagePreview" class="w-48 h-48 object-cover rounded-xl"/>
            </div>
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

const file = ref(null);
const imagePreview = ref(null);

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

const handleFileChange = (e) => {
  const selectedFile = e.target.files[0];
  if (selectedFile) {
    file.value = selectedFile;
    imagePreview.value = URL.createObjectURL(selectedFile);
  }
};

const submitItem = async () => {
  try {
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';

    const formData = new FormData();
    formData.append('title', form.title);
    formData.append('description', form.description);
    formData.append('price_cents', Math.round(form.price * 100));
    formData.append('condition', form.condition);
    formData.append('is_auction', form.is_auction);
    if (form.is_auction && form.endtime) {
      formData.append('endtime', new Date(form.endtime).toISOString());
    } else {
      formData.append('endtime', '');
    }
    const cats = form.categories.split(',').map(c => c.trim()).filter(Boolean);
    cats.forEach(c => formData.append('categories', c));

    if (file.value) {
      formData.append('image', file.value);
    }
    
    const res = await axios.post('/api/items', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
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
