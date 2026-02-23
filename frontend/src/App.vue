<script setup lang="ts">
import type router from './router';


</script>

<template>
    <nav class="bg-white shadow-md border-b border-gray-100 w-full drop-shadow-xl">
    <div class="max-w-8xl mx-auto px-12">
      <div class="flex justify-between items-center h-16, px-4 sm:px-6 lg:px-8 py-4">
        
        <div class="flex-shrink-0 flex items-center">
            <a href="/" class="text-4xl font-extrabold tracking-tight hover:opacity-80 transition">
                        <span class="text-uom-purple">UOM</span><span class="text-uom-yellow">ARKET</span>
                </a>
        </div>

        <div class="flex items-center space-x-6 text-lg font-bold">
          <router-link to="/login" class="basic_button">
            Login
          </router-link>

          <router-link to="/register" class="basic_button">
            Register
          </router-link>
            
        </div>

      </div>
    </div>
  </nav>
    <router-view />


</template>

<style scoped>

</style>
