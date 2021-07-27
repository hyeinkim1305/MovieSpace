<template>
  <div>
    <div id="portfolio">
    <!-- <div> -->
      <h3 class="fw-bolder">{{ anotherUser.username }} 님의 Playlists</h3>
      <h4 class="d-inline fw-bold">playlist 추가</h4>
      <img class="mb-2 ms-2" src="@/assets/plus.png" height="30px;" onclick="document.getElementById('modal-wrapper').style.display='block'" style="cursor:pointer;">
    </div>
    <div id="portfolio">
      <section class="clearfix">
        <div class="project-section">
          <div class="project-container">
            <div class="project-img-container" onclick="document.getElementById('modal-playlist').style.display='block'">
              <img :src="'https://image.tmdb.org/t/p/w500' + movies[20].poster_path" alt="project image">
            </div>
            <p class="project-title text-dark">내 플레이리스트1</p>
          </div>
          <div class="project-container" v-for="(playlist, idx) in playlists" :key="idx">
            <div class="project-img-container" @click="click_modal(playlist)">
              <img :src="'https://image.tmdb.org/t/p/w500' + movies[18].poster_path" alt="project image">
            </div>
            <p class="project-title text-dark">{{ playlist.list_name }}</p>
          </div>
        </div>

        <!-- add playlist modal start -->
        <div id="modal-wrapper" class="modal">
          <form class="modal-content animate">
            <div class="imgcontainer">
              <span onclick="document.getElementById('modal-wrapper').style.display='none'" class="close" title="Close PopUp">&times;</span>
              <img src="@/assets/rocket.jpg" alt="project" class="avatar">
              <h1 class="project_details" style="text-align:center">Playlist 추가</h1>
            </div>
            <div class="container">
              <input type="text" placeholder="Playlist Name" name="uname" v-model="playlist_info.list_name">
              <textarea class="project_description" rows="3" placeholder="Playlist Description" v-model="playlist_info.list_description"></textarea>
              <button class="project_submit" type="button" @click="addPlaylist">확인</button>
              <button class="project_cancel" style="" type="submit" onclick="document.getElementById('modal-wrapper').style.display='none'">취소</button>
            </div>
          </form>
        </div>
        <!-- add playlist modal end -->

        <!-- modal playlist start -->
        <div id="modal-playlist" class="modal">
          <form class="modal-content animate">
            <div class="imgcontainer">
              <span onclick="document.getElementById('modal-playlist').style.display='none'" class="close" title="Close PopUp">&times;</span>
              <img src="@/assets/rocket.jpg" alt="project" class="avatar">
              <h1 class="project_details" style="text-align:center">{{ clicked_playlist.list_name }}</h1>
              <textarea :value="clicked_playlist.list_description" class="project_description" rows="3" placeholder="Project Description" readonly></textarea>
            </div>
            <div class="container">
              <div v-for="(playlist_movie, idx) in playlist_movies" :key="idx">{{ playlist_movie.title }}</div>
              <button class="project_submit" type="button" onclick="document.getElementById('modal-playlist').style.display='none'">확인</button>
              <button class="project_submit" style="background-color:red;" type="button" @click="deletePlaylist">삭제</button>
            </div>
          </form>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'Playlists',
  computed: {
    ...mapState([
      'movies',
      'anotherUser',
      'user',
      // 'playlists'
    ]),
  },
  created: function () {
    this.getPlaylists()

  },
  data: function () {
    return {
      playlist_info: {
        list_name: '',
        list_description: '',
      },
      playlists: [],
      clicked_playlist: {},
      playlist_movies: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    click_modal: function (playlist) {
      this.clicked_playlist = playlist
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.anotherUser.username}/${playlist.id}/movies`,
        data: {},
        headers: this.setToken(),
      })
        .then(res => {
          this.playlist_movies = res.data.myMovies
          return res
        })
        .then(res => {
          const modal = document.querySelector('#modal-playlist')
          modal.setAttribute('style', 'display:block;')
          return res
        })
        .catch(err => {
          console.log(err)
        })
    },
    getPlaylists: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movies/${this.anotherUser.username}/playlist/`,
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
    addPlaylist: function () {
      const playlist = {
        list_name: this.playlist_info.list_name,
        list_description: this.playlist_info.list_description,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/${this.user.username}/playlist/`,
        data: playlist,
        headers: this.setToken()
      })
      .then(res => {
        this.getPlaylists()
        const modal = document.querySelector('#modal-wrapper')
        modal.setAttribute('style', 'display:none;')
        return res
      })
      .catch(err => {
        console.log(err)
      })
    },
    deletePlaylist: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${this.user.username}/playlist/${this.clicked_playlist.id}`,
        data: {},
        headers: this.setToken()
      })
        .then(res => {
          const modal = document.querySelector('#modal-playlist')
          modal.setAttribute('style', 'display:none;')
          this.getPlaylists()
          return res
        })
        .then(err => {
          console.log(err)
        })
    },
    getMovies: function () {
      axios({
        method: 'get',
        url: ``,
        data: {},
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
        })
    }
  }
}
</script>

