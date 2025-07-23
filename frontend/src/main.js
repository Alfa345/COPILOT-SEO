import { createApp } from 'vue';
import App from './App.vue';
import PrimeVue from 'primevue/config';
// [FIX] The Aura theme is no longer needed, as tailwindcss-primeui will handle styling.
// import Aura from '@primevue/themes/aura'; 
import './assets/css/main.css';

const app = createApp(App);

app.use(PrimeVue, {
  unstyled: true,
  // [FIX] Remove the pt: Aura property.
  // pt: Aura 
});

app.mount('#app');