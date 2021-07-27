<template>
<!-- CSS only -->
  <div id="app">
    <!-- style을 줘서 해결을 하긴 했는데 글씨가 잘 안 보이는 문제가 있다. -->
    <video autoplay muted loop id="bg-video">
      <source src="@/assets/v1.mp4" type="video/mp4">
    </video>
    <!-- 'bg-transparent'가 배경 투명하게 하는 것 -->
    <div id="nav" class="navbar navbar-expand-lg navbar-light bg-transparent" v-if="logined()">
      <div class="container-fluid">
        <router-link to="/" class="nav-link">
          <a class="navbar-brand" style="font-size:30px;" href="#" id="nav1">
            <img src="@/assets/rocket.jpg" alt="" style="width:30px; border-radius:15px;" class="me-1">
            Movie Space
          </a>
        </router-link>
        <button class="navbar-toggler bg-light" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item fs-4" id="nav2">
              <router-link to="/movielist" class="nav-link me-3">추천</router-link>
            </li>
            <li class="nav-item dropdown fs-4" id="nav3">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                게시판
              </a>
              <ul class="dropdown-menu bg-dark" aria-labelledby="navbarDropdown">
                <li class="fs-5">
                  <router-link to="/newReviews" class="dropdown-item">
                    최근 한줄평
                  </router-link>
                </li>
                <li class="fs-5">
                  <router-link to="/articleList" class="dropdown-item">게시판</router-link>
                </li>
                <li><hr class="dropdown-divider bg-light"></li>
                <li class="fs-5"><a class="dropdown-item" href="#" onClick="window.open('https://www.youtube.com')">Youtube</a></li>
              </ul>
            </li>
            <li class="nav-item fs-4" v-if="user.username === 'admin'">
              <a href="http://127.0.0.1:8000/admin" class="nav-link ms-3">관리자</a>
            </li>
          </ul>
          <form id="search-content" class="nav-item" onsubmit="return false">
            <input v-model="search" type="text" name="input" class="search-input" id="search-input" @keyup.enter="searchMovie">
            <button type="reset" class="search" id="search-btn"></button>
          </form>
          <div class="fs-6 d-inline" style="width:150px;">
            {{ weather.date }} 서울의 기온 {{ weather.temp }}℃
            <img :src="getImg" alt="">
          </div>
          <div class="nav-item navbar p-0" v-if="isLogin">
            <a class="nav-link dropdown-toggle fs-3" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              <!-- <img class="me-2" :src="user.image" style="width:40px; height:40px; border-radius:20px;" v-if="user.image"> -->
              <img class="me-2" src="@/assets/img.jpg" style="width:60px; height:60px; border-radius:30px;">
              {{ user.username }}
            </a>
            <ul class="dropdown-menu dropdown-menu-end bg-dark mt-4" style="font-size:20px;" aria-labelledby="navbarDropdown">
              <li @click="getAnotherUser">
                <a class="dropdown-item fs-4" href="#">내 정보</a>
              </li>
              <li class="fs-4"><a class="dropdown-item fs-4" href="#">플레이리스트</a></li>
              <li><hr class="dropdown-divider bg-light"></li>
              <li>
                <a @click="logout" class="dropdown-item fs-4" href="#">로그아웃</a>
              </li>
            </ul>
          </div>
          <span v-else class="nav-item navbar">
            <ul class="navbar col">
              <li class="navbar-nav">
                <router-link to="/login" class="nav-link fs-2">
                  로그인
                  <br>
                </router-link>
              </li>
              <li class="navbar-nav">
                <router-link to="/signup" class="nav-link fs-2">회원가입</router-link>
              </li>
            </ul>
          </span>   
        </div>
      </div>
    </div>
    <router-view :key="$route.fullPath" />
  </div>
</template>
<script>
/* 일단 cdn으로 붙여넣었는데 axios오류... 어떡할까... */
import axios from 'axios'
import { mapState } from 'vuex'

const URL = 'http://127.0.0.1:8000/movies/'

