/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
    "./node_modules/primevue/**/*.{vue,js,ts,jsx,tsx}" // Important for PrimeVue components
  ],
  darkMode: 'class', // Enables dark mode based on class, typically on the <html> or <body> tag
  theme: {
    extend: {
      // You can add custom theme extensions here if needed
      // For example:
      // colors: {
      //   'primary': '#007bff',
      // },
    },
  },
  plugins: [
    // PrimeVue components are included via the content array. No plugin needed here for basic setup.
  ],
}