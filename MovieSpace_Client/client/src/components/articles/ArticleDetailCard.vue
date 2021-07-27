<template>
  <div class="container">
    <h3>상세 페이지</h3>
    <hr>
		<div class="row text-start text-secondary">
			<h5 class="col-7">작성자 : 
				<span style="cursor:pointer;" @click="getProfile">
					{{ article.username }}
				</span>
			</h5>
			<h5 class="col text-end">작성일자 : {{ article.created_at }}</h5>
			<h5 class="col text-end">수정일자 : {{ article.updated_at }}</h5>
		</div>
		<hr>
    <div class="field">
      <label for="demo-title" class="text-start fs-5 my-2">Title</label>
      <h3 name="demo-title" id="demo-title" class="mb-5">
        {{ article.title }}
      </h3>
    </div>
    <hr>
    <div class="field">
      <label for="demo-content" class="text-start fs-5 my-2">Content</label>
      <h3 name="demo-content" id="demo-content" class="mb-5" >
        {{ article.content }}
      </h3>
    </div>
    <hr>
    <div>
      <div class="text-start">
        <label for="demo-hashtag" class="fs-4 my-2">HashTag</label>
        <a href="#">#{{ movies[0].title }}</a>
        <br>
        <a href="#">#{{ movies[1].title }}</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  name: 'ArticleDetailCard',
  computed: {
    ...mapState([
      'article',
      'movies',
      'user'
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
		getProfile: function () {
			axios({
				method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.article.username}`,
        data: {},
        headers: this.setToken()
			})
				.then(res => {
					this.$store.dispatch('getAnotherUser', res.data)
					return res.data
				})
				.then(res => {
					this.$router.push({ name: 'Profile' })
					return res
				})
				.catch(err => {
					console.log(err)
				})
		}
	}
}
</script>

<style scoped>
  form {
		margin: 0 0 1.5rem 0;
	}

		form > :last-child {
			margin-bottom: 0;
		}

		form > .fields {
			display: -moz-flex;
			display: -webkit-flex;
			display: -ms-flex;
			display: flex;
			-moz-flex-wrap: wrap;
			-webkit-flex-wrap: wrap;
			-ms-flex-wrap: wrap;
			flex-wrap: wrap;
			width: calc(100% + 3rem);
			margin: -1.5rem 0 1.5rem -1.5rem;
		}

			form > .fields > .field {
				-moz-flex-grow: 0;
				-webkit-flex-grow: 0;
				-ms-flex-grow: 0;
				flex-grow: 0;
				-moz-flex-shrink: 0;
				-webkit-flex-shrink: 0;
				-ms-flex-shrink: 0;
				flex-shrink: 0;
				padding: 1.5rem 0 0 1.5rem;
				width: calc(100% - 1.5rem);
			}

				form > .fields > .field.half {
					width: calc(50% - 0.75rem);
				}

				form > .fields > .field.third {
					width: calc(100%/3 - 0.5rem);
				}

				form > .fields > .field.quarter {
					width: calc(25% - 0.375rem);
				}

		@media screen and (max-width: 736px) {

			form > .fields {
				width: calc(100% + 2.25rem);
				margin: -1.125rem 0 1.5rem -1.125rem;
			}

				form > .fields > .field {
					padding: 1.125rem 0 0 1.125rem;
					width: calc(100% - 1.125rem);
				}

					form > .fields > .field.half {
						width: calc(100% - 1.125rem);
					}

					form > .fields > .field.third {
						width: calc(100% - 1.125rem);
					}

					form > .fields > .field.quarter {
						width: calc(100% - 1.125rem);
					}

		}
	label {
		color: rgba(255, 255, 255, 0.875);
		display: block;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 0.8rem;
		font-weight: 700;
		margin: 0 0 0.4875rem 0;
	}
	h5 span:hover {
		color: skyblue;
		text-decoration: underline;
	}
</style>