<template>
    <div className="cart">
        <h2 className="section_title">
            Заказ
        </h2>
        <div className="cart__content">
            <CartItem />

            <DeliveryOptions />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import CartItem from '../components/CartItem.vue';
import DeliveryOptions from '../components/DeliveryOptions.vue';

</script>

<style lang="scss" scoped>
.cart {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
    padding: 50px;

    &__content {
        display: flex;
        gap: 50px;
    }
}
</style>