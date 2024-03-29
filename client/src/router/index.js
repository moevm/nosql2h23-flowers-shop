import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '../pages/MainPage.vue'
import Catalog from '../pages/Catalog.vue'
import Storage from '../pages/Storage.vue'
import Cart from '../pages/Cart.vue'
import addProductPage from '../pages/addProductPage.vue'
import FlowerCard from '../components/FlowerCard.vue'

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
		path: '/storage',
        name: 'storage',
		component: Storage,
	},
    {
		path: '/add',
        name: 'add',
		component: addProductPage,
	},
    {
		path: '/catalog/:id',
        name: 'flower',
		component: FlowerCard,
        props: true
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