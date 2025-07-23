<script setup>
import SeoForm from './components/SeoForm.vue';
import ThemeSwitcher from './components/ThemeSwitcher.vue';
</script>

<template>
  <ThemeSwitcher />
  <div class="min-h-screen font-sans bg-gradient-to-tr from-indigo-900 via-blue-800 to-purple-900 dark:from-gray-950 dark:via-gray-900 dark:to-gray-950 flex flex-col">
    <header class="sticky top-0 z-30 w-full backdrop-blur-xl bg-white/40 dark:bg-gray-900/40 border-b border-blue-300 dark:border-gray-800 shadow-2xl">
      <div class="container mx-auto px-6 py-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <h1 class="text-4xl md:text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 dark:from-blue-300 dark:via-purple-300 dark:to-pink-300 drop-shadow-2xl animate-fade-in-slow tracking-tight mb-2">
            Copilote SEO
          </h1>
          <p class="text-lg md:text-xl text-gray-700 dark:text-gray-300 font-medium mb-2 md:mb-0">
            De l'idée à l'article, assisté par l'IA.
          </p>
        </div>
        <div class="flex items-center gap-4">
          <!-- ThemeSwitcher déjà importé -->
        </div>
      </div>
    </header>
    <main class="flex-1 flex items-center justify-center px-2 md:px-0">
      <div class="w-full max-w-2xl mx-auto">
        <div class="bg-white/90 dark:bg-gray-900/90 rounded-3xl shadow-2xl p-10 md:p-14 border border-blue-200 dark:border-gray-800 backdrop-blur-xl glassmorphism animate-fade-in-slow transition-all duration-500">
          <SeoForm />
        </div>
      </div>
    </main>
    <footer class="w-full text-center py-6 text-xs md:text-sm text-gray-400 dark:text-gray-600 tracking-wide">
      © 2025 Copilote SEO. Créé avec <span class="font-semibold text-blue-400 dark:text-blue-300">Vue.js</span>, <span class="font-semibold text-purple-400 dark:text-purple-300">PrimeVue</span>, <span class="font-semibold text-pink-400 dark:text-pink-300">Tailwind</span> & <span class="font-semibold text-gray-700 dark:text-gray-300">Flask</span>.
    </footer>
  </div>
</template>

<style>
@keyframes fade-in-slow {
  from { opacity: 0; transform: translateY(-30px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}
.animate-fade-in-slow {
  animation: fade-in-slow 1.2s cubic-bezier(.4,0,.2,1);
}
.glassmorphism {
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border-radius: 24px;
  border: 1px solid rgba(255,255,255,0.18);
}
</style>