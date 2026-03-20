<template>
  <div class="bg-white">
    <div class="pt-6">

      <div class="mx-auto mt-6 max-w-2xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:gap-8 lg:px-8">
        <img src="https://media1.tenor.com/m/LCCrUegzs70AAAAC/dog-getting-fade.gif" alt="Two each of gray, white, and black shirts laying flat." class="row-span-2 aspect-3/4 size-full rounded-lg object-cover max-lg:hidden shadow-sm" />
        <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-02-tertiary-product-shot-01.jpg" alt="Model wearing plain black basic tee." class="col-start-2 aspect-3/2 size-full rounded-lg object-cover max-lg:hidden shadow-sm" />
        <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-02-tertiary-product-shot-02.jpg" alt="Model wearing plain gray basic tee." class="col-start-2 row-start-2 aspect-3/2 size-full rounded-lg object-cover max-lg:hidden shadow-sm" />
        <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-02-featured-product-shot.jpg" alt="Model wearing plain white basic tee." class="row-span-2 aspect-4/5 size-full object-cover sm:rounded-lg lg:aspect-3/4 shadow-sm" />
      </div>

      <div class="mx-auto max-w-2xl px-4 pt-10 pb-16 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto_auto_1fr] lg:gap-x-8 lg:px-8 lg:pt-16 lg:pb-24">
        <div class="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
          <h1 class="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl">
            <span v-if="title">{{ title }}</span>
            <span v-else class="text-gray-400">Loading item...</span>
          </h1>
        </div>

        <div class="mt-4 lg:row-span-3 lg:mt-0">
          <h2 class="sr-only">Product information</h2>
          <h3 class="text-lg font-semibold text-gray-500 uppercase tracking-wide">Highest Bid</h3>
          <p class="text-4xl font-bold tracking-tight text-purple-700 mt-2">
            <span v-if="price">£{{ price }}</span>
            <span v-else class="text-gray-300">--</span>
          </p>

          <div class="mt-6">
            <h3 class="text-sm font-medium text-gray-900">Seller Rating</h3>
            <div class="flex items-center mt-2">
              <div class="flex items-center">
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5 shrink-0 text-yellow-400">
                  <path d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd" fill-rule="evenodd" />
                </svg>
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5 shrink-0 text-yellow-400">
                  <path d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd" fill-rule="evenodd" />
                </svg>
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5 shrink-0 text-yellow-400">
                  <path d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd" fill-rule="evenodd" />
                </svg>
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5 shrink-0 text-yellow-400">
                  <path d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd" fill-rule="evenodd" />
                </svg>
                <svg viewBox="0 0 20 20" fill="currentColor" data-slot="icon" aria-hidden="true" class="size-5 shrink-0 text-gray-200">
                  <path d="M10.868 2.884c-.321-.772-1.415-.772-1.736 0l-1.83 4.401-4.753.381c-.833.067-1.171 1.107-.536 1.651l3.62 3.102-1.106 4.637c-.194.813.691 1.456 1.405 1.02L10 15.591l4.069 2.485c.713.436 1.598-.207 1.404-1.02l-1.106-4.637 3.62-3.102c.635-.544.297-1.584-.536-1.65l-4.752-.382-1.831-4.401Z" clip-rule="evenodd" fill-rule="evenodd" />
                </svg>
              </div>
              <p class="sr-only">4 out of 5 stars</p>
              <a href="#" class="ml-3 text-sm font-medium text-purple-700 hover:text-purple-600 transition-colors">117 reviews</a>
            </div>
          </div>

          <form class="mt-10">
            <button type="submit" class="mt-10 flex w-full items-center justify-center rounded-md border border-transparent bg-purple-700 px-8 py-4 text-lg font-bold text-white shadow-sm transition-colors hover:bg-purple-800 focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:outline-hidden">
              Place Bid
            </button>
          </form>
        </div>

        <div class="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pt-6 lg:pr-8 lg:pb-16">
          <div>
            <h3 class="text-lg font-semibold text-gray-900">Description</h3>
            <div class="space-y-6 mt-4">
              <p class="text-base text-gray-700 leading-relaxed">
                <span v-if="description">{{ description }}</span>
                <span v-else class="text-gray-400 italic">No description provided.</span>
              </p>
            </div>
          </div>

          <div class="mt-10">
            <h3 class="text-lg font-semibold text-gray-900">Condition</h3>
            <div class="mt-4">
              <ul role="list" class="list-disc space-y-2 pl-4 text-sm">
                <li class="text-gray-400">
                  <span class="text-gray-700 text-base capitalize">
                    <span v-if="condition">{{ condition }}</span>
                    <span v-else>Loading...</span>
                  </span>
                </li>
              </ul>
            </div>
          </div>

          <div class="mt-10">
            <h3 class="text-lg font-semibold text-gray-900">Status</h3>
            <div class="mt-4">
              <p class="text-base text-gray-900">
                <span v-if="status" class="inline-flex items-center rounded-md bg-purple-50 px-2 py-1 text-sm font-medium text-purple-700 ring-1 ring-inset ring-purple-700/10 capitalize">{{ status }}</span>
                <span v-else>Loading...</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-gray-50 border-t border-gray-200">
    <div class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900">Similar Products</h2>

      <div class="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        <div class="group relative">
          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg" alt="Front of men&#039;s Basic Tee in black." class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80 shadow-sm" />
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-900">
                <a href="#">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  Basic Tee
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">Black</p>
            </div>
            <p class="text-sm font-medium text-purple-700">£35</p>
          </div>
        </div>
        <div class="group relative">
          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-02.jpg" alt="Front of men&#039;s Basic Tee in white." class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80 shadow-sm" />
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-900">
                <a href="#">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  Basic Tee
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">Aspen White</p>
            </div>
            <p class="text-sm font-medium text-purple-700">£35</p>
          </div>
        </div>
        <div class="group relative">
          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-03.jpg" alt="Front of men&#039;s Basic Tee in dark gray." class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80 shadow-sm" />
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-900">
                <a href="#">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  Basic Tee
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">Charcoal</p>
            </div>
            <p class="text-sm font-medium text-purple-700">£35</p>
          </div>
        </div>
        <div class="group relative">
          <img src="https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-04.jpg" alt="Front of men&#039;s Artwork Tee in peach with white and brown dots forming an isometric cube." class="aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80 shadow-sm" />
          <div class="mt-4 flex justify-between">
            <div>
              <h3 class="text-sm font-medium text-gray-900">
                <a href="#">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  Artwork Tee
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">Iso Dots</p>
            </div>
            <p class="text-sm font-medium text-purple-700">£35</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';

const props = defineProps<{ itemId: string }>();

const title = ref('');
const description = ref('');
const price = ref<number|null>(null);
const condition = ref('');
const status = ref('');
const categories = ref<string[]>([]);
const image = ref('');
const auction = ref('');
const bid = ref<number|null>(null);
const ddl = ref('');

async function fetchItemDetails(id: string) {
  const response = await fetch(`/api/items/${id}`);
  if (!response.ok) return;
  const data = await response.json();

  // Update the reactive variables with the fetched data.
  title.value = data.name;
  description.value = data.description;
  price.value = data.bid ?? null;
  condition.value = data.condition;
  status.value = data.status;
  categories.value = data.categories || [];
  image.value = data.image || '';
  auction.value = data.auction || '';
  bid.value = data.bid ?? null;
  ddl.value = data.ddl || '';
}

// run on initial load.
onMounted(() => {
  fetchItemDetails(props.itemId);
});

// When user clicks on a different item.
watch(() => props.itemId, (newId) => {
  fetchItemDetails(newId);
});
</script>