export default {
  name: 'App',
  data: function () {
    return {
      username: 'user',
      search: '',
    }
  },
  created: function () {
    console.log(this.logined())
    if (!localStorage.getItem('jwt')) {
      this.$router.push({ name: 'Login' })
    } else {
      this.$store.dispatch('isLogin', true)
    }
    axios.get(URL)
      .then(response => {
        this.$store.dispatch('getMovies', response.data)
        return response
      })
      .catch(error => {
        console.log(error)
      })
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/genres/',
      data: {},
    })
    .then((res)=> {
      this.$store.dispatch('getGenres', res.data)
    })

    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/best/',
      data: {},
    })
    .then((res)=>{
      // console.log(res.data)
      this.$store.dispatch('getBests', res.data)
      // this.bestmovies = res.data
      // console.log(this.bestmovies)
    })
    .catch((err) => {
      console.log(err)
    })
    
  },
  /* DOM이 모두 구성된 후에 인식할 수 있으므로 mounted 사용 */
  mounted: function () {
    const input = document.querySelector("#search-input");
    const searchBtn = document.querySelector("#search-btn");
    
    const expand = () => {
      searchBtn.classList.toggle("close");
      input.classList.toggle("square");
    };
    searchBtn.addEventListener("click", expand);
    this.user.image='img'

    const date = new Date()
    const date1 = date.toString()
    const now = date1.substr(16, 2)
    const today = date1.substr(8, 2)

    axios.get('http://api.openweathermap.org/data/2.5/forecast?q=seoul&lang=ko_kr&APPID=c102a437a9d8f986c74e57cd6a2dbce1')
      .then((res) => {
        return res.data.list
      })
      .then(res => {
        res.forEach((e) => {
          if (e.dt_txt.toString().substr(11, 2) - now <= 3 && e.dt_txt.toString().substr(8, 2) === today) {
            this.date = e.dt_txt
            this.temp = Math.round(e.main.temp - 273.15)
            this.img = e.weather[0].icon
            // console.log(this.date)
            // console.log(this.temp)
          }
        })
        return res
      })
      .then(res => {
        const weather = {
          date: this.date,
          temp: this.temp,
          img: this.img
        }
        this.$store.dispatch('getWeather', weather)
        return res
      })
      .catch(err => {
        console.error(err);
    });
    
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.dispatch('logout')
      this.$router.push({ name: 'Login' })
    },
    getAnotherUser: function () {
      this.$store.dispatch('getAnotherUser', this.user)
      this.$router.push({ name: 'Profile' }).catch(() => {
        this.$router.go(this.$router.currentPage)
      })
    },
    searchMovie: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.search}/search`,
        data: this.search,
        headers: this.setToken()
      })
        .then(res => {
          this.$store.dispatch('getMovie', res.data)
          return res
        })
        .then(res => {
          this.$router.push({ name:'MovieDetail' })
          this.search = ''
          return res
        })
        .catch(err => {
          alert('존재하지 않는 영화를 입력하셨습니다.')
          console.log(err)
        })
    },
    logined: function () {
      if (localStorage.getItem('jwt')) {
        return true
      } else {
        return false
      }
    },
    /* 이곳에 methods로 검색 기능 넣어줘야 함 */
  },
  computed: {
    ...mapState ([
      'user',
      'isLogin',
      'weather',
    ]),
    getImg: function () {
      return `http://openweathermap.org/img/w/${this.weather.img}.png`
    }
  },

}

</script>
<!-- CSS only -->
<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    /* color: #2c3e50; */
    /* 혹시 몰라 위에 color 안 지움. */
    color: white;
  }

  #nav {
    font-size: 15px;
    padding: 20px;
    padding-right: 0px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
    color: white;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
    font-weight: bold;
  }

  /* 비디오 background로 보여주기 */
  #bg-video {
    position: fixed;
    left: 50%;
    top: 50%;
    bottom: auto;
    right: auto;
    min-width: 100%;
    min-height: 100%;
    transform: translateX(-50%) translateY(-50%);
    z-index: -100;
    background-image: url(assets/astro.jpg);
    background-position: center;
    background-size: cover;
    background-repeat: no-repeat;
  }

