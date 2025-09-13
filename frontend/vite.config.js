// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({ command }) => ({
  base: command === 'serve' ? '/' : '/assets/',  // '/' for dev, '/assets/' for build
  plugins: [react(), tailwindcss()],
  build: {
    outDir: 'dist',
    assetsDir: '',
  }
}))
