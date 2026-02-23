<template>
  <section class="relative flex w-full items-start justify-center bg-[url('/src/assets/Landing-page-bg.jpg')] bg-cover bg-center bg-no-repeat overflow-hidden">
    
    <div class="absolute inset-0 bg-white/30 z-0"></div>

    <div class="relative z-10 m-auto flex max-w-5xl grow flex-col items-center justify-start gap-8 py-20 md:gap-14 lg:max-w-screen-xl px-4 sm:px-8 lg:px-16 xl:px-32">
      
      <a href="/" class="text-6xl md:text-8xl font-extrabold tracking-tight transition-all duration-300 hover:scale-105 drop-shadow-sm hover:drop-shadow-md">
        <span class="text-uom-purple">UOM</span><span class="text-uom-yellow">ARKET</span>
      </a>

      <div class="flex max-w-2xl w-full flex-col items-center gap-6 text-center backdrop-blur-xl bg-white/80 border border-white/60 rounded-2xl p-8 md:p-12 shadow-xl transition-all duration-500 hover:-translate-y-1 hover:border-uom-purple/30 hover:shadow-2xl hover:shadow-uom-purple/10">
        
        <h1 class="text-4xl font-extrabold tracking-tight text-slate-900 md:text-6xl">
          Made for students, <br/> by students
        </h1>
        
        <p class="text-lg font-medium leading-relaxed text-slate-600 max-w-lg">
          The easiest way to buy, sell, and trade textbooks, tech, and dorm essentials within your campus community.
        </p>
        
        <form class="flex w-full max-w-md gap-3 mt-4 flex-col sm:flex-row" @submit.prevent="handleSignup">
          <div class="relative flex-grow group">
            <div class="pointer-events-none absolute left-4 top-1/2 w-5 -translate-y-1/2 text-slate-400 group-focus-within:text-uom-purple transition-colors duration-300">
              <svg width="20" height="20" viewBox="0 0 21 20" fill="none" stroke="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path d="M13 8.3335L9.66667 11.6668L14.6667 16.6668L18 3.3335L3 9.16683L6.33333 10.8335L8 15.8335L10.5 12.5002" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
              </svg>
            </div>
            
            <input
              id="email"
              type="email"
              placeholder="Your university email"
              required
              class="w-full rounded-xl bg-white border border-slate-300 py-3 pl-11 pr-4 text-sm text-slate-900 placeholder-slate-400 outline-none transition-all duration-300 focus:border-uom-purple focus:ring-2 focus:ring-purple-200 disabled:opacity-50 shadow-sm"
            />
          </div>
          
          <button 
            type="submit" 
            class="inline-flex h-12 items-center justify-center whitespace-nowrap rounded-xl bg-uom-purple px-8 text-sm font-bold text-white transition-all duration-300 hover:bg-opacity-90 hover:shadow-lg hover:shadow-uom-purple/30 active:scale-95 disabled:opacity-50"
          >
            Sign Up
          </button>
        </form>
      </div>

      <div class="flex flex-col items-center gap-6 md:flex-row md:gap-8 mt-4">
        
        <div class="flex items-center justify-center -space-x-4">
          <div v-for="i in 3" :key="i" class="relative box-content flex size-12 items-center justify-center overflow-hidden rounded-full border-[3px] border-white bg-white shadow-md z-[inherit] transition-transform duration-300 hover:-translate-y-1 hover:z-30">
            <img src="https://www.tailframes.com/images/avatar.webp" alt="Student avatar" class="h-full w-full object-cover">
          </div>
        </div>
        
        <div role="separator" class="h-px w-16 bg-slate-300 md:h-12 md:w-px"></div>
        
        <div class="backdrop-blur-md bg-white/80 border border-white/60 rounded-xl px-5 py-3 shadow-md flex flex-col items-center md:items-start gap-1 transition-transform duration-300 hover:scale-105 hover:shadow-lg">
          <div class="flex items-center gap-2">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" class="text-uom-yellow drop-shadow-sm">
              <path d="M12 3L14.781 8.59516L21 9.4979L16.5 13.8507L17.562 20L12 17.0952L6.438 20L7.5 13.8507L3 9.4979L9.219 8.59516L12 3Z"></path>
            </svg>
            <p class="text-lg font-bold text-slate-900">4.9/5</p>
          </div>
          <p class="text-xs font-medium text-slate-500">Based on 250+ student reviews</p>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
// Example handler for the form
const handleSignup = () => {
  console.log("Signup submitted!");
};
</script>