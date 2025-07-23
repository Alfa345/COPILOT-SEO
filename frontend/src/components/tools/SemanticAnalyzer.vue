<script setup>
defineProps({ analysis: Object });
</script>
<template>
  <div class="tool-container">
    <h3>Analyse Sémantique</h3>
    <p>Utilisez ces termes pour enrichir votre contenu et couvrir le sujet en profondeur.</p>
    <div class="tags-list">
      <span v-for="kw in analysis.semantic_analysis.keywords_to_include" :key="kw[0]" class="tag">
        {{ kw[0] }}
      </span>
    </div>
  </div>
</template>
<style scoped>
.tool-container { padding: 1rem; }
.tags-list { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }
.tag { background-color: var(--background-tertiary); padding: 0.3rem 0.8rem; border-radius: 16px; }
</style>