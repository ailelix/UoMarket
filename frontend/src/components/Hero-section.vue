<template>
    <section class="flex w-full items-start justify-center bg-[url('/src/assets/Landing-page-bg.jpg')] bg-cover bg-center bg-no-repeat">
  <div class="m-auto flex max-w-5xl grow flex-col items-center justify-start gap-6 py-20 md:gap-12 lg:max-w-screen-xl px-3 sm:px-8 lg:px-16 xl:px-32">
        <a href="/" class="text-8xl font-extrabold tracking-tight hover:opacity-80 transition">
                <span class="text-uom-purple">UOM</span><span class="text-uom-yellow">ARKET</span>
        </a>
    <div class="flex max-w-2xl flex-1 flex-col items-center gap-6 text-center backdrop-blur-lg bg-white/60 rounded-lg p-12 shadow-lg">
      <h3 class="text-4xl font-semibold text-slate-950 md:text-6xl w-130">Made for students, by students</h3>
      <p class="text-lg font-normal leading-7 text-slate-500">The easiest way to buy, sell, and trade textbooks, tech, and dorm essentials within your campus community.</p>
      <form class="flex gap-2">
        <div class="inline-flex w-full flex-col items-start gap-1.5 stroke-black transition-colors duration-300 ease-in-out focus-within:stroke-blue-700">
          <div class="relative w-full">
            <div class="pointer-events-none absolute left-6 top-1/2 w-5 -translate-x-1/2 -translate-y-1/2">
              <svg width="21" height="20" viewBox="0 0 21 20" fill="none" stroke="#1D4ED8" xmlns="http://www.w3.org/2000/svg" class="stroke-blue-700">
                <g clip-path="url(#clip0_4036_225)">
                  <path d="M13 8.3335L9.66667 11.6668L14.6667 16.6668L18 3.3335L3 9.16683L6.33333 10.8335L8 15.8335L10.5 12.5002" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>
                </g>
                <defs>
                  <clipPath id="clip0_4036_225">
                    <rect width="20" height="20" fill="white" transform="translate(0.5)"></rect>
                  </clipPath>
                </defs>
              </svg>
            </div>
            <input
              class="w-full rounded-lg border border-slate-200 px-3 text-sm font-medium placeholder-slate-400 outline-none transition-all duration-300 ease-in-out disabled:cursor-not-allowed disabled:bg-slate-50 disabled:text-slate-400 disabled:placeholder-slate-400 focus:border-blue-600 py-2.5 pl-10"
              aria-disabled="false" id="email" placeholder="Your E-mail" required=false type="email">
          </div>
        </div>
        <button type="submit" aria-disabled="false"
          class="group inline-flex items-center justify-center whitespace-nowrap rounded-lg py-2 align-middle text-sm font-semibold leading-none transition-all duration-300 ease-in-out disabled:cursor-not-allowed bg-uom-purple stroke-white px-6 text-white hover:bg-uom-purple-light h-[42px] min-w-[42px] gap-2 disabled:bg-slate-100 disabled:stroke-slate-400 disabled:text-slate-400 disabled:hover:bg-slate-100">
          <div>Sign Up</div>
        </button>
      </form>
    </div>
    <div class="flex flex-col gap-4 md:flex-row md:gap-0">
      <div class="flex items-center justify-center -space-x-4">
        <div class="relative box-content flex items-center justify-center overflow-hidden rounded-full size-10 border-white drop-shadow-md border-[3px] bg-white z-20">
          <img src="https://www.tailframes.com/images/avatar.webp" alt="" class="aspect-square">
        </div>
        <div class="relative box-content flex items-center justify-center overflow-hidden rounded-full size-10 border-white drop-shadow-md border-[3px] bg-white z-10">
          <img src="https://www.tailframes.com/images/avatar.webp" alt="" class="aspect-square">
        </div>
        <div class="relative box-content flex items-center justify-center overflow-hidden rounded-full size-10 border-white drop-shadow-md border-[3px] bg-white z-0">
          <img src="https://www.tailframes.com/images/avatar.webp" alt="" class="aspect-square">
        </div>
      </div>
      <div role="separator" class="bg-slate-200 max-h-screen min-h-full border-l m-auto w-8 md:mx-4 md:my-1 md:w-[unset]"></div>
      <div class="flex flex-col items-center justify-center md:items-start">
        <div class="backdrop-blur bg-white/60 rounded-md px-4 py-2 shadow-md flex flex-col items-center gap-1">
          <div class="flex gap-2">
            <div class="flex items-center justify-center gap-0.5">
              <div class="relative">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg" class="fill-amber-300 stroke-amber-300">
                  <path d="M12 3L14.781 8.59516L21 9.4979L16.5 13.8507L17.562 20L12 17.0952L6.438 20L7.5 13.8507L3 9.4979L9.219 8.59516L12 3Z"></path>
                </svg>
              </div>
            </div>
            <p class="text-base font-semibold">4.95/5</p>
          </div>
          <p class="text-sm text-slate-500">Base on over 256+ reviews</p>
        </div>
      </div>
    </div>
  </div>
</section>
</template>