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
  <div class="brief-container animate-fade-in">
    <div class="score-section">
      <h3 class="font-bold text-lg mb-2 flex items-center gap-2">
        <span class="inline-block w-6 h-6 bg-gradient-to-tr from-blue-400 to-purple-400 rounded-full mr-1"></span>
        Score SEO
      </h3>
      <div class="score-circle">
        <span class="score-value">{{ seoScore }}</span>
        <span class="score-total">/ 100</span>
      </div>
      <progress class="score-progress" :value="seoScore" max="100"></progress>
      <div class="score-bar mt-2 w-full h-3 rounded-full bg-gray-200 dark:bg-gray-800 overflow-hidden">
        <div :style="{width: seoScore + '%'}" class="h-full rounded-full bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 transition-all duration-500"></div>
      </div>
    </div>

    <div class="checklist-section">
      <h4 class="font-semibold text-base mb-2 flex items-center gap-2"><span class="icon">🎯</span> Objectifs</h4>
      <div class="check-item" :class="{ 'is-done': wordCount >= targetWordCount }">
        <span class="check-icon">{{ wordCount >= targetWordCount ? '✅' : '⬜️' }}</span>
        <span class="text">Nombre de mots : <span class="font-bold">{{ wordCount }}</span> / <span class="text-blue-500">~{{ targetWordCount }}</span></span>
      </div>
    </div>

    <div class="checklist-section">
      <h4 class="font-semibold text-base mb-2 flex items-center gap-2"><span class="icon">🔑</span> Mots-clés sémantiques</h4>
      <div class="tags-list">
        <div v-for="kw in keywordChecklist" :key="kw.text" class="tag transition-all duration-300" :class="{ 'is-used': kw.used }">
          <span class="inline-block mr-1">{{ kw.used ? '✅' : '⬜️' }}</span>
          <span class="font-semibold">{{ kw.text }}</span>
          <span class="ml-1 text-xs text-gray-500">({{ kw.count }}/{{ kw.target }})</span>
        </div>
      </div>
    </div>

    <div class="checklist-section">
      <h4 class="font-semibold text-base mb-2 flex items-center gap-2"><span class="icon">🏗️</span> Structure de l'article (Plan)</h4>
      <div v-for="h in headingChecklist" :key="h.text" class="check-item transition-all duration-300" :class="{ 'is-done': h.used }">
        <span class="check-icon">{{ h.used ? '✅' : '⬜️' }}</span>
        <span class="text" :class="`heading-level-${h.level}`">{{ h.text }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fade-in 0.8s cubic-bezier(.4,0,.2,1);
}
@keyframes fade-in {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.brief-container {
  padding: 1.5rem;
  background: rgba(255,255,255,0.85);
  border-radius: 18px;
  box-shadow: 0 4px 32px 0 rgba(31, 38, 135, 0.12);
  height: 100%;
  overflow-y: auto;
  transition: box-shadow 0.3s;
}
.icon { margin-right: 0.5rem; }
.score-section {
  text-align: center;
  margin-bottom: 2rem;
}
.score-circle {
  display: inline-block;
  position: relative;
  margin: 0.5rem 0;
}
.score-value {
  font-size: 2.8rem;
  font-weight: 800;
  color: #7c3aed;
  letter-spacing: -2px;
}
.score-total {
  font-size: 1.1rem;
  color: #64748b;
}
.score-bar {
  background: #e0e7ef;
}
.checklist-section {
  margin-bottom: 2rem;
}
.checklist-section h4 {
  border-bottom: 1px solid #e0e7ef;
  padding-bottom: 0.5rem;
  margin-bottom: 0.75rem;
}
.check-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.3rem 0;
  font-size: 1rem;
  color: #64748b;
  transition: all 0.2s ease;
}
.check-item.is-done {
  color: #22c55e;
  text-decoration: line-through;
  opacity: 0.8;
}
.check-icon {
  font-size: 1.2rem;
}
.heading-level-H3 {
  padding-left: 1.5rem;
}
.tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}
.tag {
  background: #f3f4f6;
  color: #64748b;
  padding: 0.3rem 1rem;
  border-radius: 16px;
  font-size: 0.95rem;
  border: 1px solid transparent;
  box-shadow: 0 1px 4px 0 rgba(31, 38, 135, 0.07);
}
.tag.is-used {
  background: #22c55e22;
  color: #22c55e;
  border-color: #22c55e;
  font-weight: 700;
}
</style>