<script setup>
// Le moyen moderne de créer un v-model sur un composant
const model = defineModel();
</script>

<template>
  <textarea v-model="model" class="main-editor" placeholder="Commencez à rédiger votre article ici..."></textarea>
</template>

<style scoped>
.main-editor {
  width: 100%;
  height: 100%;
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 1rem;
  font-size: 1rem;
  line-height: 1.6;
  resize: none;
}
</style>