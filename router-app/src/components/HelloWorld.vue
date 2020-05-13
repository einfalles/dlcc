<template>
<canvas id="myCanvas" width="200" height="100">
  Your browser does not support the HTML canvas tag.</canvas>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {}
  },
  mounted () {
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    ctx.beginPath();
    ctx.strokeStyle = 'red';
    ctx.arc(95,50,40,0,2*Math.PI);
    ctx.stroke();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
canvas {
  display: block;
  margin: 128px auto;
}
</style>
