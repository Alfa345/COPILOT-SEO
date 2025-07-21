<script setup>
import { ref } from 'vue';
import SeoBrief from './SeoBrief.vue';
import TextEditor from './TextEditor.vue';
import AiCopilot from './AiCopilot.vue';

const props = defineProps({
  analysis: {
    type: Object,
    required: true
  }
});

// Le contenu de l'article, qui sera partagé entre les composants
const articleContent = ref('');

</script>

<template>
  <div class="editor-layout">
    <aside class="left-pane">
      <SeoBrief :analysis="analysis" :editor-text="articleContent" />
    </aside>
    
    <main class="center-pane">
      <!-- v-model lie le contenu de l'éditeur à notre variable articleContent -->
      <TextEditor v-model="articleContent" />
    </main>

    <aside class="right-pane">
       <AiCopilot :article-context="articleContent" />
    </aside>
  </div>
</template>

/* frontend/src/components/ArticleEditor.vue */
<style scoped>
.editor-layout {
  display: flex;
  gap: 1.5rem;
  width: 100%;
  height: 80vh;
  background-color: var(--background-secondary); /* <-- Utiliser la variable */
  padding: 1rem;
  border-radius: 8px;
}


.left-pane {
  flex: 0 0 25%; /* 25% de la largeur, ne grandit pas, ne rétrécit pas */
  overflow-y: auto;
}

.center-pane {
  flex: 1 1 50%; /* 50% de la largeur, grandit et rétrécit */
}

.right-pane {
  flex: 0 0 25%; /* 25% de la largeur */
  display: flex;
  flex-direction: column;
}
</style>