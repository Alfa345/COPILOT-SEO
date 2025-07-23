<script setup>
import { ref, defineAsyncComponent } from 'vue';

const props = defineProps({
  analysis: Object,
  articleContext: String
});

// --- GESTION DES ONGLETS ---
const activeTab = ref('Copilot');

// --- ASYNC COMPONENT IMPORTS ---
const CopilotChat = defineAsyncComponent(() => import('./tools/CopilotChat.vue'));
const SemanticAnalyzer = defineAsyncComponent(() => import('./tools/SemanticAnalyzer.vue'));
const CompetitorAnalysis = defineAsyncComponent(() => import('./tools/CompetitorAnalysis.vue'));
const ContentAuditor = defineAsyncComponent(() => import('./tools/ContentAuditor.vue'));

const tabs = {
  'Copilot': CopilotChat,
  'Analyse Sémantique': SemanticAnalyzer,
  'Concurrents': CompetitorAnalysis,
  'Audit Contenu': ContentAuditor
};

const activeComponent = computed(() => tabs[activeTab.value]);
</script>

<template>
  <!-- [FIX] Added a complete template to render the tabs and their content -->
  <div class="flex flex-col h-full">
    <!-- Tab Navigation -->
    <div class="flex border-b border-gray-300 dark:border-gray-700">
      <button
        v-for="(component, tabName) in tabs"
        :key="tabName"
        @click="activeTab = tabName"
        :class="[
          'px-4 py-2 text-sm font-medium focus:outline-none transition-colors',
          activeTab === tabName
            ? 'border-b-2 border-blue-500 text-blue-600 dark:text-blue-400'
            : 'text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-200'
        ]"
      >
        {{ tabName }}
      </button>
    </div>

    <!-- Tab Content -->
    <div class="flex-grow p-4 overflow-y-auto">
      <KeepAlive>
        <component 
          :is="activeComponent" 
          :analysis="analysis" 
          :article-context="articleContext" 
        />
      </KeepAlive>
    </div>
  </div>
</template>