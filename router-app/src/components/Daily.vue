<template>
  <div class="list">
    <!-- <div v-for="daily in data">
        <div id="">
          <img width="100px" src="https://cdn.dribbble.com/users/6051/screenshots/11403377/media/56bd45b32c72a233f18572467c58e7d5.png"/>
          <h2>{{daily.name}}</h2>
          <span>{{daily.description}}</span>
        </div>
    </div> -->
    <masonry
      :cols="6"
      :gutter="30"
      >
      <div v-for="(item, index) in data" :key="index">
        <div class="cell">
          <app-image
            lazy-src="http://via.placeholder.com/350x150"
          />
          <p>{{item.name}}</p>
          <p>{{item.creation_date}}</p>
        </div>
        </div>
    </masonry>
  </div>
</template>

<script>
import AppImage from './AppImage.vue';
import axios from 'axios';
export default {
  name: 'Daily',
  components: {
    AppImage
  },
  data () {
    return {
      data: []
    }
  },
  created () {
    const ax = axios.create({
      baseURL: 'http://localhost:8080/static'
    });
    ax.get('daily.json').then((response)=> {
        this.data = response.data.data;
        console.log(this.data);
    });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  margin-top: 0;
  font-size: 15px;
}
.AppImage {
  width: 100%;
  margin-bottom: 12px;
}
.width {
  width: 10%;
}
.list {
  max-width: 90%;
  margin:0 auto;
}
.cell {
  position: relative;
}
</style>
