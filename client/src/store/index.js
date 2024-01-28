import { ref, watch } from 'vue';
import { defineStore } from "pinia";
import axios from 'axios';

export const useFlowersStore = defineStore('FlowersStore', () => {
    const url = 'http://127.0.0.1:5050';

    const flowers = ref();
    const storage = ref();

    const cart = ref([]);

    const loadData = async () => {
        await axios.get(`${url}/catalog`)
        .then ((res) => {
            flowers.value = res.data;
        })
    }

    const loadSorage = async () => {
        await axios.get(`${url}/1/warehouse`)
        .then ((res) => {
            storage.value = res.data;
        })
    }

    // ! указать параметры
    const addToCart = async () => {
        try {
            axios.post(`${url}/orders`);
        }
        catch {
            alert('Не удалось составить заказ');
        }
    }


    return {
        flowers,
        loadData,
        getFlower,
        addToCart,
    }
})