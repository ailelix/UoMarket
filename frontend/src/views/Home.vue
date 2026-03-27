<script setup lang="ts">
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

import HeroCard from '@/components/Hero-section.vue';
import PromoCard from '@/components/Promo-section.vue';
import FeatureView from '@/components/Feature-view.vue';
import PromoCard2 from '@/components/Promo-section-flipped.vue';

const router = useRouter();

onMounted(async () => {
  try {
    const res = await axios.get('/api/me');
    if (res.data.id) {
      router.push('/marketplace');
    }
  } catch (err) {
    // Not logged in, stay on home
  }
});
</script>

<template>
  <HeroCard />
  <PromoCard />
  <FeatureView/>
  <PromoCard2 />
</template>