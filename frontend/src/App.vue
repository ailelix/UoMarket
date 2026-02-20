<script setup lang="ts">
import type router from './router';


</script>

<template>
    <nav class="bg-white shadow-md border-b border-gray-100 w-full">
    <div class="max-w-7xl mx-auto " >
      <div class="flex justify-between items-center h-16">
        
        <div class="flex-shrink-0 flex items-center">
            <a href="/" class="text-2xl font-extrabold tracking-tight hover:opacity-80 transition">
                        <span class="text-uom-purple">UOM</span><span class="text-uom-yellow">MARKET</span>
                </a>
        </div>

        <div class="flex items-center space-x-6">
          <a href="/about" class="text-gray-600 hover:text-blue-600 font-medium transition">
            About Us
          </a>

          <a href="/login" class="text-gray-600 hover:text-blue-600 font-medium transition">
            Log in
          </a>

          <a href="/signup" class="bg-uom-purple hover:bg-purple-600 text-white px-5 py-2 rounded-lg font-medium shadow-sm transition transform hover:-translate-y-0.5">
            Sign up
          </a>
        </div>

      </div>
    </div>
  </nav>
    <router-view />
</template>

<style scoped>

</style>
