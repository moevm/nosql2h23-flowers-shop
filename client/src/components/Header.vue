<template>
    <div className="header">
        <h1>
            Цветы, которые говорят <br />без слов
        </h1>
    </div>
</template>

<style lang="scss" scoped>
.header {
    background: var(--gradient-header);
    font-family: var(--font-base);
    height: 500px;
    display: flex;
    justify-content: center;
    align-items: center;
    
    h1 {
        color: var(--color-white);
        text-align: center;
        font-size: 48px;
    }
}
</style>