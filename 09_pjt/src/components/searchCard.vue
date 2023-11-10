<script setup>
import {useRoute, useRouter} from 'vue-router'

const props = defineProps({
    infos: Array,
    keyword: String
})


const router = useRouter()
const goDetail = function(info) {
    router.push(
        {
            name: 'detail',
            params: {
                keyword: props.keyword,
                id: info.id.videoId
            },

        }
    )
}

</script>

<template>
    <div class="card-list">
        <div v-for="info in infos">
            <div class="card">
                <a href="" @click.prevent="goDetail(info)">
                    <img :src="info.snippet.thumbnails.medium.url" class="card-img-top" alt="...">
                </a>
                <div class="card-body">
                    <p>{{ info.snippet.title }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card-list {
    display: flex;
    flex-wrap: wrap;
}

.card {
    margin: 20px 40px;
    width: 20rem;
    height: 18rem;
}
</style>