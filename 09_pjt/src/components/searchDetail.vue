<script setup>
import axios from 'axios'
import {ref} from 'vue'
import {useRoute} from 'vue-router'

const route = useRoute()
const id = route.params.id
const url = 'https://www.googleapis.com/youtube/v3/videos'

const title = ref("")
const videourl = ref(`http://www.youtube.com/embed/${id}?enablejsapi=1`)
const description = ref("")
const date = ref("")
axios.get(url, {
    params: {
        part: 'snippet',
        id: id,
        key: 'AIzaSyBfZABZqr0H1gILlNs5rDc9B9eNFxSdH0o'
    }
})
    .then(response => {
        const videoDetails = response.data.items[0].snippet;
        title.value = videoDetails.title;
        description.value = videoDetails.description;
        date.value = videoDetails.publishedAt

    })
    .catch(error => {
    console.error('Error fetching video details:', error);
});

const localSave = (videoId) =>{
    const existingCart = JSON.parse(localStorage.getItem('bookMark')) || []
    
    const isDuplicated = existingCart.length > 0 && existingCart.find((item) => {
        console.log(item)
        return item === videoId
    })
    
    if(!isDuplicated){
        alert('장바구니에 추가합니다')
        existingCart.push(videoId)
    }else{
        alert('이미 있는 상품입니다.')
    }
    localStorage.setItem('bookMark',JSON.stringify(existingCart))
}

</script>

<template>
    <div>
        <h1>{{ title }}</h1>
        <p>업로드 날짜 : {{ date.slice(0,10) }}</p>
        <iframe :src="videourl" type="text/html" width="600" height="400" frameborder="0"></iframe>
        <p>{{ description }}</p>
        <button @click.prevent="localSave(id)" class="btn btn-primary">동영상 저장</button>
    </div>
</template>

<style scoped>

</style>