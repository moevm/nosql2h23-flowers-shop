import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '../pages/MainPage.vue'
import Catalog from '../pages/Catalog.vue'
import Cart from '../pages/Cart.vue'

const routes = [
    {
        path: '',
        redirect: {name: 'main'}
    },
    {
        path: '/', 
        name: 'main',
        component: MainPage,
    },
    {
		path: '/catalog',
        name: 'catalog',
		component: Catalog,
	},
    {
        path: '/cart',
        name: 'cart',
        component: Cart,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router