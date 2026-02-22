<script>
import HeroCard from '@/components/Hero-section.vue';
import PromoCard from '@/components/Promo-section.vue';
import FeatureView from '@/components/Feature-view.vue';

export default {
  components: {
    HeroCard,
    PromoCard,
    FeatureView
  }
}
</script>
<template>
  <HeroCard />
  <PromoCard />
  <FeatureView/>
</template>