<style scoped>
*, *:before, *:after {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* HTML5 DECLARATIONS */
article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section, dialog {
  display: block
}

audio[controls], canvas, video {
  display: inline-block;
  *display: inline;
  zoom: 1
}

/* BASE */
html {
  height: 100%;
  font-size: 100%;
  overflow-y: scroll;
  -webkit-text-size-adjust: 100%
}

/* Force scrollbar in non-IE and Remove iOS text size adjust without disabling user zoom */
body {
  margin: 0;
  min-height: 100%;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
  color: #666
}

/* Improve default text rendering, handling of kerning pairs and ligatures */
/* DEFAULT FONT SETTINGS */
/* 16px base font size with 150% (24px) friendly, unitless line height and margin for vertical rhythm */
/* Font-size percentage is based on 16px browser default size */
body, button, input, select, textarea {
  font: 100% 'Lato', sans-serif;
  *font-size: 1em;
  color: #555
}

/* IE7 and older can't resize px based text */
p, blockquote, q, pre, address, hr, code, samp, dl, ol, ul, form, table, fieldset, menu, img {
  margin: 0 0 1.5em;
  padding: 0
}

/* TYPOGRAPHY */
/* Composed to a scale of 12px, 14px, 16px, 18px, 21px, 24px, 36px, 48px, 60px and 72px */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Open Sans', sans-serif;
  color: #444;
}

h1 {
  margin: 0;
  font-size: 4.75em;
  line-height: 1.2em;
  margin-bottom: 0.4em
}

/* 60px / 72px */
h2 {
  margin: 0;
  font-size: 2.75em;
  line-height: 1.3em;
  margin-bottom: 0.5em
}

/* 48px / 48px */
h3 {
  margin: 0;
  font-size: 2.25em;
  line-height: 1.3333333333333333333333333333333em;
  margin-bottom: 0.6667em
}

/* 36px / 48px */
h4 {
  margin: 0;
  font-size: 1.5em;
  line-height: 1em;
  margin-bottom: 1em
}

/* 24px / 24px */
h5 {
  margin: 0;
  font-size: 1.3125em;
  line-height: 1.1428571428571428571428571428571em;
  margin-bottom: 1.1428571428571428571428571428571em
}

/* 21px / 24px */
h6 {
  margin: 0;
  font-size: 2.75em;
  line-height: 1.2em;
  margin-bottom: 0.4em
}

/* 18px / 24px */
h7 {
  margin: 0;
  font-size: 0.5em;
  line-height: 1.3em;
  margin-bottom: 0.5em
}

p, ul, blockquote, pre, th, label {
  margin: 0;
  font-size: 1em;
  line-height: 1.5em;
  margin-bottom: 1.5em
}

