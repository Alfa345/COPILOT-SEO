<script setup>
import { ref, onMounted } from 'vue';

// On utilise 'dark' ou 'light' pour représenter le thème
const currentTheme = ref(localStorage.getItem('theme') || 'light');

const toggleTheme = () => {
  const newTheme = currentTheme.value === 'light' ? 'dark' : 'light';
  currentTheme.value = newTheme;
  localStorage.setItem('theme', newTheme);
  
  // Applique la classe au document HTML
  if (newTheme === 'dark') {
    document.documentElement.classList.add('dark-theme');
  } else {
    document.documentElement.classList.remove('dark-theme');
  }
};

// Applique le thème au chargement initial de la page
onMounted(() => {
  if (currentTheme.value === 'dark') {
    document.documentElement.classList.add('dark-theme');
  }
});
</script>

<template>
  <button @click="toggleTheme" class="theme-switcher">
    <!-- Affiche une icône lune ou soleil selon le thème -->
    <span v-if="currentTheme === 'light'">🌙</span>
    <span v-else>☀️</span>
  </button>
</template>

<style scoped>
.theme-switcher {
  background: none;
  border: 1px solid var(--border-color);
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.2rem;
  position: fixed; /* On le met en position fixe pour un accès facile */
  top: 1rem;
  right: 1rem;
  z-index: 1000;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}
.theme-switcher:hover {
    background-color: var(--background-tertiary);
}
</style>