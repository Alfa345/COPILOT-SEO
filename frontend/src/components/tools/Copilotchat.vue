<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  articleContext: String
});

const userInput = ref('');
const messages = ref([
  { id: 1, sender: 'ai', text: 'Bonjour ! Comment puis-je vous aider à rédiger cet article ?' }
]);
const isLoading = ref(false);

// A simple function to simulate an AI response
const sendMessage = () => {
  if (!userInput.value.trim()) return;

  // Add user message
  messages.value.push({ id: Date.now(), sender: 'user', text: userInput.value });
  const userText = userInput.value;
  userInput.value = '';
  isLoading.value = true;

  // Simulate AI thinking and responding
  setTimeout(() => {
    let aiResponse = "Je ne suis qu'une simulation, mais voici une suggestion basée sur votre demande : ";
    if (userText.toLowerCase().includes('titre')) {
      aiResponse += "Essayez un titre comme 'Le Guide Ultime de [Votre Sujet]' pour attirer l'attention.";
    } else if (userText.toLowerCase().includes('introduction')) {
      aiResponse += "Commencez votre introduction par une question percutante ou une statistique surprenante pour captiver le lecteur.";
    } else {
      aiResponse += "Pensez à utiliser des listes à puces pour rendre l'information plus digeste.";
    }
    
    messages.value.push({ id: Date.now() + 1, sender: 'ai', text: aiResponse });
    isLoading.value = false;
  }, 1500);
};

</script>

<template>
  <div class="flex flex-col h-full tool-container">
    <div class="flex-grow overflow-y-auto pr-2 space-y-4">
      <!-- Chat Messages -->
      <div v-for="message in messages" :key="message.id" :class="['flex', message.sender === 'user' ? 'justify-end' : 'justify-start']">
        <div 
          :class="[
            'max-w-xs lg:max-w-md px-4 py-2 rounded-lg',
            message.sender === 'user' 
              ? 'bg-blue-500 text-white' 
              : 'bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200'
          ]"
        >
          {{ message.text }}
        </div>
      </div>
       <div v-if="isLoading" class="flex justify-start">
          <div class="bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200 px-4 py-2 rounded-lg">
            <span class="animate-pulse">...</span>
          </div>
        </div>
    </div>
    
    <!-- Chat Input -->
    <div class="mt-4 pt-4 border-t border-gray-300 dark:border-gray-700">
      <form @submit.prevent="sendMessage" class="flex items-center gap-2">
        <input
          v-model="userInput"
          type="text"
          placeholder="Posez une question..."
          class="w-full bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md py-2 px-3 focus:ring-2 focus:ring-blue-500 focus:outline-none"
        />
        <button type="submit" class="bg-blue-600 text-white p-2 rounded-md hover:bg-blue-700 disabled:bg-gray-400" :disabled="isLoading">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
            <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
          </svg>
        </button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.tool-container {
  padding: 0; /* Padding is handled by parent now */
}
</style>