/* 16px / 24px */
small, p.small {
  margin: 0;
  font-size: 0.875em;
  line-height: 1.7142857142857142857142857142857em;
  margin-bottom: 1.7142857142857142857142857142857em
}

/* 14px / 24px */
/* CODE */
pre {
  white-space: pre;
  white-space: pre-wrap;
  word-wrap: break-word
}

/* Allow line wrapping of 'pre' */
pre, code, kbd, samp {
  font-size: 1em;
  line-height: 1.5em;
  margin-bottom: 1.5em;
  font-family: Menlo, Consolas, 'DejaVu Sans Mono', Monaco, monospace
}

/* TABLES */
table {
  border-collapse: collapse;
  border-spacing: 0;
  margin-bottom: 1.5em;
  display: flex;
  margin-left: 105px;
}

th {
  text-align: left
}

th {
  padding: 800px;
  border-bottom: 0 solid #333
}

/* FORMS */
form {
  margin: 0
}

fieldset {
  border: 0;
  padding: 0
}

textarea {
  overflow: auto;
  vertical-align: top
}

legend {
  *margin-left: -.75em
}

button, input, select, textarea {
  vertical-align: baseline;
  *vertical-align: middle
}

/* IE7 and older */
button, input {
  line-height: normal;
  *overflow: visible
}

button, input[type="button"], input[type="reset"], input[type="submit"] {
  cursor: pointer;
  -webkit-appearance: button
}

input[type="checkbox"], input[type="radio"] {
  box-sizing: border-box
}

input[type="search"] {
  -webkit-appearance: textfield;
  -moz-box-sizing: content-box;
  -webkit-box-sizing: content-box;
  box-sizing: content-box
}

input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none
}

button::-moz-focus-inner, input::-moz-focus-inner {
  border: 0;
  padding: 0
}

/* QUOTES */
blockquote, q {
  quotes: none
}

blockquote:before, blockquote:after, q:before, q:after {
  content: '';
  content: none
}

blockquote, q, cite {
  font-style: italic
}

blockquote {
  padding-left: 1.5em;
  border-left: 3px solid #ccc
}

blockquote>p {
  padding: 0
}

/* LISTS */
ul, ol {
  list-style-position: inside;
  padding: 0
}

li ul, li ol {
  margin: 0 1.5em
}

dl dd {
  margin-left: 1.5em
}

dt {
  font-family: Futura, "Century Gothic", AppleGothic, sans-serif
}

/* HYPERLINKS */
a {
  text-decoration: none;
  color: #444;
  -webkit-transition: color 0.1s linear, border 0.1s linear, opacity 0.1s linear, background-color 0.1s linear;
  -moz-transition: color 0.1s linear, border 0.1s linear, opacity 0.1s linear, background-color 0.1s linear;
  -ms-transition: color 0.1s linear, border 0.1s linear, opacity 0.1s linear, background-color 0.1s linear;
  -o-transition: color 0.1s linear, border 0.1s linear, opacity 0.1s linear, background-color 0.1s linear;
  transition: color 0.1s linear, border 0.1s linear, opacity 0.1s linear, background-color 0.1s linear;
}

a:hover, a:focus, a:active {
  text-decoration: none;
  border: none;
  color: #2E8B57;
}

/* MEDIA */
figure {
  margin: 0
}

img, object, embed, video {
  max-width: 100%;
  _width: 100%
}

/* Fluid images */
img {
  border: 0;
  -ms-interpolation-mode: bicubic
}

/* Improve IE's resizing of images */
svg:not(:root) {
  overflow: hidden
}

/* Correct IE9 overflow */
/* ABBREVIATION */
abbr[title], dfn[title] {
  border-bottom: 1px dotted #333;
  cursor: help
}

/* MARKED/INSERTED/DELETED AND SELECTED TEXT */
ins, mark {
  text-decoration: none
}

mark {
  background: #c47529
}

ins {
  background: #d49855
}

del {
  text-decoration: line-through
}

