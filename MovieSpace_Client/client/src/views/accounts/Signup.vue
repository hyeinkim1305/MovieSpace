<template>
  <div class="mx-auto container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-5">
        <div class="input-group tm-mb-30">
          <input name="username" type="text" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="아이디" v-model="credentials.username" required>
        </div>
        <div class="input-group tm-mb-30">
          <input name="password" type="password" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="비밀번호" v-model="credentials.password" required>
        </div>
        <div class="input-group tm-mb-30">
          <input name="passwordConfirmation" type="password" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="비밀번호 확인" v-model="credentials.passwordConfirmation" required>
        </div>
        <div class="input-group tm-mb-30">
          <input name="lastname" type="text" class="form-control rounded-0 border-top-0 border-end-0 border-start-0" placeholder="이름" v-model="credentials.last_name" required>
        </div>
        <div class="input tm-mb-30" @click="text">
          <b-form-datepicker id="signup" v-model="credentials.birth" class="form-control rounded-0 border-top-0 border-end-0 border-start-0 text-white"></b-form-datepicker>
        </div>
        <div class="input-group justify-content-end">
          <input type="button" class="btn btn-primary tm-btn-pad-2" value="Send" @click="signup()">
          <router-link to="Login" class="ms-3">
            <input type="button" class="btn btn-primary tm-btn-pad-2" value="Cancel">
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
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        last_name: null,
        birth: null,
      },
      token: '',
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
    // 왜 send 버튼을 누르는데 한번에 이동되지 않고 2번 클릭해야 넘어갈까?
    signup: async function () {
      await axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(async res => {
          await axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
            data: this.credentials,
          })
            .then(res => {
              localStorage.setItem('jwt', res.data.token)
              this.token = res.data.token
              return res
            })
            .catch(err => {
              console.log(err)
            })
            return res
          })
        .then(async res => {
          const decode = jwt.verify(this.token, secretkey)
          console.log(decode)
          await axios({
            method: 'get',
            url: `http://127.0.0.1:8000/accounts/${decode.username}`,
            data: {},
            headers: this.setToken()
            })
            .then(res => {
              this.$store.dispatch('getUser', res.data)
              this.$store.dispatch('isLogin', true)
              this.$router.push({ name: 'Home' })
              console.log(res)
            })
            .catch(err => {
              console.log(err)
            })
            console.log(res)
        })
        .catch(err => {
          console.log(err)
          alert('정보를 모두 입력해주세요.')
        })
        /* jwt obtain 회원가입, 로그인 함께 처리하는 방법 고려 */

    },
    text: function () {
      const label = document.querySelector('#signup__value_')
      label.setAttribute('class', 'form-control text-dark')
    }
  },

}
</script>
<style scoped>
/* Signup CSS Start */
.tm-contact-left {
    padding-right: 55px;
}

.form-control {
    color: white;
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
    color: white;
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

/* Signup CSS end */
</style>