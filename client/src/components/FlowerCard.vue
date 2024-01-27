<template>
    <div className="flowerCard">
        <img 
            :src="flower.image"
            className="flowerCard_image"
        >

        <div className="flowerCard__info">
            <h2 class="flowerCard__title">
                {{ flower.name }}
            </h2>

            <p class="flowerCard__desc">
                {{ flower.description }}
            </p>

            <div className="flowerCard__options">
                <div className="flowerCard__optionsCount">
                    <img src="/icons/minus.svg"/>

                    1

                    <img src="/icons/plus.svg"/>
                </div>

                <span className="flowerCard__optionsPrice">
                    {{ flower.price }} ₽
                </span>
            </div>

            <button className="app_button">
                Добавить в корзину
            </button>
        </div>
    </div>
</template>

<!-- !Добавить пропс с объектом товара -->
<script setup>

const flower = {
    image: '/images/slider1.jpg',
    name: 'Букет цветочков',
    price: 2300
}

</script>

<style lang="scss" scoped>
.flowerCard {
    border-radius: 15px;
    background: var(--color-white);
    padding: 50px;

    display: flex;
    align-items: center;
    justify-content: center;

    &__image {
        width: 686px;
        height: 414px;
        object-fit: cover;
    }

    &__info {
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    &__title {
        color: var(--color-accent-pink);
        font-size: 27px;
        font-style: normal;
        font-weight: 400;
    }

    &__options {
        display: flex;
        justify-content: space-between;

        &Price {
            color: #000;
            font-size: 27px;
            font-style: normal;
            font-weight: 400;
        }
    }
}
</style>