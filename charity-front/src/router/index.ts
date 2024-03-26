import { createRouter, createWebHistory } from 'vue-router'

import App from '@/App.vue'
import ProjetComponent from '@/components/ProjetComponent.vue'
import CategorieComponent from '@/components/CategorieComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/projet',
      name: 'projet',
      component: ProjetComponent
    },
    {
      path: '/categorie',
      name: 'categorie',
      component: CategorieComponent
    },
    
  ]
})

export default router
