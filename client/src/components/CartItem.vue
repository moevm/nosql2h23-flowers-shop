<template>
    <div className="cartItem">
        <div className="cartItem__header">
            <img :src="flower.image" className="cartItem__image">

            <div className="cartItem__info">
                <h2 class="cartItem__title">
                    {{ flower.name }}
                </h2>

                <div className="cartItem__options">
                    <div className="cartItem__optionsCount">
                        <img src="/icons/minus.svg" />

                        <span>1</span>

                        <img src="/icons/plus.svg" />
                    </div>

                    <span className="cartItem__optionsPrice">
                        {{ flower.price }} ₽
                    </span>
                </div>
            </div>
        </div>

        <div className="divider"></div>

        <div className="cartItem__delivery">
            <span>Доставка</span>   

            <span>Бесплатно</span>
        </div>

        <div className="divider"></div>

        <div className="cartItem__cost">
            <span>Общая стоимость</span>

            <span>2300 ₽</span>
            </div>
    </div>
</template>

<!-- !Добавить пропс с объектом товара и функцию счета цены-->
<script setup>

const flower = {
    image: '/images/slider1.jpg',
    name: 'Букет цветочков',
    price: 2300
}

</script>

<style lang="scss" scoped>
.cartItem {
    border-radius: 15px;
    background: var(--color-white);
    padding: 50px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;

    &__header {
        display: flex;
        gap: 20px;
    }

    &__image {
        width: 270px;
        height: 163px;
        object-fit: cover;
    }

    &__info {
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    &__title {
        font-size: 27px;
        font-style: normal;
        font-weight: 400;
    }

    &__options {
        display: flex;
        justify-content: space-between;

        &Count {
            font-size: 27px;
            color: var(--color-dark-text);
            display: flex;
            align-items: center;
            gap: 5px;
        }

        &Price {
            color: #000;
            font-size: 27px;
            font-style: normal;
            font-weight: 400;
        }
    }

    &__delivery, 
    &__cost {
        font-size: 24px;
        display: flex;
        width: 100%;
        justify-content: space-between;
    }
}
</style>