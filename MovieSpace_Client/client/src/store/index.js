import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    movie: {},
    user: {},
    anotherUser: {},
    articles: [],
    article: {},
    comments: [],
    genres: [],
    bestMovies: [],
    isLogin: false,
    weather: {},
    reviews: [],
  },
  mutations: {
    GET_MOVIES: function (state, movies) {
      state.movies = movies
    },
    GET_MOVIE: function (state, movie) {
      state.movie = movie
    },
    GET_GENRES: function (state, genres) {
      state.genres = genres
    },
    GET_BESTS: function (state, movies) {
      state.bestMovies = movies
    },
    GET_USER: function (state, user) {
      state.user = user
      state.isLogin = true
    },
    GET_ANOTHER_USER: function (state, user) {
      state.anotherUser = user
    },
    LOGOUT: function (state) {
      state.user = {}
      state.isLogin = false
    },
    GET_ARTICLES: function (state, articles) {
      state.articles = articles
    },
    GET_ARTICLE: function (state, article) {
      state.article = article
    },
    GET_COMMENTS: function (state, comments) {
      state.comments = comments
    },
    DELETE_USER: function (state) {
      state.user = []
    },
    IS_LOGIN: function (state, status) {
      state.isLogin = status
    },
    UPDATE_USER: function (state, user) {
      state.user.last_name = user.last_name
      state.user.birth = user.birth
      state.user.introduction = user.introduction
      state.user.email = user.email
      state.user.image = user.image
      state.anotherUser = state.user
    },
    GET_WEATHER: function (state, weather) {
      state.weather = weather
    },
    GET_REVIEWS: function (state, reviews) {
      state.reviews = reviews
    },
  },
  actions: {
    getMovies: function({commit}, movies) {
      commit('GET_MOVIES', movies)
    },
    getMovie: function({commit}, movie) {
      commit('GET_MOVIE', movie)
    },
    getGenres: function({commit}, genres) {
      commit('GET_GENRES', genres)
    },
    getBests: function({commit}, movies) {
      commit('GET_BESTS', movies)
    },
    getUser: function({commit}, user) {
      commit('GET_USER', user)
    },
    getAnotherUser: function({commit}, user) {
      commit('GET_ANOTHER_USER', user)
    },
    logout: function ({commit}) {
      commit('LOGOUT')
    },
    getArticles: function ({commit}, articles) {
      commit('GET_ARTICLES', articles)
    },
    getArticle: function ({commit}, article) {
      commit('GET_ARTICLE', article)
    },
    getComments: function ({commit}, comments) {
      commit('GET_COMMENTS', comments)
    },
    deleteUser: function ({commit}) {
      commit('DELETE_USER')
    },
    isLogin: function ({commit}, status) {
      commit('IS_LOGIN', status)
    },
    updateUser: function ({commit}, user) {
      commit('UPDATE_USER', user)
    },
    getWeather: function ({commit}, weather) {
      commit('GET_WEATHER', weather)
    },
    getReviews: function ({commit}, reviews) {
      commit('GET_REVIEWS', reviews)
    },

  },
  getters: {
    
  },
  modules: {
  }
})
