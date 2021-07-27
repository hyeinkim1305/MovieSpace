<template>
  <div class="col text-dark">
    <div class="card h-100">
      <img :src="movieImage" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
    }
  },
  computed: {
    movieImage: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    }
  }
}
</script>

<style>
.card-body > p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}
</style>