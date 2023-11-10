<script setup>
import searchCard from '@/components/searchCard.vue'

import {ref} from 'vue'
import axios from 'axios'

const inputText = ref("")
const output = ref("")
const inputKeyword = ref("")
const searchInput = function(keyword) {
    inputText.value = keyword
    inputKeyword.value = keyword
    
    axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
            key: 'AIzaSyBfZABZqr0H1gILlNs5rDc9B9eNFxSdH0o',
            part: 'snippet',
            type: 'video',
            q : inputText.value,
            maxResults: 1,
        }
    })
        .then((response) => {
            // console.log(response.data.items)
            output.value = response.data.items
        })
        .catch((error) =>{
            console.log(error)
        })
    inputText.value = ""
}
</script>

<template>
    <div>
        <h1>비디오 검색</h1>
        <form class="input-group mb-3" @submit.prevent="searchInput(inputText)">
            <input type="text" class="form-control" placeholder="검색어를 입력하세요" v-model="inputText">
            <button class="btn btn-success" type="submit" id="button-addon2">찾기</button>
        </form>

        <div>
            <searchCard :infos="output" :keyword="inputKeyword"/>
        </div>
    </div>
</template>

<style scoped>

</style>