::-moz-selection {
  background: #2E8B57;
  color: #fff;
  text-shadow: none
}

/* selected text */
::selection {
  background: #2E8B57;
  color: #fff;
  text-shadow: none
}

/* selected text */
/* OTHERS */
strong, b, dt {
  font-weight: bold
}

dfn {
  font-style: italic
}

var, address {
  font-style: normal
}

sub, sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline
}

/* Position 'sub' and 'sup' without affecting line-height */
sup {
  top: -0.5em
}

/* Move superscripted text up */
sub {
  bottom: -0.25em
}

/* Move subscripted text down */
span.amp {
  font-family: Adobe Caslon Pro, Baskerville, "Goudy Old Style", "Palatino", "Palatino Linotype", "Book Antiqua", Georgia, "Times New Roman", Times, serif;
  font-style: italic;
  font-size: 110%;
  line-height: 0;
  position: relative;
  vertical-align: baseline
}

/* Best available ampersand */
/* MICRO CLEARFIX HACK */
.cf:before, .cf:after {
  content: "";
  display: table
}

/* For modern browsers */
.cf:after {
  clear: both
}

.cf {
  zoom: 1
}

/* For IE 6/7 (trigger hasLayout) */
/* DEFAULT MOBILE STYLE */
body {
  width: 92%;
  margin: 0 auto
}

/* Center page without wrapper */
/* column grid */
.g1, .g2, .g3 {
  display: block;
  position: relative;
  margin-left: 1%;
  margin-right: 1%
}

/* 1 column grid */
.g1, .g2, .g3 {
  width: 98.0%
}

/* Wrapper */
.main {
  padding-top: 50px;
  max-width: 1020px;
}

.wrapper {
  margin: 0 auto;
}

/* Utility */
.chromeframe {
  margin: 0.2em 0;
  background: #ccc;
  color: #000;
  padding: 0.2em 0;
}

.clear {
  clear: both;
}

.bg-fixed {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center center;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

.clearfix:after {
  content: ".";
  visibility: hidden;
  display: block;
  height: 0;
  clear: both;
}

.no-list {
  margin: 0px;
  padding: 0px;
  list-style: none;
}

.break {
  padding-bottom: 1em;
  clear: both;
}

/* Backgrounds */
.bg-1 {
  /* background-image: url('@/assets/img.jpg'); */
}

/* Header */
#header {
  margin-bottom: 2em;
}

#header #logo {
  text-align: center;
  display: none;
}

#header #helloworld {
  text-align: center;
  display: none;
}

#header h4 {
  margin-bottom: 0px;
}

#header .visible {
  opacity: 1;
}

/* Tabs */
.etabs {
  margin: 0;
  padding: 0px;
  text-align: center;
}

.etabs li span {
  display: none;
}

#tab-data-wrap {
  padding: 30px 20px;
  background: #fff;
  border: 1px solid #f1f1f1;
  box-shadow: 0px 6px #2E8B57;
  border-radius: 0px 0px 4px 4px;
}

.tab {
  display: inline-block;
  zoom: 1;
  *display: inline;
  background: #fff;
  border: solid 1px #f1f1f1;
  border-bottom: 0px;
  border-radius: 4px 4px 0 0;
  -moz-border-radius: 4px 4px 0 0;
  -webkit-border-radius: 4px 4px 0 0;
  margin-right: 10px;
}

.tab a {
  font-weight: bold;
  text-transform: uppercase;
  font-size: 14px;
  display: block;
  padding: 2px 10px;
  outline: none;
  color: #888;
  text-decoration: none;
}

.tab a:hover {
  text-decoration: none;
}

.tab.active {
  background: #fff;
  position: relative;
  top: 1px;
  border-color: #f1f1f1;
  border-bottom: none;
}

.tab a.active {
  padding-top: 10px;
  color: #2E8B57;
}

.tab a i {
  font-size: 16px;
  margin-right: 0px;
}


