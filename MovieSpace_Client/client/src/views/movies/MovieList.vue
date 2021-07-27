<template>
  <div class="text-white">
    <div class="mt-5">
      <h1 class="m-4">랜덤 추천</h1>
      <RandomMovie
      :pickmovies="this.pickmovies"
      />
    </div>
    <div class="m-5">
      <h1 class="m-4">좋아하는 장르별 추천</h1>
      <MovieListItem
      v-for="(likegenre, idx) in likegenres"
      :key="idx"
      :likegenre="likegenre"
      :genrename="myGenres[idx]"
      />
    </div>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import RandomMovie from '@/components/movies/RandomMovie.vue'
import MovieListItem from '@/components/movies/MovieListItem.vue'
import { mapState } from 'vuex'
import _ from 'lodash'

export default {
  name: 'MovieList',
  components: {
    RandomMovie,
    MovieListItem,
  },
  data: function() {
    return {
      pickmovies: [],
      likegenres: '',
      myGenres: [],
      checkGenres: [],
    }
  },
  created: function() {
    this.pickMovie()
    this.likeGenre()
    this.getGenres()
  },
  computed: {
    ...mapState ([
      'movies',
      'user',
      'genres',
    ])
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    // 랜덤 영화 뽑기
    pickMovie: function () {
      this.pickmovies = _.sampleSize(this.movies, 10)
    },
    // 좋아하는 장르 기반 뽑기
    likeGenre: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.user.username}/recommend/`,
        data: {},
        headers: this.setToken()
      })
      .then((res)=>{
        // console.log(res.data)
        // console.log(res.data)
        this.likegenres = res.data['data']
        // console.log(this.likegenres)
        // console.log(this.user.like_genres)
      })
    },
    // 사용자가 좋아하는 장르 이름 가져오기
    getGenres: function () {
      // console.log(this.genres)
      // console.log(this.user.like_genres.length)
      // if (this.user.like_genres.lenth) {
      //   this.genreList = this.genres.filter((genre) => {
      //   return this.user.like_genres.includes(genre.id)
      // })
      // } else {


      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.user.username}/like_genre/`,
        data: {},
        headers: this.setToken(),
      })
        .then(res => {
          this.checkGenres = res.data.like_genres
          // this.myGenres = this.checkGenres.join(', ')
          // const myGenres = this.checkGenres
          let Ge = []
          for(let i=0; i<this.genres.length; i++){
            if (this.checkGenres.includes(this.genres[i]['id'])) {
              Ge.push(this.genres[i]['name'])
            }
          }
          this.myGenres = Ge
          console.log(this.myGenres)
        })
        
      // console.log(this.genreList)
      // [ { "id": 12, "name": "모험" }, { "id": 16, "name": "애니메이션" } ]
    },
  }
}
</script>

<style>

</style>