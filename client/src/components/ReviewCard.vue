<template>
    <div className="review-card">
        <div v-if="review.user" className="review-card__user">
            <div className="user__row">
                <div className="user__row-photo">
                    <img :src="review.user.photo"/>
                </div>
                <span className="user__row-name">{{ review.user.name }}</span>
            </div>
            <p className="user__text text">
                {{ review.user.text }}
            </p>
        </div>
        <div v-else className="review-card__other">
            <a>Смотреть все отзывы</a>
        </div>
    </div>
</template>
<script setup>
    const props = defineProps(['review']);
</script>

<!--!Сделать адекватное выравнивание ссылки потом -->
<style lang="scss" scoped>
.review-card {
    width: 325px;
    height: 380px; 
    border-radius: 15px;
    background: var(--color-white);
    box-shadow: 0px 0px 15px 5px rgba(92, 92, 92, 0.14);
    font-family: var(--font-base);
    color: var(--color-middle-text);
    
    &__user {
        padding: 0 30px;
    }
    
    &__other {
        margin-top: 150px;
        display: flex;
        justify-content: center;
        align-content: center;
        font-size: 24px;
        color: var(--color-accent-pink);
        text-decoration: underline;
        a {
            cursor: pointer;
        }
    }
}

.user {
    &__row {
        display: flex;
        align-items: center;
        margin-top: 30px;

        &-photo {
            background: var(--color-accent-pink);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 15px;
        }

        &-name {
            font-size: 24px;
            
        }
    }

    &__text {
        text-align: justify;
        font-size: 16px;
    }
}
</style>