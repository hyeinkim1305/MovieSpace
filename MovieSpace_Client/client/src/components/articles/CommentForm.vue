<template>
  <div class="mt-5">
    <hr style="background-color: white; height:5px;">
    <div class="field text-start row">
      <label for="demo-comment" class="text-start fs-3 my-2">댓글 작성</label>
      <textarea @keyup.enter="createComment" name="demo-comment" id="demo-comment" placeholder="내용을 입력해주세요." rows="2" class="mb-5" v-model.trim="content"></textarea>
      <button @click="createComment" class="col-1 buttons" style="height:75px;">작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: '',
      commentList: [],
    }
  },
  computed: {
    ...mapState([
      'user',
      'article',
      'comments'
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
    createComment: function () {
      const commentData = {
        content: this.content,
        username: this.user.username
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.article.id}/comment/`,
        data: commentData,
        headers: this.setToken(),
      })
        .then(res => {
          this.comments.push(res.data)
          this.content = ''
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		background: transparent;
		border: solid 2px rgba(255, 255, 255, 0.25);
		border-radius: 0.25rem;
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 0.75rem;
		text-decoration: none;
		width: 90%;
	}

  textarea:invalid {
    box-shadow: none;
  }

  textarea:focus {
    border-color: #ffe4b4;
  }

  textarea {
		padding: 0.75rem 1rem;
	}

  .buttons:hover {
    background: grey;
    opacity: 0.4;
    border-color: rgb(3, 77, 146);
  }
</style>