/* Photo */
.photo {
  float: left;
  height: 200px;
  width: 200px;
  margin-right: 20px;
  margin-top: 30px;
  overflow: hidden;
}

.photo img {
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
  width: 100%;
}

.info h1, #header h1 {
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: .3em;
  color: #fff;
}

.info h2, #header h2 {
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: .2em;
  margin-top: 0.5em;
}

.info h4, #header h4 {
  color: #59BD85;
  margin-bottom: 2em;
}

.info h6, #header h6 {
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: .3em;
  color: #fff;
}

.info h7, #header h7 {
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: .2em;
  margin-top: 0.5em;
  color: #fff;
}

/* Contact */

.main-links ul {
  list-style: none outside none;
  margin: 0;
  padding: 0;
}

.main-links ul li {
  border-bottom: 1px solid #F1F1F1;
  padding: 10px 0;
}

.main-links ul li a {
  font-size: 14px;
}

/* Icon Styling */
.contact-info i {
  color: #333;
  font-size: 46px;
}

/* Item Box */
.item-box {
  padding: 6px 6px 6px 10px;
  border: 1px solid #fff;
  -webkit-border-radius: 4px;
  -moz-border-radius: 4px;
  border-radius: 4px;
}

.item-box i {
  float: left;
  margin-right: 12px;
}

.item-box .item-data {
  margin-top: 6px;
}

.item-box .item-data h3 {
  line-height: 1em;
  margin: 3px 0px 0px 0px;
  font-size: 1em;
}

.item-box .item-data p {
  margin: 0px;
  font-size: 12px;
  color: #2E8B57;
  text-decoration-style: bold;
}

/* WorkExperience */
.work li {
  border-bottom: 1px solid #f1f1f1;
  margin-bottom: 2em;
}

.work li span {
  float: right;
}

.work li h5 {
  float: left;
}

.work li p {
  clear: both;
}

/* Portfolio */
.image {
  position: relative;
}

.image img {
  margin: 0px;
  width: 100%;
}

.image-overlay {
  position: absolute;
  z-index: 5;
  top: 0;
  overflow: hidden;
  width: 100%;
  height: 99%;
  background-color: rgba(231, 76, 60, .6);
  text-align: center;
  opacity: 0;
  filter: alpha(opacity=0);
  -webkit-transition: all 450ms ease-out 0s;
  -moz-transition: all 450ms ease-out 0s;
  -o-transition: all 450ms ease-out 0s;
  transition: all 450ms ease-out 0s;
  -webkit-transform: rotateY(180deg);
  -moz-transform: rotateY(180deg);
  -ms-transform: rotateY(180deg);
  transform: rotateY(180deg);
}

.image:hover .image-overlay {
  opacity: 1;
  filter: alpha(opacity=100);
  -webkit-transform: rotateY(0deg);
  -moz-transform: rotateY(0deg);
  -ms-transform: rotateY(0deg);
  transform: rotateY(0deg);
}

.image-overlay .image-link {
  position: relative;
  top: 50%;
  display: inline-block;
  margin-top: -20px;
}

/* Icon Box */
.sny-icon {
  display: block;
  margin-bottom: 1em;
  text-align: center;
}

.sny-icon i {
  display: inline-block;
  font-size: 60px;
}

.sny-icon-content {
  text-align: center;
}

.sny-icon-content h4 {
  margin-bottom: 6px;
}

.sny-icon-content p {
  margin-bottom: 0px;
}

/* Buttons */
.btn {
  display: inline-block;
  margin: 0 10px 10px 0;
  padding: 14px 20px;
  background: #E74C3C;
  color: #fff;
  font-weight: bold;
  font-size: 13px;
  font-family: 'Open Sans', sans-serif;
  line-height: 1;
  *display: inline;
  *zoom: 1;
  position: relative;
  text-transform: uppercase;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
  transition: all 0.3s;
}

.btn:hover {
  color: #ccc;
}

