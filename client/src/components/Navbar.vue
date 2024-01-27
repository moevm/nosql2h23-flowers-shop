<template>
    <div className="navbar">
        <div className="navbar__logo">
            <img src="/logo.svg" alt="logo"/>
        </div>
        <ul className="navbar__links">
            <router-link :to="{ name: 'main' }">
                <li>Главная</li>
            </router-link>

            <router-link :to="{ name: 'catalog' }">
                <li>Каталог</li>
            </router-link>

            <li>Контакты</li>
            <li>О компании</li>
        </ul>

        <div className="navbar__icons">
            <router-link :to="{ name: 'cart' }">
                <img src="/icons/cart.svg"/>
            </router-link>
        
            <span>Войти</span>
        </div>

        <!-- <img class="navbar__menu" src="/icons/menu.svg" @click="onClickMenu()"/>

        <div className="navbar__smallscreen">
            <ul className="navbar__smallscreen-list">
                <li>Главная</li>
                <li>Каталог</li>
                <li>Контакты</li>
                <li>О компании</li>
                <div>
                    <span>Перейти в корзину</span>
                    <span>Войти</span>
                </div>
            </ul>
        </div> -->
    </div>
</template>

<script setup>
import { ref } from 'vue'

let smallscreen = ref(false);

// function onClickMenu() {
//     console.log(smallscreen);
//     smallscreen = !smallscreen;
// }

</script>


<style lang="scss" scoped>

@mixin li_pink {
    cursor: pointer;
    transition: color 0.2s ease-in, border-bottom 0.2s ease-in, transform 0.2s ease-in;
    color: var(--color-dark-text);
    
    &:hover {
        color: var(--color-accent-pink);
        border-bottom: 1px solid var(--color-accent-pink);
        transform: scale(1.1);
    }
}
.navbar {
    background-color: var(--color-navbar);
    font-family: var(--font-base);
    font-size: 20px;
    display: flex;
    color: var(--color-dark-text);
    justify-content: space-between;
    align-items: center;
    padding: 0 3rem;

    &__logo img {
        width: 92px;
        height: auto;
    }

    &__smallscreen {
        position: fixed;
        z-index: 5;
        background: var(--color-navbar);
        height: 100%;
    }

    &__links {
        display: flex;
        li {
            margin: 0 1rem;
            @include li_pink;
        }
    }

    &__icons {
        display: flex;
        align-items: center;
        img {
            margin-right: 1rem;
        }
        span {
            @include li_pink;
        }
    }

    &__menu {
        cursor: pointer;
    }
}

@media screen and (max-width: 750px) {
    .navbar {
        &__links {
            display: none;
        }

        &__icons {
            display: none;
        }
    }
}
</style>