<template>
  <div class="text-white container bg-dark">
    <span onclick="history.back()" class="close" title="Close PopUp"></span>
    <div class="d-flex m-3 row">
      
      <div class="p-4 d-flex flex-column mt-3 col-8">
        <div class="d-inline-flex justify-content-between ms-2">
          <h1><strong>{{ movie.title }}</strong></h1>
          <div class="d-flex flex-column justify-content-center me-3">
            <!-- 좋아요기능 -->
            <div v-if="liked">
              <i class="fas fa-heart fa-3x" style="color:crimson; cursor:pointer;" size="lg" @click="likeMovie"></i>
            </div>
            <div v-else>
              <i class="far fa-heart fa-3x" style="color:crimson; cursor:pointer;" size="lg" @click="likeMovie"></i>
            </div>
            
          </div>
        </div>
        <!-- width="640" height="360" -->
        <iframe id="player" type="text/html" :src="youtubeVideoSrc" frameborder="0" class="mt-4 w-100 h-100"></iframe>
      </div>
      <div class="p-4 mt-5 col-4">
        <h4>비슷한 영화 추천</h4>
        <div class="mt-4 ms-2">
          <SimilarMovie
          v-for= "(video, idx) in similarVideo"
          :key="idx"
          :video="video"
          @click="toDetail(video)"
          />
        </div>
        <div class="mt-5">
          <!-- <h4>영화 정보</h4> -->
          <div class="d-flex">
            <i class="fas fa-heart fa-lg" style="color:crimson; cursor:pointer;"></i>
            <div class="ms-2">{{ likedCount }}명이 이 영화를 좋아합니다.</div>

            <div class="ms-5">
              <i class="fas fa-plus text-success ms-5" style="cursor:pointer" @click="addMovieModal"></i>
            </div>
            <!-- add playlist modal start -->
            <div id="addMovieModal" class="modal">
              <form class="modal-content animate">
                <div class="imgcontainer">
                  <span onclick="document.getElementById('addMovieModal').style.display='none'" class="close" title="Close PopUp">&times;</span>
                </div>
                <div class="container text-dark">
                  <p class="text-dark">선택한 playlist : {{ selectedPlaylist.list_name }}</p>
                  <hr class="text-dark">
                  <div class="w-100 px-4">
                    <div v-for="(playlist, idx) in playlists" :key="idx" class="text-dark d-flex justify-content-between">
                      {{ playlist.list_name }} 
                      <button @click="clickPlaylist(playlist)" type="button">선택</button>
                    </div>
                  </div>
                  <button class="project_submit" type="button"  @click="addMovie">추가</button>
                  <button class="project_cancel" style="" type="button" onclick="document.getElementById('addMovieModal').style.display='none'">취소</button>
                </div>
              </form>
            </div>
            <!-- add playlist modal end -->
          </div>
          
          <div class="d-flex justify-content-between mt-4" >
            <p style="color:white;">발매일 {{ movie.release_date }}</p>
            <p style="color:white;">평점 {{ movie.vote_average }}</p>
          </div>
          <div>
            <p class="textlength" style="color:white;">{{ movie.overview }}</p>
          </div>
          <div class="d-flex ms-2">
            <div v-for="(genre,idx) in genreList" :key="idx" class="me-4">
              #{{ genre.name }}
            </div>
          </div>
          
        </div>
      </div>
      <!-- 몇명이 좋아합니다 넣기 -->
    </div>
    <div>
      <div>
        <div class="d-flex mx-4">
          <div class="star-rating space-x-4">
            <input type="radio" id="5-stars" name="rating" value="5" v-model="score"/>
            <label for="5-stars" class="star pr-4">★</label>
            <input type="radio" id="4-stars" name="rating" value="4" v-model="score"/>
            <label for="4-stars" class="star">★</label>
            <input type="radio" id="3-stars" name="rating" value="3" v-model="score"/>
            <label for="3-stars" class="star">★</label>
            <input type="radio" id="2-stars" name="rating" value="2" v-model="score"/>
            <label for="2-stars" class="star">★</label>
            <input type="radio" id="1-star" name="rating" value="1" v-model="score" />
            <label for="1-star" class="star">★</label>
          </div>
          <div class="input-group tm-mb-30 mx-4">
            <input name="username" type="text" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="리뷰를 남겨주세요" v-model="content" @keyup.enter="createReview" autofocus>
          </div>
          <button class="btn btn-light" style="width:8%;" @click="createReview">
            확인
          </button>
        </div>
        <!-- 아래 코드 추가함 -->
        <div class="table-responsive mt-5">
          <b-table 
          id="my-table"
          :items="reviewList"
          :fields="['score', 'content', 'username', 'updated_at', 'etc']"
          :per-page="perPage"
          :current-page="currentPage"
          class="table table-striped custom-table"
          small
          >
            <!-- <template #cell(content)="content">
              {{ content.item.content }}
            </template> -->
            <template #cell(etc)="row">
              <div v-if="row.item.username === user.username">
                <b-button size="sm" class="mr-2 me-3" @click="row.toggleDetails">
                  수정
                </b-button>
                <div @click="deleteReview(row.item)" class="d-inline">
                  <b-button size="sm" class="mr-2 btn-danger">
                    삭제
                  </b-button>
                </div>
              </div>
            </template>
            <template #row-details="row">
              <b-card class="text-start" style="background-color:transparent">
                <input type="integer" :value="row.item.score" style="width:15%;">
                <input type="text" :value="row.item.content" style="width:85%;">
                <button @click="updateReview(row), row.toggleDetails" class="btn-secondary mx-2">확인</button>
                <button @click="row.toggleDetails" class="btn-warning">취소</button>
              </b-card>
            </template>            
          </b-table>
          <b-pagination
            v-model="currentPage"
            :total-rows="rows"
            :per-page="perPage"
            aria-controls="my-table"
            align="center"
            pills
            first-number
            last-number
            class="my-5 d-flex"
          >
          </b-pagination>
        </div>

      </div>
    </div>
  </div>
