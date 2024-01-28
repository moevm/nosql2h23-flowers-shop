<template>
    <div className="deliveryOptions">
        <span className="deliveryOptions__title">
            Доставка
        </span>

        <span className="deliveryOptions__subtitle">
            Адрес доставки
        </span>

        <input 
            class="deliveryOptions__street inputStyled"
            placeholder="Улица и номер дома"
            v-model="streetValue"
        >

        <div class="deliveryOptions__details">
            <input 
                class="deliveryOptions__apartment inputStyled"
                placeholder="Квартира"
                v-model="apartmentValue"
            >

            <input 
                class="deliveryOptions__porch inputStyled"
                placeholder="Подъезд"
                v-model="porchValue"
            >

            <input 
                class="deliveryOptions__floor inputStyled"
                placeholder="Этаж"
                v-model="floorValue"
            >
        </div>

        <textarea
            class="deliveryOptions__comments inputStyled"
            placeholder="Комментарии"
            v-model="commentsValue"
        />

        <button className="app_button">
            Оплатить
        </button>

    </div>
</template>


<script setup>
import { ref } from 'vue';

let streetValue = ref("");
let apartmentValue = ref("");
let porchValue = ref("");
let floorValue = ref("");
let commentsValue = ref("");

</script>

<style lang="scss" scoped>
.deliveryOptions {
    border-radius: 15px;
    background: var(--color-white);
    padding: 50px;

    display: flex;
    flex-direction: column;
    gap: 20px;

    &__title {
        color: var(--color-accent-pink);
        font-size: 27px;
        font-style: normal;
        font-weight: 400;
    }

    &__subtitle {
        font-size: 24px;
    }

    &__street {
        width: 517px;
    }

    &__details {
        display: flex;
        justify-content: space-between;
    }

    &__apartment,
    &__porch,
    &__floor {
        width: 138px;
    }

    &__comments {
        width: 517px;
        height: 100px;
    }
}

</style>