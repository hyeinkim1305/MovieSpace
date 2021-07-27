<template>
  <div class="text-white mx-3">
    <h1>Popular Movies</h1>
    <carousel-3d 
    :controls-visible="true" 
    :controls-prev-html="'&#10092;'" 
    :controls-next-html="'&#10093;'" 
    :controls-width="50"
    :controls-height="90"
    :width="360"
    :height="540"
    :display="11"
    :clickable="false"
    :draggable="true"
    :loop="false"
    :border="0"
    :animationSpeed="300"
    style="background:transparent;">
      <slide v-for="(movie, idx) in movies" :key="idx" :index="idx">
        <figure style="height:100%; cursor:pointer;" @click="getMovie(movie)">
          <img :src="getImage(movie.poster_path)" style="height:100%;">
        </figure>
      </slide>
    </carousel-3d>
    
    <!-- 나중에 밑에 Genre를 쭉 뿌려주고 각각의 Component에 carousel을 넣어주면 될 것 같다. -->
    <!-- 뿌려주면서 장르를 넘겨주고 받아서 뿌려주면 된다. -->
    <h1 style="margin-top:120px; margin-bottom:30px;">Best Movies</h1>
    <carousel-3d 
    :controls-visible="true" 
    :controls-prev-html="'&#10092;'" 
    :controls-next-html="'&#10093;'" 
    :controls-width="50"
    :controls-height="90"
    :width="360"
    :height="540"
    :display="11"
    :clickable="false"
    :draggable="true"
    :loop="false"
    :border="0"
    :animationSpeed="300"
    style="background:transparent;">
      <slide v-for="(movie, idx) in bestMovies" :key="idx" :index="idx">
        <figure style="height:100%; cursor:pointer;" @click="getMovie(movie)">
          <img :src="getImage(movie.poster_path)" style="height:100%;">
        </figure>
      </slide>
    </carousel-3d>
  </div>
</template>


<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
import { mapState } from 'vuex'
import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'Home',
  components: {
    Carousel3d,
    Slide
  },
  data: function () {
    return {
      bestmovies: [],
    }
  },
  computed: {
    ...mapState ([
      'movies',
      'bestMovies',
    ]),
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getImage: function (url) {
      return 'https://image.tmdb.org/t/p/original'+ url
    },
    getMovie: function (movie) {
      this.$store.dispatch('getMovie', movie)
      this.$router.push({name: 'MovieDetail'})
    },
    // bestMovie: function () {
    //   axios({
    //     method: 'get',
    //     url: 'http://127.0.0.1:8000/movies/best/',
    //     data: {},
    //     headers: this.setToken()
    //   })
    //   .then((res)=>{
    //     // console.log(res.data)
    //     this.bestmovies = res.data
    //     // console.log(this.bestmovies)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // }
    
  }
}
</script>

<style scoped>
  .carousel-3d-slide {
    font-size: 22px; 
  }
</style>