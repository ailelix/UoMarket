<script>
import HeroCard from '@/components/Hero-section.vue';
import PromoCard from '@/components/Promo-section.vue';
import FeatureView from '@/components/Feature-view.vue';
import PromoCard2 from '@/components/Promo-section-flipped.vue';

export default {
  components: {
    HeroCard,
    PromoCard,
    PromoCard2,
    FeatureView
  }
}
</script>
<template>
  <HeroCard />
  <PromoCard />
  <FeatureView/>
  <PromoCard2 />
</template>