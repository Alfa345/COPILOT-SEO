<script setup>
import { ref } from 'vue';
// ON IMPORTE LE NOUVEL ÉDITEUR
import ArticleEditor from './ArticleEditor.vue';

const keyword = ref('');
const isLoading = ref(false);
const analysisResult = ref(null);
const errorMessage = ref('');

const analyzeKeyword = async () => {
  if (!keyword.value) return;
  isLoading.value = true;
  errorMessage.value = '';
  analysisResult.value = null;
  try {
    const response = await fetch('http://127.0.0.1:5000/api/analyze-serp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ keyword: keyword.value }),
    });
    if (!response.ok) {
      const errData = await response.json();
      throw new Error(errData.error || `Erreur HTTP: ${response.status}`);
    }
    const data = await response.json();
    analysisResult.value = data;
  } catch (error) {
    console.error("Erreur lors de l'appel API:", error);
    errorMessage.value = error.message || 'Une erreur est survenue. Vérifiez que le serveur Python est bien lancé.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="seo-form-container">
    <!-- Si on n'a pas encore de résultat, on affiche le formulaire -->
    <template v-if="!analysisResult">
      <form @submit.prevent="analyzeKeyword">
        <input v-model="keyword" type="text" placeholder="Entrez un sujet..." />
        <button type="submit" :disabled="isLoading">Analyser →</button>
      </form>

      <div v-if="isLoading" class="p-d-flex p-jc-center p-mt-4">
        <ProgressSpinner />
      </div>
      <Message v-if="errorMessage" severity="error">{{ errorMessage }}</Message>
    </template>

    <!-- Sinon, on affiche notre nouvel éditeur d'article ! -->
    <div v-else>
      <ArticleEditor :analysis="analysisResult" />
    </div>
  </div>
</template>

<style scoped>
  /* Styles inchangés */
</style>