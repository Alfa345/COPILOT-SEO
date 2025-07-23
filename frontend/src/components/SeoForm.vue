<script setup>
import { ref } from 'vue';
import ArticleEditor from './ArticleEditor.vue';
import AnalysisDashboard from './AnalysisDashboard.vue'; // Placeholder, assuming it was intended to be used here or similar context

// --- Component State ---
const keyword = ref('');
const isLoading = ref(false);
const error = ref(null);
const analysisResult = ref(null);

/**
 * [FIX] Implemented the API call logic.
 * This function sends the keyword to a backend API, handles loading states,
 * and populates the result or an error message.
 */
async function analyzeKeyword() {
  if (!keyword.value.trim()) return;

  isLoading.value = true;
  error.value = null;
  analysisResult.value = null;

  try {
    // NOTE: This is a placeholder URL. Replace with your actual backend endpoint.
    // In src/components/SeoForm.vue
// ...
// [FIX] Change the fetch URL to a relative path
const response = await fetch('/api/analyze', {
  method: 'POST',
  //...

// ...
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ keyword: keyword.value }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    analysisResult.value = data;

  } catch (e) {
    console.error("Analysis failed:", e);
    error.value = e.message;
  } finally {
    isLoading.value = false;
  }
}
</script>

<template>
  <div>
    <template v-if="!analysisResult">
      <form @submit.prevent="analyzeKeyword" class="max-w-2xl mx-auto mb-8">
        <div class="flex items-center gap-2 p-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg shadow-lg focus-within:ring-2 focus-within:ring-blue-500 transition-all">
          <input 
            v-model="keyword" 
            type="text" 
            placeholder="Entrez un sujet d'article..." 
            class="w-full bg-transparent text-lg placeholder-gray-400 dark:placeholder-gray-500 text-gray-900 dark:text-white border-none focus:ring-0"
            :disabled="isLoading"
          />
          <button 
            type="submit" 
            :disabled="isLoading || !keyword" 
            class="px-6 py-2.5 bg-blue-600 text-white font-semibold rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-gray-400 dark:disabled:bg-gray-600 disabled:cursor-not-allowed transition-colors"
          >
            <span v-if="!isLoading">Analyser →</span>
            <span v-else>Analyse...</span>
          </button>
        </div>
      </form>

      <!-- [FIX] Added loading and error display -->
      <div v-if="isLoading" class="flex flex-col items-center justify-center text-center mt-8">
        <ProgressSpinner />
        <p class="mt-4 text-gray-600 dark:text-gray-400">Analyse en cours, veuillez patienter...</p>
      </div>

      <div v-if="error" class="max-w-2xl mx-auto mt-4">
        <Message severity="error" :closable="false">{{ error }}</Message>
      </div>
    </template>
    
    <!-- [FIX] Changed to show ArticleEditor when analysis is complete -->
    <div v-else>
      <ArticleEditor :analysis="analysisResult" />
    </div>
  </div>
</template>