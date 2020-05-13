<template>
  <div class="list">
    <div v-for="essay in data">
        <div id="">
          <img src="https://www.pngkit.com/png/full/2-21021_blue-triangle-neon-lights-png-neon-effect-light.png"/>
          <h2>{{essay.name}}</h2>
          <span>{{essay.content[0].title}}</span>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Essays',
  data () {
    return {
      data: []
    }
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
