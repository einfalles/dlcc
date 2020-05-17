<template>
  <div class="list">
    <div v-for="essay in data">
        <router-link :to="{ name: 'essaydets', params: { eid: essay._id, content: essay.content}}">
          <h1>{{ essay.name }}</h1>
        </router-link>
    </div>
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
      data: []
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
input {
  display: none;
}
h1, h2 {
  font-weight: 500;
    -webkit-text-stroke: 1px white;
    -webkit-text-fill-color: transparent;
    font-size: 56px;
    margin-bottom: 16px;
    margin-top: 0;
}
a {
  text-decoration: none;
}
h1:hover {
  -webkit-text-fill-color: white;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
