import { ref, watch } from 'vue';
import { defineStore } from "pinia";
import axios from 'axios';

export const useFlowersStore = defineStore('FlowersStore', () => {
    const url = 'http://127.0.0.1:5050';

    const flowers = ref();
    const storage = ref();

    const cart = ref();

    const loadData = async () => {
        await axios.get(`${url}/catalog`)
        .then ((res) => {
            flowers.value = res.data;
        })
    }

    const loadStorage = async () => {
        await axios.get(`${url}/7/storage`)
        .then ((res) => {
            storage.value = res.data;
        })
    }

    const addToCart = async (id) => {
        try {
            axios.post(`${url}/2/changeOrder`, {product_id: Number(id)});
        }
        catch {
            alert('Не удалось составить заказ');
        }

        getCart();
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
            axios.post(`${url}/7/storage/addProduct`, {data: data})
        }
        catch {
            alert('Не удалось составить заказ');
        }

        loadData();
        loadStorage();
    }

    const buyProduct = async (data) => {
        try {
            axios.post(`${url}/2/cart/update`, {data: data});
        }
        catch {
            alert('Не удалось составить заказ');
        }

        await getCart();
    }

    return {
        flowers,
        loadData,
        storage,
        cart,
        loadStorage,
        addToCart,
        getCart,
        addToStorage,
        buyProduct
    }
})