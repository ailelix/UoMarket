<template>
  <div class="bg-white">
    <div class="pt-6">

      <div class="mx-auto mt-6 max-w-2xl sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:gap-8 lg:px-8">
        <template v-for="(src, idx) in images" :key="idx">
          <img :src="src" :alt="`Product image ${idx + 1}`" :class="imageClass(idx)" />
        </template>
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
            <span v-if="price !== null">£{{ formatPounds(price) }}</span>
            <span v-else class="text-gray-300">Base</span>
          </p>

          <div v-if="auction === 'auction' && timeRemaining" class="mt-4 p-4 bg-indigo-50 border border-indigo-100 rounded-xl shadow-sm">
            <span class="text-sm font-semibold text-indigo-800 uppercase tracking-wide">Time Remaining</span>
            <p class="text-2xl font-bold text-indigo-900 mt-1 tabular-nums">{{ timeRemaining }}</p>
          </div>

          <form v-if="currentUserId !== sellerId" @submit.prevent="placeBid" class="mt-10">
            <div class="flex items-center space-x-4">
              <button type="button" @click="changeUserBid(-10)" class="inline-flex items-center justify-center h-12 w-12 rounded-md border border-gray-300 bg-white text-lg font-bold text-gray-700 hover:bg-gray-50">-</button>

              <div class="flex-1">
                <label for="userBid" class="sr-only">Your bid</label>
                <input id="userBid" v-model.number="user_bid" type="number" class="w-full rounded-md border border-gray-300 px-4 py-3 text-lg font-semibold text-gray-900" />
              </div>

              <button type="button" @click="changeUserBid(10)" class="inline-flex items-center justify-center h-12 w-12 rounded-md border border-gray-300 bg-white text-lg font-bold text-gray-700 hover:bg-gray-50">+</button>
            </div>

            <button type="submit" class="mt-6 w-full flex items-center justify-center rounded-md border border-transparent bg-purple-700 px-8 py-4 text-lg font-bold text-white shadow-sm transition-colors hover:bg-purple-800 focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:outline-hidden">
              Place Bid
            </button>
          </form>
          
          <div v-else class="mt-10 p-4 bg-yellow-50 rounded-xl border border-yellow-200">
            <p class="text-yellow-800 text-center font-medium">You cannot bid on your own item.</p>
          </div>
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
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();

const title = ref('');
const description = ref('');
const price = ref<number|null>(null);
const condition = ref('');
const status = ref('');
const categories = ref<string[]>([]);
const image = ref('');
const images = ref<string[]>([]); // list of image URLs for gallery display
const auction = ref('');
const bid = ref<number|null>(null);
const ddl = ref('');
const user_bid = ref<number|null>(null);
const currentUserId = ref<number|null>(null);
const sellerId = ref<number|null>(null);

const timeRemaining = ref('');
let timer: ReturnType<typeof setInterval> | null = null;

const updateCountdown = () => {
  if (!ddl.value) return;
  const now = new Date();
  const end = new Date(ddl.value);
  const diff = end.getTime() - now.getTime();
  if (diff <= 0) {
    timeRemaining.value = 'Auction Ended';
    if (timer) clearInterval(timer);
    return;
  }
  const d = Math.floor(diff / (1000 * 60 * 60 * 24));
  const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const m = Math.floor((diff / 1000 / 60) % 60);
  const s = Math.floor((diff / 1000) % 60);
  
  if (d > 0) timeRemaining.value = `${d}d ${h}h ${m}m ${s}s`;
  else timeRemaining.value = `${h}h ${m}m ${s}s`;
};

async function fetchItemDetails(id: string) {
  const response = await fetch(`/api/items/${id}`);
  if (!response.ok) return;
  const data = await response.json();

  // Update the reactive variables with the fetched data.
  title.value = data.name;
  description.value = data.description;
  // incoming bid is in cents; convert to pounds
  const bidCents = data.bid ?? null;
  if (bidCents !== null) {
    const bidPounds = bidCents / 100;
    price.value = bidPounds;
    bid.value = bidPounds;
    
    // initialize the user's bid to current highest bid + £10
    user_bid.value = bidPounds + 10;
  } else {
    price.value = null;
    bid.value = null;
    user_bid.value = 10;
  }
  condition.value = data.condition;
  status.value = data.status;
  categories.value = data.categories || [];
  image.value = data.image || '';
  auction.value = data.auction || '';
  ddl.value = data.ddl || '';
  sellerId.value = data.seller_id;
  // populate images array (support `images` or single `image`)
  if (Array.isArray(data.images) && data.images.length > 0) {
    images.value = data.images;
  } else if (data.image) {
    images.value = [data.image];
  } else {
    images.value = [];
  }
  
  if (ddl.value && data.auction === 'auction') {
    updateCountdown();
    if (timer) clearInterval(timer);
    timer = setInterval(updateCountdown, 1000);
  }
}

async function placeBid() {
  const currentHighest = bid.value ?? 0;
  const proposed = user_bid.value ?? 0;
  if (proposed <= currentHighest) {
    alert('Your bid must be higher than the current highest bid.');
    return;
  }
  // convert back to cents for submission
  const proposedCents = Math.round(proposed * 100);
  try {
    const response = await fetch('/api/bids', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ itemId: route.query.id, amount: proposedCents }),
    });

    if (!response.ok) {
      const text = await response.text().catch(() => '');
      throw new Error(text || `HTTP ${response.status}`);
    }

    const result = await response.json().catch(() => ({}));
    // update UI to reflect new highest bid
    bid.value = proposed;
    price.value = proposed;
    alert('Your bid was placed successfully.');
    return result;
  } catch (error) {
    console.error('Error placing bid:', error);
    alert('There was an error placing your bid. Please try again.');
  }
}

function changeUserBid(delta: number) {
  const base = user_bid.value ?? (bid.value ?? 0);
  const next = base + delta;
  // enforce minimum of 0
  user_bid.value = Math.max(0, Math.round(next));
}

function formatPounds(value: number | null) {
  if (value === null) return '0.00';
  return value.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function imageClass(idx: number) {
  // mimic previous layout for first four images, fallback for more
  if (idx === 0) return 'row-span-2 aspect-3/4 size-full rounded-lg object-cover max-lg:hidden shadow-sm';
  if (idx === 1) return 'col-start-2 aspect-3/2 size-full rounded-lg object-cover max-lg:hidden shadow-sm';
  if (idx === 2) return 'col-start-2 row-start-2 aspect-3/2 size-full rounded-lg object-cover max-lg:hidden shadow-sm';
  if (idx === 3) return 'row-span-2 aspect-4/5 size-full object-cover sm:rounded-lg lg:aspect-3/4 shadow-sm';
  return 'aspect-square w-full rounded-md bg-gray-200 object-cover group-hover:opacity-75 lg:aspect-auto lg:h-80 shadow-sm';
}
// run on initial load.
onMounted(async () => {
  try {
    const meRes = await axios.get('/api/me');
    currentUserId.value = meRes.data.id;
  } catch (err) {}

  if (route.query.id) {
    fetchItemDetails(route.query.id as string);
  }
});

// When user clicks on a different item.
watch(() => route.query.id, (newId) => {
  if (newId) {
    fetchItemDetails(newId as string);
  }
});

onUnmounted(() => {
  if (timer) clearInterval(timer);
});
</script>