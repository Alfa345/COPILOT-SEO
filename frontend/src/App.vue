<script setup>
import SeoForm from './components/SeoForm.vue';
import ThemeSwitcher from './components/ThemeSwitcher.vue';
</script>

<template>
  <ThemeSwitcher />
  <div class="min-h-screen font-sans">
    <div class="container mx-auto px-4 py-8 md:py-16">
      <header class="text-center mb-12">
        <h1 class="text-4xl md:text-6xl font-bold text-gray-900 dark:text-white">
          Copilote SEO
        </h1>
        <p class="mt-4 text-lg text-gray-600 dark:text-gray-400">
          De l'idée à l'article, assisté par l'IA.
        </p>
      </header>
      <main>
        <SeoForm />
      </main>
    </div>
  </div>
</template>

<style>
/* Plus besoin de styles globaux ici, Tailwind s'en occupe ! */
/* Vous pouvez supprimer tout le CSS de ce fichier. */
</style>