/* Labels */
.label {
  display: inline;
  padding: .25em .6em;
  font-size: 90%;
  font-weight: 500;
  line-height: 1;
  color: #ffffff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}

.label-info {
  background-color: #444445E6;
}

.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}

.label[href]:hover,
.label[href]:focus {
  color: #ffffff;
  text-decoration: none;
  cursor: pointer;
}

.label-default {
  background-color: #999999;
}

.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #808080;
}

.label-danger {
  background-color: #d9534f;
}

.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}

.label-success {
  background-color: #5cb85c;
}

.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}

.label-warning {
  background-color: #f0ad4e;
}

.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}

/* Project */
.project-section {
  display: grid;
  grid-template-columns: auto auto auto;
  grid-gap: 1.5rem;
  justify-content: center;
  align-items: center;
}

.project-container {
  max-width: 240px;
  border-radius: 5px;
  background-color: #5cb85c;
  color: #fff;
  cursor: pointer;
  box-shadow: 2px 2px 5px 3px #5cb85c27;
}

.project-img-container {
  width: 100%;
  border-radius: 5px 5px 0px 0px;
}

.project-img-container img {
  width: 100%;
  border-radius: 5px 5px 0px 0px;
  margin-bottom: 0px;
}

.project-title {
  text-align: center;
  margin: 1.2rem auto;
  font-size: 1.2rem;
  font-weight: 600;
}
.project_details{
  text-align: center;
  display: block;
  font-size: 2em;
  margin : 0;
  font-weight: bold;
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

/* Set a style for all buttons */
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

/* Center the image and position the close button */
.imgcontainer {
  text-align: center;
  margin: 12px 0 6px 0;
  position: relative;
}
.avatar {
    width: 175px;
	height:175px;
    border-radius: 50%;
    margin: 0;
}

/* The Modal (background) */
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

/* Modal Content Box */
.modal-content {
  background-color: #fefefe;
  margin: 1% auto 1% auto;
  border: 1px solid #888;
  width: 30%;
  padding-bottom: 20px;
}

/* The Close Button (x) */
.close {
    position: absolute;
    right: 25px;
    top: 0;
    color: #000;
    font-size: 35px;
    font-weight: bold;
}
.close:hover,.close:focus {
    color: red;
    cursor: pointer;
}

/* Add Zoom Animation */
@keyframes zoom {
    from {transform: scale(0)}
    to {transform: scale(1)}
}


/* Meters */
.meter {
  height: 24px;
  /* Can be anything */
  position: relative;
  border: 1px solid #f1f1f1;
  -moz-border-radius: 4px;
  -webkit-border-radius: 4px;
  border-radius: 4px;
  margin-bottom: 1em;
}

.meter>span {
  display: block;
  height: 100%;
  -moz-border-radius: 4px;
  -webkit-border-radius: 4px;
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}

.meter>span>span {
  margin-left: 4px;
  color: #fff;
}

.animate>span:after {
  display: none;
}

@keyframes move {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 50px 50px;
  }
}

.emerald>span {
  background-color: #2E8B57;
}

.carrot>span {
  background-color: #e67e22;
}

.wisteria>span {
  background-color: #8e44ad;
}

.sunflower>span {
  background-color: #f1c40f;
}

.midnight>span {
  background-color: #2c3e50;
}

.pomengrate>span {
  background-color: #c0392b;
}

.asbestos>span {
  background-color: #7f8c8d;
}

.nostripes>span>span, .nostripes>span:after {
  animation: none;
  -webkit-animation: none;
  background-image: none;
}

/* Footer */
footer {
  text-align: center;
  margin-top: 2em;
  padding: 10px;
  background: rgba(255, 255, 255, .8);
  box-shadow: 0px 4px #ccc;
  color: #333;
  -moz-border-radius: 4px;
  -webkit-border-radius: 4px;
  border-radius: 4px;
}

footer p {
  margin-bottom: 0px;
}

