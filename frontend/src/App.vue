<script setup>
import SeoForm from './components/SeoForm.vue';
import ThemeSwitcher from './components/ThemeSwitcher.vue'; // <-- Importer le composant
</script>

<template>
  <ThemeSwitcher /> <!-- <-- Ajouter le bouton ici -->
  <div id="app-container">
    <header>
      <h1>Copilote SEO</h1>
      <p>De l'idée à l'article, assisté par l'IA.</p>
    </header>
    <main>
      <SeoForm />
    </main>
  </div>
</template>

<style>
/* --- NOUVEAU : GESTION DES THÈMES --- */

/* Thème par défaut (Clair) */
:root {
  --background-primary: #ffffff;
  --background-secondary: #f8f9fa;
  --background-tertiary: #e9ecef;
  
  --text-primary: #212529;
  --text-secondary: #555;
  --text-accent: #007bff;
  
  --border-color: #ccc;
  
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color-scheme: light;
}

/* Thème Sombre (quand la classe .dark-theme est appliquée) */
html.dark-theme {
  --background-primary: #121212;
  --background-secondary: #1e1e1e;
  --background-tertiary: #2a2a2a;
  
  --text-primary: #e0e0e0;
  --text-secondary: #a0a0a0;
  --text-accent: #3b9bff;

  --border-color: #444;

  color-scheme: dark;
}

/* --- Styles globaux utilisant les variables --- */
body {
  margin: 0;
  background-color: var(--background-primary);
  color: var(--text-primary);
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* etc... Le reste du CSS que nous avons défini à l'étape 1 va ici */
#app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
}

header p {
  font-size: 1.2rem;
  color: var(--text-secondary);
}

input[type="text"], textarea {
  background-color: var(--background-primary);
  color: var(--text-primary);
  border: 1px solid var(--border-color);
  border-radius: 4px;
}

button {
  background-color: var(--text-accent);
  color: var(--background-primary);
  border: none;
  cursor: pointer;
}
</style>