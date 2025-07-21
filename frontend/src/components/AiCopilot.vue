<script setup>
import { ref } from 'vue';

const props = defineProps({
  articleContext: String
});

// --- NOUVEAU : Gestion du modèle ---
const availableModels = ref([
  { id: 'gemini-1.5-pro', name: 'Google Gemini 1.5 Pro' },
  { id: 'gemini-1.5-flash', name: 'Google Gemini 1.5 Flash' },
  // On pourra ajouter d'autres modèles ici plus tard
  // { id: 'openai-gpt4o', name: 'OpenAI GPT-4o' },
  // { id: 'anthropic-claude3-opus', name: 'Anthropic Claude 3 Opus' }
]);
const selectedModel = ref(availableModels.value[0].id); // On sélectionne le premier par défaut

const messages = ref([
  { from: 'ai', text: 'Bonjour ! Comment puis-je vous aider à rédiger cet article ?' }
]);
const userInput = ref('');
const isLoading = ref(false);

const sendMessage = async () => {
  if (!userInput.value) return;

  const userMessage = userInput.value;
  messages.value.push({ from: 'user', text: userMessage });
  userInput.value = '';
  isLoading.value = true;

  try {
    const response = await fetch('http://127.0.0.1:5000/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 
          message: userMessage,
          context: props.articleContext,
          model: selectedModel.value // <-- ON ENVOIE LE MODÈLE CHOISI !
      }),
    });
    const data = await response.json();
    messages.value.push({ from: 'ai', text: data.reply });
  } catch (error) {
    messages.value.push({ from: 'ai', text: "Désolé, une erreur est survenue." });
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="copilot-container">
    <!-- NOUVEAU : Sélecteur de modèle -->
    <div class="model-selector-bar">
      <select v-model="selectedModel">
        <option v-for="model in availableModels" :key="model.id" :value="model.id">
          {{ model.name }}
        </option>
      </select>
    </div>

    <div class="messages-window">
      <!-- Le contenu des messages reste identique -->
      <div v-for="(msg, index) in messages" :key="index" class="message" :class="`from-${msg.from}`">
        {{ msg.text }}
      </div>
       <div v-if="isLoading" class="message from-ai is-loading">...</div>
    </div>
    <form @submit.prevent="sendMessage" class="input-area">
      <!-- La zone de saisie reste identique -->
      <input v-model="userInput" type="text" placeholder="Demandez quelque chose..." :disabled="isLoading" />
      <button type="submit" :disabled="isLoading">→</button>
    </form>
  </div>
</template>

<style scoped>
/* Le style existant reste le même... */

<style scoped>
/* --- NOUVEAUX STYLES --- */
.model-selector-bar {
  padding: 0.5rem;
  border-bottom: 1px solid #ccc;
  background-color: #f8f9fa;
}

.model-selector-bar select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: white;
}
/* ... le reste du style est identique */
.copilot-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  border: 1px solid #ccc;
  border-radius: 6px;
  background: white;
}
.messages-window {
  flex-grow: 1;
  padding: 1rem;
  overflow-y: auto;
}
.message {
  padding: 0.5rem 1rem;
  border-radius: 12px;
  margin-bottom: 0.5rem;
  max-width: 85%;
}
.from-ai {
  background-color: #e9ecef;
  align-self: flex-start;
}
.from-user {
  background-color: #007bff;
  color: white;
  align-self: flex-end;
  margin-left: auto;
}
.is-loading {
  font-style: italic;
}
.input-area {
  display: flex;
  border-top: 1px solid #ccc;
}
.input-area input {
  flex-grow: 1;
  border: none;
  padding: 1rem;
  outline: none;
}
.input-area button {
  border: none;
  background-color: #007bff;
  color: white;
  padding: 0 1.5rem;
  cursor: pointer;
}
</style>
