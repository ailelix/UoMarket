<template>
  <div class="flex items-center justify-center min-h-[50vh]">
    <div class="flex flex-col items-center gap-4">
      <div class="w-12 h-12 rounded-full animate-spin border-y-4 border-solid border-uom-purple border-t-transparent shadow-md"></div>
      <p class="text-xl font-bold text-slate-800 tracking-wide animate-pulse">Redirecting to UoM Login...</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';

onMounted(() => {
  // Hard navigation redirect to the backend API endpoint
  window.location.href = '/api/login';
});
</script>