</template>


<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
import axios from 'axios'
import { mapState } from 'vuex'
import SimilarMovie from '@/components/movies/SimilarMovie.vue'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'MovieDetail',
  data: function () {
    return {
      movieData: {},
      movieVideo: '',
      similarVideo: [],
      reviewList: [],
      content: '',
      score: '',
      perPage: 10,
      currentPage: 1,
      genreList: [],
      // 좋아요 땜에 일단 추가
      liked: '',
      likeusers: '',
      likedCount: '',
      playlists: [],
      selectedPlaylist: {},
      
    }
  },
  components: {
    SimilarMovie,
  },
  // created: function () {
    /* 배경을 영화 backdrop_path로 바꾸기 진행중 */
    // const video = document.querySelector('#bg-video')
    // video.setAttribute('style', 'display:none;')
    // const body = document.querySelector('body')
    // const bg = document.createElement('div')
    // body.append(bg)
    // bg.setAttribute('url', this.movie.backdrop_path)
  // },
  // 추가함
  mounted: async function () {

    // detail 영화 정보 불러오기
    const videoId = this.movie.id
    const apiKey = '7a8df8004890b70d9d4175ce5a47331d'
    const VIDEO_URL = `https://api.themoviedb.org/3/movie/${videoId}/videos?api_key=${apiKey}&language=ko` 

    axios.get(VIDEO_URL)
    .then(response => {
      // console.log(response)
      this.movieVideo = response.data.results[0].key
    })

    // similar 영화 정보 불러오기
    const SIMILAR_URL = `https://api.themoviedb.org/3/movie/${videoId}/similar?api_key=${apiKey}&language=ko&page=1`
    axios.get(SIMILAR_URL)
    .then(response=> {
      let i = 0
      while (this.similarVideo.length < 3) {
        if (response.data.results[i].poster_path) {
          this.similarVideo.push(response.data.results[i])
        }
        i ++
      }
    })

    
    this.getReviews()
    this.like()
    this.getGenres()
    // this.likeMovie()
    
  },
  created: function() {
    this.movieData = this.movie
  },
  computed: {
    youtubeVideoSrc: function () {
      return `http://www.youtube.com/embed/${this.movieVideo}?enablejsapi=1&origin=http://example.com`
    },
    ...mapState ([
      'user',
      'movie',
      'genres',
    ]),
    rows() {
      return this.reviewList.length
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReviews: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        data: {},
        headers: this.setToken()
      })
      .then((res)=> {
        this.reviewList = res.data
        this.content = ''
        this.score = ''
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getGenres: function () {
      this.genreList = this.genres.filter((genre) => {
        return this.movie.genres.includes(genre.id)
      })
    },
    // 영화의 리뷰 생성 기능
    createReview: function() {
      const reviewScore = {
        content : this.content,
        score : this.score,
        user: this.user.id,
        movie: this.movie.id,
        username: this.user.username,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/`,
        data: reviewScore,
        headers: this.setToken()
      })
        .then((res)=> {
          // console.log(res)
          this.getReviews()
          return res
        })
        .catch(err => {
          console.log(err)
        })
    },
    // similar movie의 detail 이동 기능
    toDetail : function (video) {
      this.$store.dispatch('getMovie', video)
      this.$router.go(this.$router.currentPage)
    },
    // 영화 좋아요 기능
    like: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/like/`,
        headers: this.setToken()
      })
      .then((res)=> {
        console.log(res.data)
        this.likedCount = res.data.count
        this.likeUsers = res.data.movie.like_users
        console.log(this.likeUsers)
        this.liked = this.likeUsers.find((users) => {
          return users === this.user.id
        })
        if (this.liked === undefined) {
          this.liked = false
        }
      })
      .catch((error) =>{
        console.log(error)
      })
    },
    likeMovie: function () {
      const likeuserInfo = {
        user: this.user.id,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/movie_like/`,
        data: likeuserInfo,
        headers: this.setToken()
      })
      .then((res)=> {
        console.log(this.liked)
        this.liked = res.data.liked
        console.log(this.liked)
        this.like()
      })
      .catch((error) =>{
        console.log(error)
      })
    },
    // 리뷰 수정
    updateReview: function (review) {
      const reviewHTML = document.querySelector(`#my-table__details_${review.index}_`)
      const score = reviewHTML.firstChild.firstChild.childNodes[2].childNodes[2].value
      const content = reviewHTML.firstChild.firstChild.childNodes[2].childNodes[3].value
      const reviewInfo = {
				score: score,
        content: content,
				username: review.item.username,
			}
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/${review.item.id}/`,
        data: reviewInfo,
        headers: this.setToken(),
      })
        .then(res => {
          this.reviewList[review.index].score = score
          this.reviewList[review.index].content = content
          return res
        })
        .catch(err => {
          console.log(err)
        })
    },
    // 리뷰삭제
    deleteReview: function (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${this.movie.id}/review/${review.id}/`,
        data: {},
        headers: this.setToken(),
      })
        .then(res => {
          // const newReviews = this.reviewList.filter(x => {
          //   return x != review
          // })
          this.getReviews()
          return res
        })
        .catch(err => {
          console.log(err)
        })
    },
    getPlaylists: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.user.username}/playlist/`,
        data: {},
        headers: this.setToken()
      })
      .then(res => {
        this.playlists = res.data
        return res
      })
      .catch(err => {
        console.log(err)
      })
    },
    addMovieModal: function () {
      const modal = document.querySelector('#addMovieModal')
      modal.setAttribute('style', 'display:block;')
      this.getPlaylists()
    },
    clickPlaylist: function (playlist) {
      this.selectedPlaylist = playlist
    },
    addMovie:function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.user.username}/${this.selectedPlaylist.id}/${this.movie.id}/`,
        data: {},
        headers: this.setToken()
      })
    },



  },
}
</script>

