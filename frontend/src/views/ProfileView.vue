<template>
	<div class="min-h-screen bg-white px-4 py-12 font-sans text-slate-900">
		<div class="mx-auto flex w-full max-w-2xl items-center justify-center">
			<div
				class="w-full rounded-3xl border border-slate-200 bg-white p-8 shadow-sm sm:p-10"
			>
				<div class="flex flex-col gap-8">
					<div class="flex flex-col items-center gap-6 sm:flex-row sm:items-start">
						<div
							class="flex h-28 w-28 items-center justify-center rounded-full bg-slate-100 text-slate-400"
						>
							<span class="text-xs font-semibold uppercase tracking-wide">Photo</span>
						</div>

						<div class="w-full">
							<div class="flex flex-wrap items-center justify-between gap-3">
								<h1 class="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
									{{ profile.fullName }}
								</h1>
								<span :class="statusBadgeClass">
									{{ statusLabel }}
								</span>
							</div>

							<div class="mt-4 flex items-center gap-2 text-base text-slate-500">
								<svg
									class="h-5 w-5 text-slate-400"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
									stroke-linecap="round"
									stroke-linejoin="round"
									aria-hidden="true"
								>
									<path d="M4 4h16v16H4z" />
									<path d="m22 6-10 7L2 6" />
								</svg>
								<span>{{ profile.email }}</span>
							</div>

							<p class="mt-5 text-sm text-slate-500">
								{{ joinedLabel }}
							</p>
						</div>
					</div>

					<div class="border-t border-slate-200 pt-6">
						<h2 class="text-lg font-semibold text-slate-900">Edit profile</h2>
						<div class="mt-4 grid gap-4 sm:grid-cols-2">
							<label class="flex flex-col gap-2 text-sm text-slate-600">
								<span class="font-medium text-slate-700">Full name</span>
								<input
									v-model="profile.fullName"
									type="text"
									class="h-11 rounded-xl border border-slate-200 px-4 text-base text-slate-900 shadow-sm focus:border-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-200"
									placeholder="Enter full name"
								/>
							</label>

							<label class="flex flex-col gap-2 text-sm text-slate-600">
								<span class="font-medium text-slate-700">Email</span>
								<input
									v-model="profile.email"
									type="email"
									class="h-11 rounded-xl border border-slate-200 px-4 text-base text-slate-900 shadow-sm focus:border-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-200"
									placeholder="name@example.com"
								/>
							</label>

							<label class="flex flex-col gap-2 text-sm text-slate-600 sm:col-span-2">
								<span class="font-medium text-slate-700">Status</span>
								<select
									v-model="profile.status"
									class="h-11 rounded-xl border border-slate-200 bg-white px-4 text-base text-slate-900 shadow-sm focus:border-slate-400 focus:outline-none focus:ring-2 focus:ring-slate-200"
								>
									<option value="active">Active</option>
									<option value="inactive">Inactive</option>
								</select>
							</label>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { computed, reactive } from "vue";

const profile = reactive({
	fullName: "Avery Williams",
	email: "avery.williams@uomarket.com",
	status: "active",
	createdAt: "2023-08-14T00:00:00.000Z",
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
