import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite'
import { PrimeVueResolver } from 'unplugin-vue-components/resolvers'

export default defineConfig({
  plugins: [
    vue(),
    Components({
      resolvers: [
        PrimeVueResolver()
      ]
    })
  ],
  // [FIX] Add the server proxy configuration
  server: {
    proxy: {
      // Requests to /api will be proxied to your backend
      '/api': {
        target: 'http://127.0.0.1:5000', // Your backend server
        changeOrigin: true, // Needed for virtual hosted sites
        // Pas de rewrite: le backend attend /api/analyze
      },
    },
  },
})