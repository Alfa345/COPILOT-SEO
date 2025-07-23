<script setup>
import { onMounted } from 'vue';
import { useToast } from "primevue/usetoast";
import Toast from 'primevue/toast'; // [FIX] Import Toast component

const props = defineProps({
  analysis: Object,
});

const toast = useToast();

// Message de notification pour informer l'utilisateur
const showSuccess = () => {
  toast.add({severity:'success', summary: 'Succès', detail:'Analyse terminée', life: 3000});
};

onMounted(() => {
  if (props.analysis) {
    showSuccess();
  }
});
</script>

<template>
  <!-- [FIX] Converted layout from PrimeFlex to Tailwind CSS for consistency -->
  <div class="mt-8">
    <Toast />
    <div class="grid grid-cols-1 md:grid-cols-12 gap-6">
      
      <!-- Colonne de gauche : Résumé et Plan IA -->
      <div class="md:col-span-4 flex flex-col gap-6">
        <Card>
          <template #title>Analyse Synthétique</template>
          <template #content>
            <div class="flex justify-between text-lg mb-4">
              <strong>Objectif de mots :</strong>
              <span>~{{ analysis.analysis_summary.word_count_avg }}</span>
            </div>
            <hr class="my-3">
            <strong>Mots-clés à inclure :</strong>
            <div class="flex flex-wrap gap-2 mt-2">
              <span v-for="kw in analysis.analysis_summary.common_keywords" :key="kw[0]" class="bg-gray-200 dark:bg-gray-700 text-sm px-3 py-1 rounded-full">
                {{ kw[0] }} ({{ kw[1] }})
              </span>
            </div>
          </template>
        </Card>

        <Card>
          <template #title>Questions Fréquentes (P.A.A)</template>
          <template #content>
            <ul class="list-disc list-inside space-y-2">
              <li v-for="(question, index) in analysis.analysis_summary.people_also_ask" :key="index">
                {{ question }}
              </li>
            </ul>
          </template>
        </Card>

        <Card>
          <template #title>Plan Suggéré par l'IA</template>
          <template #content>
            <pre class="text-sm whitespace-pre-wrap break-words bg-gray-100 dark:bg-gray-800 p-4 rounded-md font-mono">{{ analysis.ai_generated_outline }}</pre>
          </template>
        </Card>
      </div>

      <!-- Colonne de droite : Concurrents -->
      <div class="md:col-span-8">
        <Card>
          <template #title>Analyse des Concurrents</template>
          <template #content>
            <Accordion :activeIndex="0">
              <AccordionTab v-for="(competitor, index) in analysis.competitors_detailed" :key="index">
                <template #header>
                  <span>{{ index + 1 }}. {{ competitor.title }} ({{ competitor.word_count }} mots)</span>
                </template>
                <div class="competitor-details">
                  <p><strong>URL :</strong> <a :href="competitor.link" target="_blank" class="text-blue-500 hover:underline">{{ competitor.link }}</a></p>
                  <p><strong>Snippet :</strong> <em>{{ competitor.snippet }}</em></p>
                  <p><strong>Meta Description :</strong> {{ competitor.meta_description || "Non disponible" }}</p>
                  <hr class="my-4">
                  <strong>Structure de l'article :</strong>
                  <ul class="mt-2 space-y-1">
                    <li v-for="heading in competitor.headings" :class="`heading-${heading.tag}`">
                      <strong>{{ heading.tag.toUpperCase() }}:</strong> {{ heading.text }}
                    </li>
                  </ul>
                  <strong class="block mt-4">Balises Alt des Images :</strong>
                  <div v-if="competitor.alt_tags && competitor.alt_tags.length" class="mt-2">
                    <ul class="list-disc list-inside">
                      <li v-for="(tag, idx) in competitor.alt_tags" :key="idx">{{ tag }}</li>
                    </ul>
                  </div>
                  <div v-else>
                    <p>Aucune balise alt trouvée.</p>
                  </div>
                </div>
              </AccordionTab>
            </Accordion>
          </template>
        </Card>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* [FIX] Scoped styles are simplified as Tailwind handles most of it. */
.competitor-details ul {
  list-style-type: none;
  padding-left: 0;
}
.heading-h1 { font-size: 1.2rem; font-weight: bold; margin-top: 1rem; }
.heading-h2 { font-size: 1.1rem; font-weight: bold; margin-left: 1rem; margin-top: 0.5rem;}
.heading-h3 { margin-left: 2rem; }
.heading-h4 { margin-left: 3rem; font-style: italic; }
</style>