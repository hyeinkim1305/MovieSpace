<template>
  <div class="text-white span-4-5 container">
    <ArticleDetailCard />
    <CommentForm />
    <CommentList />
    <ul class="actions button-ul" v-if="user.username === article.username">
      <li><router-link to="articleupdate"><input type="button" value="수정" class="primary color2 buttons" /></router-link></li>
      <li><router-link to="articleList"><input type="reset" value="목록" class="buttons" /></router-link></li>
      <li><input type="button" value="삭제" class="primary color2 del" @click="deleteArticle" /></li>
    </ul>
    <ul class="actions button-ul" v-else>
      <li><router-link to="articleList"><input type="reset" value="목록" class="buttons" /></router-link></li>
    </ul>
  </div>
</template>

<script>
import ArticleDetailCard from '@/components/articles/ArticleDetailCard.vue'
import CommentForm from '../../components/articles/CommentForm.vue'
import CommentList from '../../components/articles/CommentList.vue'
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  name: 'ArticleDetail',
  components: {
    ArticleDetailCard,
    CommentForm,
    CommentList,
  },
  computed: {
    ...mapState([
      'user',
      'article',
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
    deleteArticle: function () {
      let like = confirm('삭제하시겠습니까?')
      if (like) {
        if (this.article.username === this.user.username) {
          axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/community/${this.article.id}/`,
            data: '',
            headers: this.setToken(),
          })
            .then(res => {
              console.log(res)
              this.$router.push({ name: 'ArticleList' })
            })
        } else {
          alert('작성자만 삭제 가능합니다.')
        }
      }
    },
  }
}
</script>

<style>
  ul.actions {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		cursor: default;
		list-style: none;
		margin-left: -0.75rem;
		padding-left: 0;
	}

		ul.actions li {
			padding: 0 0 0 0.75rem;
			vertical-align: middle;
		}

		ul.actions.special {
			-moz-justify-content: center;
			-webkit-justify-content: center;
			-ms-justify-content: center;
			justify-content: center;
			width: 100%;
			margin-left: 0;
		}

			ul.actions.special li:first-child {
				padding-left: 0;
			}

		ul.actions.stacked {
			-moz-flex-direction: column;
			-webkit-flex-direction: column;
			-ms-flex-direction: column;
			flex-direction: column;
			margin-left: 0;
		}

			ul.actions.stacked li {
				padding: 0.975rem 0 0 0;
			}

				ul.actions.stacked li:first-child {
					padding-top: 0;
				}

		ul.actions.fit {
			width: calc(100% + 0.75rem);
		}

			ul.actions.fit li {
				-moz-flex-grow: 1;
				-webkit-flex-grow: 1;
				-ms-flex-grow: 1;
				flex-grow: 1;
				-moz-flex-shrink: 1;
				-webkit-flex-shrink: 1;
				-ms-flex-shrink: 1;
				flex-shrink: 1;
				width: 100%;
			}

				ul.actions.fit li > * {
					width: 100%;
				}

			ul.actions.fit.stacked {
				width: 100%;
			}

  .buttons {
    color: white;
    background: transparent;
    cursor: pointer;
    font-size: 1.0rem;
    line-height: 2.75rem;
    padding: 0 1.5rem 0 1.65rem;
    list-style: none;
    border-radius: 6px;
    letter-spacing: 0.15rem;
    white-space: nowrap;
    font-weight: 700;
  }

  .del {
    color: white;
    background: transparent;
    cursor: pointer;
    font-size: 1.0rem;
    line-height: 2.75rem;
    padding: 0 1.5rem 0 1.65rem;
    list-style: none;
    border-radius: 6px;
    letter-spacing: 0.15rem;
    white-space: nowrap;
    font-weight: 700;
  }

  .button-ul {
    justify-content: center;
    background: transparent;
    margin-top: 100px;
  }

  .button-ul .buttons:hover {
    background: grey;
    opacity: 0.4;
    border-color: rgb(3, 77, 146);
  }

  .button-ul .del:hover {
    background: red;
    opacity: 0.4;
    border-color: rgb(3, 77, 146);
  }
</style>