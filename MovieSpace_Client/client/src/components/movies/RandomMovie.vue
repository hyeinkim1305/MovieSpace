<template>
  <div class="text-white">
    <carousel-3d
    :disable3d="true" 
    :space="310"
    :clickable="false" 
    :draggable="true"
    :controls-visible="true" 
    :display="5"
    :border="0"
    :height="450"
    :width="300"
    style="background-color:transparent;"
    >
      <slide v-for="(movie, i) in pickmovies" :key="i" :index="i" style="background:transparent;">
        <!-- <router-link :to="{name: 'MovieDetail', params: { movie: movie }}"> -->
        <div class="d-inline" @click="getMovie(movie)" style="cursor:pointer">
          <img :src="getImage(movie.poster_path)" style="width:100%; height:85%;">
        
          <div class="title" style="background-color:transparent; font-size:18px;">{{ movie.title }}</div>
        </div>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
export default {
  name: 'RandomMovie',
  components: {
    Carousel3d,
    Slide
  },
  props: {
    pickmovies: {
      type: Array,
    }
  },
  methods: {
    getImage: function (url) {
      return 'https://image.tmdb.org/t/p/original'+ url
    },
    getMovie: function (movie) {
      this.$store.dispatch('getMovie', movie)
      this.$router.push({name: 'MovieDetail'})
    },
    
  }
}
</script>

<style scoped>
  .carousel-3d-slide {
    font-size: 22px; 
  }
  /* a.next[data-v-05517ad0] {
    color: white;
  }
  a.prev[data-v-05517ad0] {
    color: white;
  } */
</style>