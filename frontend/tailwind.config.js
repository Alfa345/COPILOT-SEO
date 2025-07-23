/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/primevue/**/*.{vue,js,ts,jsx,tsx}"
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  // [FIX] Add the tailwindcss-primeui plugin here
  plugins: [
    require('tailwindcss-primeui')
  ],
}