/*  */
/* 여기부터 Search Box 관련 CSS */
/*  */
/* 나중에 absolute 위치와 글씨 크기를 조정해서 레이아웃을 깔끔하게 만들어야 한다. */
  #search-content {
    text-align: start;
    position: absolute;
    height: 50px;
    width: 300px;
    /* margin-left: 170px; */
    margin-top: 50px;
    /* top: 77%;
    right: -20%; */
    top: 10%;
    right: 10%;
    /* transform: translate(-50%, -50%); */
  }

  #search-content.on {
    -webkit-animation-name: in-out;
    animation-name: in-out;
    -webkit-animation-duration: 0.7s;
    animation-duration: 0.7s;
    -webkit-animation-timing-function: linear;
    animation-timing-function: linear;
    -webkit-animation-iteration-count: 1;
    animation-iteration-count: 1;
  }

  .search-input {
    text-align: start;
    box-sizing: border-box;
    /* 이곳과 search, close, square 등 건드려서 크기 조절 */
    width: 50px;
    height: 50px;
    border: 4px solid #ffffff;
    border-radius: 50%;
    background: none;
    color: #fff;
    font-size: 16px;
    font-weight: 400;
    font-family: Roboto;
    outline: 0;
    -webkit-transition: width 0.4s ease-in-out, border-radius 0.8s ease-in-out,
      padding 0.2s;
    transition: width 0.4s ease-in-out, border-radius 0.8s ease-in-out,
      padding 0.2s;
    -webkit-transition-delay: 0.4s;
    transition-delay: 0.4s;
    -webkit-transform: translate(-100%, -50%);
    -ms-transform: translate(-100%, -50%);
    transform: translate(-100%, -50%);
  }

  .search {
    background: none;
    position: absolute;
    top: 0px;
    left: 0;
    height: 50px;
    width: 50px;
    padding: 0;
    border-radius: 100%;
    outline: 0;
    border: 0;
    color: inherit;
    cursor: pointer;
    -webkit-transition: 0.2s ease-in-out;
    transition: 0.2s ease-in-out;
    -webkit-transform: translate(-100%, -50%);
    -ms-transform: translate(-100%, -50%);
    transform: translate(-100%, -50%);
  }

  .search:before {
    content: "";
    position: absolute;
    width: 20px;
    height: 4px;
    background-color: #fff;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
    margin-top: 26px;
    margin-left: 17px;
    -webkit-transition: 0.2s ease-in-out;
    transition: 0.2s ease-in-out;
  }

  .close {
    -webkit-transition: 0.4s ease-in-out;
    transition: 0.4s ease-in-out;
    -webkit-transition-delay: 0.4s;
    transition-delay: 0.4s;
  }

  .close:before {
    content: "";
    position: absolute;
    width: 27px;
    height: 4px;
    margin-top: -1px;
    margin-left: -13px;
    background-color: #fff;
    -webkit-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    transform: rotate(45deg);
    -webkit-transition: 0.2s ease-in-out;
    transition: 0.2s ease-in-out;
  }

  .close:after {
    content: "";
    position: absolute;
    width: 27px;
    height: 4px;
    background-color: #fff;
    margin-top: -1px;
    margin-left: -13px;
    cursor: pointer;
    -webkit-transform: rotate(-45deg);
    -ms-transform: rotate(-45deg);
    transform: rotate(-45deg);
  }

  .square {
    box-sizing: border-box;
    padding: 0 40px 0 10px;
    width: 300px;
    height: 50px;
    border: 4px solid #ffffff;
    border-radius: 0;
    background: none;
    color: #fff;
    font-family: Roboto;
    font-size: 16px;
    font-weight: 400;
    outline: 0;
    -webkit-transition: width 0.4s ease-in-out, border-radius 0.4s ease-in-out,
      padding 0.2s;
    transition: width 0.4s ease-in-out, border-radius 0.4s ease-in-out,
      padding 0.2s;
    -webkit-transition-delay: 0.4s, 0s, 0.4s;
    transition-delay: 0.4s, 0s, 0.4s;
    -webkit-transform: translate(-100%, -50%);
    -ms-transform: translate(-100%, -50%);
    transform: translate(-100%, -50%);
  }
/*  */
/* 여기까지 Search Box 관련 CSS */
/*  */

/*  */
/* 여기부터 profile 관련 CSS */
/*  */

/*  */
/* 여기까지 profile 관련 CSS */
/*  */
</style>