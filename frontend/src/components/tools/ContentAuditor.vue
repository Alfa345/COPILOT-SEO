<script setup>
import { computed } from 'vue';
const props = defineProps({ analysis: Object, articleContext: String });

// Simulation de la mise à jour des scores
const auditScores = computed(() => ({
  plagiarism: Math.min(5, (props.articleContext.length / 500)).toFixed(1), // Simulé
  ai_score: Math.min(90, (props.articleContext.length / 10)).toFixed(1), // Simulé
  readability: Math.max(0, 80 - (props.articleContext.length / 50)).toFixed(1) // Simulé
}));
</script>
<template>
  <div class="tool-container">
    <h3>Audit du Contenu</h3>
    <p>Scores estimés en temps réel (simulation).</p>
    <div class="audit-grid">
      <div class="audit-metric">
        <div class="value">{{ auditScores.plagiarism }}%</div>
        <div class="label">Plagiat</div>
      </div>
      <div class="audit-metric">
        <div class="value">{{ auditScores.ai_score }}%</div>
        <div class="label">Détection IA</div>
      </div>
       <div class="audit-metric">
        <div class="value">{{ auditScores.readability }}</div>
        <div class="label">Lisibilité (Flesch)</div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.tool-container { padding: 1rem; }
.audit-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; text-align: center; margin-top: 1rem; }
.audit-metric .value { font-size: 2rem; font-weight: bold; color: var(--text-accent); }
.audit-metric .label { font-size: 0.9rem; color: var(--text-secondary); }
</style>