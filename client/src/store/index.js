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

    const loadStorage = async () => {
        await axios.get(`${url}/7/warehouse`)
        .then ((res) => {
            storage.value = res.data;
        })
    }

    const addToCart = async (id) => {
        try {
            console.log('here')
            axios.post(`${url}/2/changeOrder`, {product_id: Number(id)});
        }
        catch {
            alert('Не удалось составить заказ');
        }
    }

    const getCart = async () => {
        try {
            axios.get(`${url}/2/cart`)
            .then ((res) => {
                cart.value = res.data;
        });
        }
        catch {
            alert('Не удалось составить заказ');
        }
    }

    const addToStorage = async (data) => {
        try {
            axios.post(`${url}/7/warehouse/addProduct`, {data: data})
            .then ((res) => {
                cart.value = res.data;
        });
        }
        catch {
            alert('Не удалось составить заказ');
        }
    }

    return {
        flowers,
        loadData,
        storage,
        loadStorage,
        addToCart,
        getCart
    }
})