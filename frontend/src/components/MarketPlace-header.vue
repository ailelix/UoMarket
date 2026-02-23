<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const categories = [
  { name: 'Textbooks', href: '/listings?category=textbooks' },
  { name: 'Electronics', href: '/listings?category=electronics' },
  { name: 'Home & Kitchen', href: '/listings?category=home' },
  { name: 'Tickets', href: '/listings?category=tickets' },
  { name: 'Other', href: '/listings?category=other' },
];

const searchQuery = ref('');
const isCategoriesOpen = ref(false);
const dropdownRef = ref(null);

const handleSearch = () => {
  console.log("Searching for:", searchQuery.value);
};

// Close dropdown if user clicks outside of it
const handleClickOutside = (event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    isCategoriesOpen.value = false;
  }
};

onMounted(() => document.addEventListener('click', handleClickOutside));
onUnmounted(() => document.removeEventListener('click', handleClickOutside));
</script>

<template>
  <nav class="sticky top-0 bg-white/90 backdrop-blur-md shadow-sm border-b border-gray-200 w-full z-50 transition-all duration-300">
    <div class="max-w-8xl mx-auto px-4 sm:px-6 lg:px-12">
      <div class="flex justify-between items-center h-16 py-4 gap-6">
        
        <div class="flex-shrink-0 flex items-center w-full max-w-lg relative group">
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search for textbooks, tech, tickets..." 
            class="w-full bg-gray-50/80 border border-gray-300 rounded-xl py-2 pl-11 pr-4 text-base text-gray-900 placeholder-gray-500 transition-all duration-300 outline-none focus:bg-white focus:border-uom-purple focus:ring-4 focus:ring-uom-purple/20 focus:shadow-md"
            @keyup.enter="handleSearch"
          />
          <svg class="absolute left-3.5 top-2.5 h-5 w-5 text-gray-400 transition-colors duration-300 group-focus-within:text-uom-purple" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>

        <div class="flex items-center space-x-6 text-base font-bold">
          
          <div class="relative" ref="dropdownRef">
            <button 
              @click="isCategoriesOpen = !isCategoriesOpen"
              class="flex items-center gap-x-1.5 text-gray-700 hover:text-uom-purple transition-colors duration-200 focus:outline-none"
            >
              Categories
              <svg 
                viewBox="0 0 20 20" 
                fill="currentColor" 
                class="h-5 w-5 text-gray-400 transition-transform duration-300 ease-in-out" 
                :class="{ 'rotate-180 text-uom-purple': isCategoriesOpen }"
              >
                <path fill-rule="evenodd" d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z" clip-rule="evenodd" />
              </svg>
            </button>

            <transition
              enter-active-class="transition ease-out duration-200"
              enter-from-class="opacity-0 translate-y-2 scale-95"
              enter-to-class="opacity-100 translate-y-0 scale-100"
              leave-active-class="transition ease-in duration-150"
              leave-from-class="opacity-100 translate-y-0 scale-100"
              leave-to-class="opacity-0 translate-y-2 scale-95"
            >
              <div 
                v-show="isCategoriesOpen"
                class="absolute left-0 top-full mt-3 w-56 origin-top-left rounded-xl bg-white shadow-xl ring-1 ring-black/5 focus:outline-none overflow-hidden"
              >
                <div class="py-2">
                  <a 
                    v-for="item in categories" 
                    :key="item.name" 
                    :href="item.href" 
                    class="block px-5 py-2.5 text-sm font-semibold text-gray-700 hover:bg-uom-purple/5 hover:text-uom-purple transition-colors"
                  >
                    {{ item.name }}
                  </a>
                </div>
              </div>
            </transition>
          </div>

          <router-link 
            to="/listings/create" 
            class="basic_button bg-white text-gray-800 border border-gray-200 px-5 py-2 rounded-xl hover:bg-gray-50 hover:text-uom-purple hover:border-uom-purple/50 hover:shadow-md active:scale-95 transition-all duration-200"
          >
            Post an Item
          </router-link>
            
        </div>
      </div>
    </div>
  </nav>
</template>