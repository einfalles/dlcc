<template>
  <div class="list">
    <div v-for="daily in data">
        <div id="">
          <img width="100px" src="https://cdn.dribbble.com/users/6051/screenshots/11403377/media/56bd45b32c72a233f18572467c58e7d5.png"/>
          <h2>{{daily.name}}</h2>
          <span>{{daily.description}}</span>
        </div>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
export default {
  name: 'Daily',
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
</style>
