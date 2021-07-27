<template>
  <div class="table-responsive">
    <b-table 
      id="my-table"
      :items="comments"
      :fields="['id', 'content', 'username', 'created_at', 'etc']"
      :per-page="perPage"
      :current-page="currentPage"
      class="table custom-table"
      small
      style="cursor:default;"
    >
      <template #cell(content)="content">
        {{ content.item.content }}
      </template>
      <template #cell(etc)="row">
        <div v-if="row.item.username === user.username">
          <b-button size="sm" class="mr-2 me-3" @click="row.toggleDetails">
            수정
          </b-button>
          <div @click="deleteComment(row.item)" class="d-inline">
            <b-button size="sm" class="mr-2 btn-danger">
              삭제
            </b-button>
          </div>
        </div>
      </template>
      <template #row-details="row">
        <b-card class="text-start" style="background-color:transparent">
          <input type="text" :value="row.item.content" style="width:85%;">
          <button @click="updateComment(row), row.toggleDetails" class="btn-secondary mx-2">확인</button>
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
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'CommentList',
  data: function () {
    return {
      commentList: [],
      perPage: 10,
      currentPage: 1,
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.article.id}/comment/`,
      data: {},
      headers: this.setToken(),
    })
      .then(res => {
        this.commentList = res.data
        return res
      })
      .then(res => {
        this.$store.dispatch('getComments', res.data)
        return res
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    updateComment: function (comment) {
      const commentHTML = document.querySelector(`#my-table__details_${comment.index}_`)
      const content = commentHTML.firstChild.firstChild.childNodes[2].childNodes[2].value
      const commentInfo = {
				content: content,
				username: comment.item.username,
			}
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${this.article.id}/comment/${comment.item.id}/`,
        data: commentInfo,
        headers: this.setToken(),
      })
        .then(res => {
          this.comments[comment.index].content = content
          return res
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteComment: function (comment) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${this.article.id}/comment/${comment.id}`,
        data: {},
        headers: this.setToken(),
      })
        .then(res => {
          const newComments = this.comments.filter(x => {
            return x != comment
          })
          this.$store.dispatch('getComments', newComments)
          return res
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'article',
      'comments',
      'user',
    ]),
    rows() {
      return this.comments.length
    },
  }
}
</script>

<style>

</style>