<script setup>
import { computed } from 'vue';

const props = defineProps({
  analysis: Object,
  editorText: String
});

// --- Propriétés calculées pour la checklist dynamique ---
const wordCount = computed(() => {
  if (!props.editorText) return 0;
  return props.editorText.trim().split(/\s+/).length;
});

const targetWordCount = computed(() => Math.round(props.analysis.analysis_summary.word_count_avg));

// Mots-clés sémantiques à inclure
const keywordChecklist = computed(() => {
    if (!props.analysis.analysis_summary.common_keywords) return [];
    
    return props.analysis.analysis_summary.common_keywords.map(kw => {
        const regex = new RegExp(`\\b${kw[0]}\\b`, 'gi');
        const count = (props.editorText.match(regex) || []).length;
        return {
            text: kw[0],
            target: kw[1], // Fréquence chez les concurrents
            used: count > 0,
            count: count
        };
    });
});

// Structure des titres (on extrait les H2 et H3 du plan de l'IA)
const headingChecklist = computed(() => {
    if (!props.analysis.ai_generated_outline) return [];
    
    const headings = [];
    const lines = props.analysis.ai_generated_outline.split('\n');
    
    for (const line of lines) {
        if (line.startsWith('## ') || line.startsWith('### ')) {
            const text = line.replace(/^[#]+\s/, '');
            const regex = new RegExp(text.slice(0, 15), 'i'); // Vérifie si le début du titre est présent
            headings.push({
                text: text,
                level: line.startsWith('## ') ? 'H2' : 'H3',
                used: regex.test(props.editorText)
            });
        }
    }
    return headings;
});


const seoScore = computed(() => {
  let score = 0;
  // 20 points pour le nombre de mots
  score += Math.min(20, (wordCount.value / targetWordCount.value) * 20);
  
  // 40 points pour les mots-clés
  const usedKeywordsCount = keywordChecklist.value.filter(kw => kw.used).length;
  score += Math.min(40, (usedKeywordsCount / keywordChecklist.value.length) * 40);
  
  // 40 points pour les titres
  const usedHeadingsCount = headingChecklist.value.filter(h => h.used).length;
  score += Math.min(40, (usedHeadingsCount / headingChecklist.value.length) * 40);

  return Math.round(score);
});
</script>

<template>
  <div class="brief-container">
    <div class="score-section">
      <h3>Score SEO</h3>
      <div class="score-circle">
        <span class="score-value">{{ seoScore }}</span>
        <span class="score-total">/ 100</span>
      </div>
      <progress class="score-progress" :value="seoScore" max="100"></progress>
    </div>

    <div class="checklist-section">
      <h4><span class="icon">🎯</span> Objectifs</h4>
      <div class="check-item" :class="{ 'is-done': wordCount >= targetWordCount }">
        <span class="check-icon">{{ wordCount >= targetWordCount ? '✅' : '⬜️' }}</span>
        <span class="text">Nombre de mots : {{ wordCount }} / ~{{ targetWordCount }}</span>
      </div>
    </div>
    
    <div class="checklist-section">
      <h4><span class="icon">🔑</span> Mots-clés sémantiques</h4>
      <div class="tags-list">
        <div v-for="kw in keywordChecklist" :key="kw.text" class="tag" :class="{ 'is-used': kw.used }">
          {{ kw.text }} ({{ kw.count }})
        </div>
      </div>
    </div>

    <div class="checklist-section">
      <h4><span class="icon">🏗️</span> Structure de l'article (Plan)</h4>
      <div v-for="h in headingChecklist" :key="h.text" class="check-item" :class="{ 'is-done': h.used }">
        <span class="check-icon">{{ h.used ? '✅' : '⬜️' }}</span>
        <span class="text" :class="`heading-level-${h.level}`">{{ h.text }}</span>
      </div>
    </div>

  </div>
</template>

<style scoped>
.brief-container {
  padding: 1rem;
  background-color: var(--background-secondary);
  border-radius: 8px;
  height: 100%;
  overflow-y: auto;
}

.icon { margin-right: 0.5rem; }

/* --- Score Section --- */
.score-section {
  text-align: center;
  margin-bottom: 1.5rem;
}
.score-circle {
  display: inline-block;
  position: relative;
  margin: 0.5rem 0;
}
.score-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--text-accent);
}
.score-total {
  font-size: 1rem;
  color: var(--text-secondary);
}
.score-progress {
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 8px;
}
.score-progress::-webkit-progress-bar {
  background-color: var(--background-tertiary);
  border-radius: 4px;
}
.score-progress::-webkit-progress-value {
  background-color: var(--text-accent);
  border-radius: 4px;
}

/* --- Checklist Section --- */
.checklist-section {
  margin-bottom: 1.5rem;
}
.checklist-section h4 {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 0.5rem;
  margin-bottom: 0.75rem;
}
.check-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.3rem 0;
  font-size: 0.9rem;
  color: var(--text-secondary);
  transition: all 0.2s ease;
}
.check-item.is-done {
  color: var(--text-primary);
  text-decoration: line-through;
  opacity: 0.7;
}
.check-icon {
  font-size: 1.1rem;
}
.heading-level-H3 {
  padding-left: 1.5rem;
}

/* --- Tags List --- */
.tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tag {
  background-color: var(--background-tertiary);
  color: var(--text-secondary);
  padding: 0.25rem 0.75rem;
  border-radius: 16px;
  font-size: 0.85rem;
  border: 1px solid transparent;
  transition: all 0.2s ease;
}
.tag.is-used {
  background-color: #28a74520; /* Vert transparent */
  color: #28a745;
  border-color: #28a745;
}
</style>