<template>
    <div v-if="storage" className="storage">
        <h2 className="section_title">
            Склад
        </h2>

        <router-link :to="{ name: 'add' }">
            <button className="app_button">
                Добавить на склад
            </button>
        </router-link>

        <div className="storage__items">
            <div v-for="item in storage" :key="item.id">
                <img class="storage__item" :src="item.image" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useFlowersStore } from '../store/index';

const store = useFlowersStore();

const storage = store.storage;

</script>

<style lang="scss" scoped>
.storage {
    padding: 0 8rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;

    &__search {
        width: 600px;
    }

    &__items {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }

    &__item {
        width: 382px;
        height: 230px;
        object-fit: cover;
    }
}
</style>