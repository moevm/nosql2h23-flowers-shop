import { ref, watch } from 'vue';
import { defineStore } from "pinia";
import axios from 'axios';

export const useFlowersStore = defineStore('FlowersStore', () => {
    const url = '';
    const flowers = ref([
        {
            id: 1,
            name: 'букет цветочков',
            price: 2300,
            image: '/images/slider1.jpg',
            shelf_life: '',
            description: 'Описание букета цветочков',
            amount: 1,
        },
        {
            id: 2,
            name: 'букет цветочков',
            price: 2300,
            image: '/images/slider1.jpg',
            shelf_life: '',
            description: 'Описание букета цветочков',
            amount: 1,
        },
        {
            id: 3,
            name: 'букет цветочков',
            price: 2300,
            image: '/images/slider1.jpg',
            shelf_life: '',
            description: 'Описание букета цветочков',
            amount: 1,
        },
        {
            id: 4,
            name: 'букет цветочков',
            price: 2300,
            image: '/images/slider1.jpg',
            shelf_life: '',
            description: 'Описание букета цветочков',
            amount: 1,
        }
    ]);

    const flower = ref({});

    const cart = ref([]);

    const loadData = async () => {
        flowers.value = await axios.get(`${url}/catalog`).data;
    }

    const getFlower = async (id) => {
        flower.value = await axios.get(`${url}/catalog/${id}`, id).data;
    }

    // ! указать параметры
    const addToCart = async () => {
        try {
            axios.post(`${url}/orders`);
        }
        catch {
            alert('Не удалось составить заказ')ж
        }
    }


    return {
        flowers,
        loadData,
        getFlower,
        addToCart,
    }
})