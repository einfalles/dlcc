<template>
  <div class="list">
    <!-- <div v-for="essay in data">
        <div id="">
          <app-image
            lazy-src="https://www.pngkit.com/png/full/2-21021_blue-triangle-neon-lights-png-neon-effect-light.png"
          />
          <h2>{{essay.name}}</h2>
          <span>{{essay.content[0].title}}</span>
        </div>
    </div> -->
<div v-for="(item, $index) in list" :key="$index">
  <!-- Hacker News item loop -->
</div>
<div infinite-wrapper>
  <!-- set force-use-infinite-wrapper -->
  <infinite-loading force-use-infinite-wrapper></infinite-loading>
</div>
<!-- <infinite-loading @infinite="infiniteHandler"></infinite-loading> -->
  </div>
</template>

<script>
import axios from 'axios';
import AppImage from './AppImage.vue';
import InfiniteLoading from 'vue-infinite-loading';
const api = '//hn.algolia.com/api/v1/search_by_date?tags=story';
export default {
  name: 'Essays',
  components: {
    AppImage,
    InfiniteLoading
  },
  data () {
    return {
      page: 1,
      list: []
    }
  },
  methods: {
      infiniteHandler($state) {
        axios.get(api, {
          params: {
            page: this.page,
          },
        }).then(({ data }) => {
          console.log('this');
          if (data.hits.length) {
            this.page += 1;
            this.list.push(...data.hits);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
      },
    },
  created () {
    const ax = axios.create({
      baseURL: 'http://localhost:8080/static'
    });
    ax.get('essays.json').then((response)=> {
        this.data = response.data.data;
        console.log(this.data);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
