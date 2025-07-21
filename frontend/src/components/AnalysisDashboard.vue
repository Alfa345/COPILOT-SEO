<script setup>
// Ce composant reçoit les résultats via une "prop"
defineProps({
  analysis: Object
});
</script>

<template>
  <div class="p-grid p-fluid dashboard">
    <!-- Colonne de gauche : Résumé et Plan IA -->
    <div class="p-col-12 p-md-4">
      <Card class="summary-card">
        <template #title>Analyse Synthétique</template>
        <template #content>
          <div class="summary-item">
            <strong>Objectif de mots :</strong>
            <span>~{{ analysis.analysis_summary.word_count_avg }} mots</span>
          </div>
          <hr>
          <!-- NOUVELLE SECTION : Mots-clés -->
          <strong>Mots-clés à inclure :</strong>
          <div class="keywords-list">
            <span v-for="kw in analysis.analysis_summary.common_keywords" :key="kw[0]" class="keyword-tag">
              {{ kw[0] }} ({{ kw[1] }})
            </span>
          </div>
        </template>
      </Card>
      
      <!-- NOUVELLE CARTE : Questions -->
      <Card class="questions-card">
        <template #title>Questions Fréquentes (P.A.A)</template>
        <template #content>
            <ul>
                <li v-for="(question, index) in analysis.analysis_summary.people_also_ask" :key="index">
                    {{ question }}
                </li>
            </ul>
        </template>
      </Card>

      <Card class="outline-card">
        <template #title>Plan Suggéré par l'IA</template>
        <template #content>
          <pre class="outline-pre">{{ analysis.ai_generated_outline }}</pre>
        </template>
      </Card>
    </div>

    <!-- Colonne de droite : Concurrents -->
    <div class="p-col-12 p-md-8">
      <Card>
        <template #title>Analyse des Concurrents</template>
        <template #content>
          <Accordion :activeIndex="0">
            <AccordionTab v-for="(competitor, index) in analysis.competitors_detailed" :key="index">
               <template #header>
                <span>{{ index + 1 }}. {{ competitor.title }} ({{ competitor.word_count }} mots)</span>
              </template>
              <div class="competitor-details">
                <p><strong>URL :</strong> <a :href="competitor.link" target="_blank">{{ competitor.link }}</a></p>
                <p><strong>Snippet :</strong> <em>{{ competitor.snippet }}</em></p>
                <hr>
                <strong>Structure de l'article :</strong>
                <ul>
                  <li v-for="heading in competitor.headings" :class="`heading-${heading.tag}`">
                    <strong>{{ heading.tag.toUpperCase() }}:</strong> {{ heading.text }}
                  </li>
                </ul>
                <!-- NOUVEAU: Mots-clés du concurrent -->
                <strong>Mots-clés principaux de cet article :</strong>
                <div class="keywords-list">
                    <span v-for="kw in competitor.word_frequencies" :key="kw[0]" class="keyword-tag-small">
                        {{ kw[0] }}
                    </span>
                </div>
              </div>
            </AccordionTab>
          </Accordion>
        </template>
      </Card>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  margin-top: 2rem;
}
.summary-card, .outline-card, .questions-card {
  margin-bottom: 1rem;
}
.summary-item {
  display: flex;
  justify-content: space-between;
  font-size: 1.1rem;
}
.keywords-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.5rem;
}
.keyword-tag {
    background-color: #e9ecef;
    padding: 0.25rem 0.75rem;
    border-radius: 14px;
    font-size: 0.9rem;
}
.keyword-tag-small {
    background-color: #f8f9fa;
    padding: 0.15rem 0.5rem;
    border-radius: 10px;
    font-size: 0.8rem;
    color: #495057;
}
.outline-pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 6px;
  font-family: monospace;
}
.competitor-details ul {
  list-style-type: none;
  padding-left: 0;
}
.heading-h1 { font-size: 1.2rem; font-weight: bold; margin-top: 1rem; }
.heading-h2 { font-size: 1.1rem; font-weight: bold; margin-left: 1rem; margin-top: 0.5rem;}
.heading-h3 { margin-left: 2rem; }
.heading-h4 { margin-left: 3rem; font-style: italic; }
</style>