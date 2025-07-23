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
      <TextEditor v-model="articleContent" />
    </main>

    <aside class="right-pane">
       <!-- [FIX] Pass the 'analysis' prop to the AiCopilot component -->
       <AiCopilot :analysis="analysis" :article-context="articleContent" />
    </aside>
  </div>
</template>

<style scoped>
.editor-layout {
  display: flex;
  gap: 1.5rem;
  width: 100%;
  /* [FIX] The height was set to 80vh, which might be too restrictive.
     A min-height is often more flexible. Let's keep vh for a full-screen feel. */
  height: calc(100vh - 200px); /* Adjust based on header height */
  background-color: var(--background-primary);
  padding: 1rem;
  border-radius: 8px;
}

.left-pane {
  flex: 0 0 25%;
  overflow-y: auto;
  background-color: var(--background-secondary);
  border-radius: 8px;
}

.center-pane {
  flex: 1 1 50%;
}

.right-pane {
  flex: 0 0 25%;
  display: flex;
  flex-direction: column;
  background-color: var(--background-secondary);
  border-radius: 8px;
  overflow: hidden; /* To contain tab content */
}
</style>