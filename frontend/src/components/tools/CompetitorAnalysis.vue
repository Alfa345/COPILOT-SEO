<script setup>
defineProps({ analysis: Object });
</script>
<template>
  <div class="tool-container">
    <h3>Analyse des Concurrents</h3>
    <div class="competitor" v-for="(c, i) in analysis.competitors_detailed" :key="c.link">
      <h4>{{ i + 1 }}. {{ c.title }}</h4>
      <p><strong>URL :</strong> <a :href="c.link" target="_blank">Lien</a> | <strong>Mots :</strong> ~{{ c.word_count }}</p>
      <ul>
        <li v-for="h in c.headings" :class="`heading-level-${h.tag}`">{{ h.text }}</li>
      </ul>
    </div>
  </div>
</template>
<style scoped>
.tool-container { padding: 1rem; }
.competitor { border-bottom: 1px solid var(--border-color); padding-bottom: 1rem; margin-bottom: 1rem; }
ul { list-style: none; padding-left: 0; }
.heading-level-h2 { font-weight: bold; margin-top: 0.5rem; }
.heading-level-h3 { padding-left: 1rem; }
</style>