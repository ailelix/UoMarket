<template>
  <section class="relative bg-slate-50 py-16 sm:py-24 lg:py-32 overflow-hidden border-t border-slate-200">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-12 items-center">
        
        <div class="order-2 lg:order-1 w-full">
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 sm:gap-4 auto-rows-[150px] sm:auto-rows-[200px]">
            
            <div class="col-span-2 row-span-2 overflow-hidden rounded-2xl shadow-sm transition-transform duration-500 hover:shadow-xl group">
              <img src="https://images.pexels.com/photos/1181298/pexels-photo-1181298.jpeg" alt="Students studying" class="size-full object-cover transition-transform duration-700 group-hover:scale-105" />
            </div>
            
            <div class="col-span-1 row-span-1 overflow-hidden rounded-2xl shadow-sm transition-transform duration-500 hover:shadow-xl group">
              <img src="https://images.pexels.com/photos/267394/pexels-photo-267394.jpeg" alt="Tech gadgets" class="size-full object-cover transition-transform duration-700 group-hover:scale-105" />
            </div>
            
            <div class="col-span-1 row-span-1 overflow-hidden rounded-2xl shadow-sm transition-transform duration-500 hover:shadow-xl group">
              <img src="https://images.pexels.com/photos/459653/pexels-photo-459653.jpeg" alt="Study materials" class="size-full object-cover transition-transform duration-700 group-hover:scale-105" />
            </div>
            
            <div class="col-span-2 sm:col-span-1 row-span-1 overflow-hidden rounded-2xl shadow-sm transition-transform duration-500 hover:shadow-xl group">
              <img src="https://images.pexels.com/photos/1251837/pexels-photo-1251837.jpeg" alt="Desk setup" class="size-full object-cover transition-transform duration-700 group-hover:scale-105" />
            </div>

            <div class="col-span-2 sm:col-span-2 row-span-1 overflow-hidden rounded-2xl shadow-sm transition-transform duration-500 hover:shadow-xl group">
              <img src="https://images.pexels.com/photos/2857477/pexels-photo-2857477.jpeg" alt="Campus life" class="size-full object-cover transition-transform duration-700 group-hover:scale-105" />
            </div>

          </div>
        </div>

        <div class="order-1 lg:order-2 flex flex-col justify-center lg:pl-10">
          
          <div class="inline-flex items-center gap-2 rounded-full bg-uom-purple/10 px-4 py-1.5 text-sm font-semibold text-uom-purple mb-6 w-fit">
            <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            Sustainable Campus
          </div>

          <h2 class="text-4xl font-extrabold tracking-tight text-slate-900 sm:text-5xl lg:text-6xl">
            Student-to-student <br />
            <span class="text-uom-purple">essentials.</span>
          </h2>
          
          <p class="mt-6 text-lg text-slate-600 leading-relaxed max-w-xl">
            The sustainable way to score tech and academic gear. Buy, sell, and auction with fellow students on campus and give your items a second life while saving money.
          </p>

          <div class="mt-10 flex flex-wrap gap-4">
            <router-link 
              to="/listings?category=tech" 
              class="inline-flex h-12 items-center justify-center rounded-xl bg-uom-purple px-8 text-base font-bold text-white transition-all duration-300 hover:bg-opacity-90 hover:shadow-lg hover:shadow-uom-purple/30 active:scale-95"
            >
              Browse Tech
            </router-link>
            
            <router-link 
              to="/listings?category=books" 
              class="inline-flex h-12 items-center justify-center rounded-xl bg-white border border-slate-300 px-8 text-base font-bold text-slate-700 transition-all duration-300 hover:bg-slate-50 hover:text-uom-purple hover:border-uom-purple active:scale-95 shadow-sm"
            >
              Find Textbooks
            </router-link>
          </div>

        </div>
      </div>
      
    </div>
  </section>
</template>