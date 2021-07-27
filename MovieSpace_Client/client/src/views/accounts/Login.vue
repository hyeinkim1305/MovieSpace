<template>
  <div class="mx-auto container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <div class="input-group tm-mb-30">
            <input name="username" type="text" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="아이디" v-model="credentials.username">
        </div>
        <div class="input-group tm-mb-30">
            <input name="password" type="password" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="비밀번호" v-model="credentials.password"  @keyup.enter="login(credentials)">
        </div>
        <div class="input-group justify-content-end">
            <input type="button" class="btn btn-primary tm-btn-pad-2" value="Login" @click="login(credentials)">
            <router-link to="/Signup" class="ms-3">
              <input type="button" class="btn btn-primary tm-btn-pad-2" value="Sign up">
            </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import jwt from 'jsonwebtoken'
const secretkey = 'django-insecure-y%n75jhzgb2h#p_rdwc&f6435(=fu7xg%4jmbosw7_hpwrt!h*'

export default {
  name: "Login",
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
      token: '',
      date: '',
      temp: '',
      img: '',
    }
  },
  mounted: function () {

  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    login: async function () {
      await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('isLogin', true)
          this.$router.push({ name: 'Home' })
          this.token = res.data.token
        })
        .catch(err => {
          console.log(err)
          alert('아이디 혹은 비밀번호가 틀렸습니다.')
        })
      const decode = jwt.verify(this.token, secretkey)
      await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${decode.username}`,
        data: {},
        headers: this.setToken()
        })
        .then(res => {
          this.$store.dispatch('getUser', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
/* Login CSS Start */
.tm-contact-left {
    padding-right: 55px;
    display:
}

.form-control {
    font-size: 1.2rem;
    padding: 15px 0;
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

.tm-mb-30 {
    margin-bottom: 30px;
}

.tm-mb-45 {
    margin-bottom: 45px;
}

.tm-btn-pad-2 {
    padding: 10px 38px;
}

.tm-btn-pad-2:hover {
    color: green;
}

.btn {
    font-size: 1.3rem;
    padding: 13px 23px;
    border-radius: 0;
}

.btn-primary {
    background-color: white;
    border: none;
    color: #333;
}

.btn-primary:hover,
.btn-primary:focus {
    color: dark;
    background-color: white;
}

input:focus::placeholder {
  color: grey;
}
/* Login CSS end */
</style>