<style scoped>
  #back {
    opacity: 0.5;
  }
  
  .star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 2.25rem;
  line-height: 2.5rem;
  justify-content: space-around;
  padding: 0 0.2em;
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color:rgb(170, 169, 169);
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}

.form-control {
    font-size: 1.2rem;
    padding: 5px 0;
}

.form-control,
.form-control:focus {
    color: white;
    background-color: transparent;
}

.form-control:focus {
    border-bottom: 1px solid dark;
    outline: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
}

.form-control::-webkit-input-placeholder { color: white; }
.form-control:-moz-placeholder { color: white; }
.form-control::-moz-placeholder { color: white; }
.form-control:-ms-input-placeholder { color: white; }

.textlength {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}
.close {
    position: static;
    right: 25px;
    top: 0;
    color: white;
    font-size: 35px;
    font-weight: bold;
}
.close:hover,.close:focus {
    color: red;
    cursor: pointer;
}

.modal {
	display:none;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}
.avatar {
    width: 175px;
	height:175px;
    border-radius: 50%;
    margin: 0;
}
/* Modal Content Box */
.modal-content {
  background-color: #fefefe;
  margin: 1% auto 1% auto;
  border: 1px solid #888;
  width: 30%;
  padding-bottom: 20px;
}

.animate {
    animation: zoom 0.6s
}

.imgcontainer {
  text-align: center;
  margin: 12px 0 6px 0;
  position: relative;
}

input[type=text], .project_description, input[type=url] {
  width: 85%;
  padding: 12px 20px;
  margin: 5px 26px;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
  font-size:16px;
}
.project_description{
  max-width: 85%;
}
.project_submit {
  background-color: #16d840;
  color: white;
  padding: 14px 20px;
  margin: 5px 26px;
  border: none;
  cursor: pointer;
  width: 85%;
  font-size:20px;
}
.project_submit:hover {
    opacity: 0.8;
}
.project_cancel {
  background-color: #070630;
  color: white;
  padding: 14px 20px;
  margin: 5px 26px;
  border: none;
  cursor: pointer;
  width: 85%;
  font-size:20px;
}
.project_cancel:hover {
    opacity: 0.8;
}

</style>