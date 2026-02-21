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
