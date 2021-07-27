<template>
  <div class="container">
    <h3 class="major">Update Form</h3>
    <div class="field">
      <label for="demo-title" class="text-start fs-3 my-2">Title</label>
      <input type="text" name="demo-title" id="demo-title" value="" placeholder="제목을 입력해주세요" class="mb-5" v-model.trim="title" />
    </div>
    <div class="field">
      <label for="demo-content" class="text-start fs-3 my-2">Content</label>
      <textarea name="demo-content" id="demo-content" placeholder="내용을 입력해주세요." rows="8" class="mb-5" v-model.trim="content"></textarea>
    </div>
    <div class="fields">
      <div class="field third">
        <label for="demo-hashtag" class="text-start fs-4 my-2">HashTag</label>
        <input type="text" name="demo-hashtag" id="demo-hashtag" placeholder="해시태그" />
      </div>
    </div>
    <ul class="actions button-ul">
      <li><input type="button" value="수정" class="primary color2 buttons" @click="updateArticle" /></li>
      <li><router-link to="articleList"><input type="reset" value="취소" class="buttons" /></router-link></li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'ArticleForm',
  data: function () {
    return {
			title: '',
			content: '',
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
    updateArticle: async function () {
			const articleinfo = {
				title: this.title,
				content: this.content,
				username: this.user.username,
			}
      await axios ({
        method: 'put',
        url: `http://127.0.0.1:8000/community/${this.article.id}/`,
        data: articleinfo,
				headers: this.setToken()
      })
        .then((res) => {
					this.$store.dispatch('getArticle', res.data)
        })
				.then(res => {
          this.$router.push({ name: 'ArticleDetail' })
					console.log(res)
				})
        .catch((err) => {
          console.log(err)
        })
    }
  },
	computed: {
		...mapState([
			'user',
      'article',
		])
	},
	mounted: function () {
		this.title = this.article.title
		this.content = this.article.content
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

	input[type="text"],
	input[type="password"],
	input[type="email"],
	input[type="tel"],
	select,
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
		width: 100%;
	}

		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		input[type="tel"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		input[type="tel"]:focus,
		select:focus,
		textarea:focus {
			border-color: #ffe4b4;
		}

	option {
		background-color: rgba(255, 255, 255, 0.875);
		color: #2e2b37;
	}

	select {
		background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' preserveAspectRatio='none' viewBox='0 0 40 40'%3E%3Cpath d='M9.4,12.3l10.4,10.4l10.4-10.4c0.2-0.2,0.5-0.4,0.9-0.4c0.3,0,0.6,0.1,0.9,0.4l3.3,3.3c0.2,0.2,0.4,0.5,0.4,0.9 c0,0.4-0.1,0.6-0.4,0.9L20.7,31.9c-0.2,0.2-0.5,0.4-0.9,0.4c-0.3,0-0.6-0.1-0.9-0.4L4.3,17.3c-0.2-0.2-0.4-0.5-0.4-0.9 c0-0.4,0.1-0.6,0.4-0.9l3.3-3.3c0.2-0.2,0.5-0.4,0.9-0.4S9.1,12.1,9.4,12.3z' fill='rgba(255, 255, 255, 0.25)' /%3E%3C/svg%3E");
		background-size: 1.25rem;
		background-repeat: no-repeat;
		background-position: calc(100% - 1rem) center;
		height: 2.5rem;
		padding-right: 2.5rem;
		text-overflow: ellipsis;
	}

		select option {
			color: rgba(255, 255, 255, 0.875);
			background: #2e2b37;
		}

		select:focus::-ms-value {
			background-color: transparent;
		}

		select::-ms-expand {
			display: none;
		}

	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.5rem;
	}

	textarea {
		padding: 0.75rem 1rem;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2rem;
		opacity: 0;
		width: 1rem;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			position: relative;
			color: rgba(255, 255, 255, 0.75);
			cursor: pointer;
			display: inline-block;
			font-size: 1rem;
			font-weight: 300;
			margin-bottom: 0;
			padding-left: 2.5rem;
			padding-right: 1rem;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				display: inline-block;
				font-style: normal;
				font-variant: normal;
				text-rendering: auto;
				line-height: 1;
				text-transform: none !important;
				font-family: 'Font Awesome 5 Free';
				font-weight: 900;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				content: '';
				display: inline-block;
				font-size: 0.8rem;
				position: absolute;
				top: 0;
				left: 0;
				width: 1.6875rem;
				height: 1.6875rem;
				line-height: 1.6875rem;
				background: rgba(255, 255, 255, 0.075);
				border: solid 1px rgba(255, 255, 255, 0.25);
				border-radius: 0.25rem;
				color: #2e2b37;
				text-align: center;
			}

				body.is-ie input[type="checkbox"] + label:before, body.is-ie
				input[type="radio"] + label:before {
					line-height: 1.5;
				}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			content: '\f00c';
			background: rgba(255, 255, 255, 0.875);
			border-color: rgba(255, 255, 255, 0.875);
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #ffe4b4;
			box-shadow: 0 0 0 1px #ffe4b4;
		}

		input[type="checkbox"]:focus:checked + label:before,
		input[type="radio"]:focus:checked + label:before {
			background: #ffe4b4;
		}

		input[type="checkbox"].color1 + label:before,
		input[type="radio"].color1 + label:before {
			color: #726193;
		}

		input[type="checkbox"].color2 + label:before,
		input[type="radio"].color2 + label:before {
			color: #e37b7c;
		}

		input[type="checkbox"].color3 + label:before,
		input[type="radio"].color3 + label:before {
			color: #ffe4b4;
		}

		input[type="checkbox"].color4 + label:before,
		input[type="radio"].color4 + label:before {
			color: #353865;
		}

	input[type="checkbox"] + label:before {
		border-radius: 0.25rem;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: rgba(255, 255, 255, 0.5) !important;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: rgba(255, 255, 255, 0.5) !important;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: rgba(255, 255, 255, 0.5) !important;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: rgba(255, 255, 255, 0.5) !important;
		opacity: 1.0;
	}

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
</style>