<template>
    <div className="slider">
        <h2  className="slider__title section_title">Лучшие предложения</h2>
    </div>
    <div className="slider__images">
        <swiper :slides-per-view="2" :space-between="25" navigation>
            <SwiperSlide v-for="image in images" :key="image.id">
                <div className="slider__image">
                    <img :src="image.path"/>
                </div>
            </SwiperSlide>
        </swiper>
    </div>
    <div className="slider__button">
        <button className="app_button">Перейти в каталог</button>
    </div>
</template>

<script setup>
import { Navigation, Pagination, Scrollbar, A11y } from 'swiper/modules';

import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';

const images = [
    {   
        id: 1,
        path: "/images/slider1.jpg"
    },
    {
        id: 2,
        path: "/images/slider2.jpg"
    },
    {
        id: 3,
        path: "/images/slider3.jpg"
    },
    {
        id: 4,
        path: "/images/slider4.jpg"
    }
]


</script>

<style lang="scss" scoped>

.slider {
    padding-top: 100px;

    &__image {
        height: 400px;
    }

    &__button {
        padding: 32px 0;
        display: flex;
        justify-content: center;
    }
}
.swiper {
    margin: 0 5rem;
    display: flex;
}
.swiper-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;

}
</style>