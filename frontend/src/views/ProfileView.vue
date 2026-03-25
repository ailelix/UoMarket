<template>
	<div class="min-h-screen bg-white px-4 py-12 font-sans text-slate-900">
		<div class="mx-auto flex w-full max-w-lg items-center justify-center">
			<div class="w-full rounded-3xl border border-slate-200 bg-white p-8 shadow-sm sm:p-10">
				<div class="flex flex-col gap-6 items-center text-center">
					<h1 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
						{{ profile.fullName }}
					</h1>
					<span :class="statusBadgeClass">
						{{ statusLabel }}
					</span>
				</div>
			</div>
		</div>

        <!-- My Items Section -->
        <div class="mx-auto mt-12 w-full max-w-5xl">
            <h2 class="text-2xl font-bold tracking-tight text-slate-900 mb-6">My Items</h2>
            <div v-if="items.length === 0" class="text-center text-slate-500 py-12 bg-slate-50 rounded-3xl border border-slate-200">
                You haven't posted any items yet.
            </div>
            <div v-else class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
                <div v-for="item in items" :key="item.id" class="group relative bg-white border border-slate-200 rounded-2xl overflow-hidden shadow-sm hover:shadow-md transition-all">
                    <img :src="item.image || 'https://tailwindcss.com/plus-assets/img/ecommerce-images/product-page-01-related-product-01.jpg'" :alt="item.name" class="aspect-video w-full object-cover bg-slate-100" />
                    <div class="p-4">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="text-base font-semibold text-slate-900">
                                    <router-link :to="'/item?id=' + item.id" class="hover:text-uom-purple">
                                        {{ item.name }}
                                    </router-link>
                                </h3>
                                <p class="mt-1 text-sm text-slate-500">${{ (item.price_cents || 0) / 100 }}</p>
                            </div>
                        </div>
                        <div class="mt-4 pt-4 border-t border-slate-100">
                            <router-link :to="'/edit-item?id=' + item.id" class="w-full flex justify-center py-2 px-4 border border-slate-300 rounded-xl text-sm font-medium text-slate-700 bg-white hover:bg-slate-50 transition-colors">
                                Edit Item
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
	</div>
</template>

<script setup lang="ts">
import { computed, reactive, onMounted, ref } from "vue";
import axios from "axios";

const profile = reactive({
    id: null as number | null,
	fullName: "Loading...",
	email: "Loading...",
	status: "active",
	createdAt: "2023-08-14T00:00:00.000Z",
});

const items = ref<any[]>([]);

onMounted(async () => {
	try {
		const res = await axios.get('/api/me');
        profile.id = res.data.id;
		profile.fullName = res.data.name || res.data.username;
		profile.email = res.data.email || `${res.data.username}@student.manchester.ac.uk`;
        
        if (profile.id) {
            const itemsRes = await axios.get(`/api/items?seller=${profile.id}`);
            items.value = itemsRes.data;
        }
	} catch (err) {
		console.error("Not logged in");
	}
});

const joinedLabel = computed(() =>
	`Joined ${new Intl.DateTimeFormat("en-US", {
		month: "long",
		year: "numeric",
	}).format(new Date(profile.createdAt))}`
);

const statusLabel = computed(() =>
	profile.status === "active" ? "Active" : "Inactive"
);

const statusBadgeClass = computed(() =>
	profile.status === "active"
		? "inline-flex items-center rounded-full bg-emerald-100 px-3 py-1 text-xs font-semibold text-emerald-700"
		: "inline-flex items-center rounded-full bg-slate-200 px-3 py-1 text-xs font-semibold text-slate-600"
);
</script>