/* media Queries

FOLDING FLUID GRID
< 767px         - 1-Column Fluid Grid
768px - 1023px  - 2-Column Fluid Grid
> 1024px            - 3-Column Fluid Grid
Change widths as necessary
------------------------------------------- */

/* SMALL TABLET */
@media only screen and (max-width: 600px) {

  .etabs>li span {
    display: block;
  }

  .project-section {
    grid-template-columns: auto;
  }

  .project-container {
    max-width: 200px;
  }
}

/* TABLET/NETBOOK */
@media only screen and (min-width: 768px) {

  /* Sidebar */
  .sidebar {
    padding-left: 20px;
    border-left: 1px solid #f1f1f1;
  }

  /* COLUMN GRID */
  .g1, .g2, .g3 {
    /* display: inline; */
    float: left;
  }

  /* 2 COLUMN GRID */
  .g1 {
    width: 48.0%
  }

  .g2 {
    width: 48.0%
  }

  .g3 {
    width: 98.0%
  }
}

/* progress bar */
.progress-item {
  position: relative;
}

.progress-item .progress-title {
  font-size: 12px;
  font-weight: 400;
  display: inline-block;
  margin-bottom: 5px;
}

.progress-item .progress {
  height: 2px;
  box-shadow: none;
  border-radius: 0;
  background: transparent;
}

.progress-item .progress-bar {
  background-color: #ff5722;
  box-shadow: none;
  text-align: right;
}

.progress-item .progress-percent {
  font-size: 10px;
  background-color: #313131;
  position: absolute;
  top: 5px;
  padding: 0 8px;
  border-radius: 3px;
}

.progress-item .progress-percent::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: -4px;
  border-top: 6px solid #313131;
  border-right: 8px solid transparent;
}

@media (max-width: 768px) {
  .progress-wrapper {
    margin-bottom: 50px;
  }
}

/* LANDSCAPE TABLET/NETBOOK/LAPTOP */
@media only screen and (min-width: 1024px) {

  .etabs>li span {
    display: inline;
  }

  .tab a i {
    font-size: 16px;
    margin-right: 6px;
  }

  .tab a {
    padding: 10px 40px 10px 40px;
  }

  .tab a.active {
    padding-top: 20px;
  }

  /* 3 COLUMN GRID */
  .g1 {
    width: 31.333%
  }

  .g2 {
    width: 64.667%;
  }

  .g3 {
    width: 98.0%
  }
}

/* PRINT */
@media print {
  * {
    background: transparent !important;
    color: black !important;
    text-shadow: none !important;
    filter: none !important;
    -ms-filter: none !important
  }

  /* Black prints faster */
  a, a:visited {
    color: #444 !important;
    text-decoration: underline
  }

  a[href]:after {
    content: " ("attr(href) ")"
  }

  abbr[title]:after {
    content: " ("attr(title) ")"
  }

  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after {
    content: ""
  }

  /* Don't print links for images, javascript or internal links */
  pre, blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }

  thead {
    display: table-header-group;
  }

  /* Repeat header row at top of each printed page */
  tr, img {
    page-break-inside: avoid;
  }

  img {
    max-width: 100% !important;
  }

  @page {
    margin: 0.5cm
  }

  p, h2, h3 {
    orphans: 3;
    widows: 3
  }

  h2, h3 {
    page-break-after: avoid
  }
}

.project-div {
  background-color: #4AB478;
  text-align: center;
  padding: 10px;
}

.image {
  height: 100px;
  background-color: white;
  margin-bottom: 10px;
  font-family: Sofia;
  text-align: center;
  padding-top: 30px;
  font-size: 20px;
  font-weight: bold;
}

.data {
  font-size: 150%;
  font-family: 'Amaranth';
  color: white;
}

td {
  padding: 20px;
  width: 250px;
  height: 200px;
}

tbody {
  display: table-row-group;
  vertical-align: middle;
  display: grid;
}
.animate {
    animation: zoom 0.6s
}

</style>