<template>
  <div id="app">
    <router-view/>
    <div id="navigation">
      <router-link :to="{ name: 'HelloWorld' }">Home</router-link>
      <router-link to="/daily">Daily</router-link>
      <router-link to="/work">Work</router-link>
      <router-link to="/essays">Essays</router-link>
      <router-link to="/about">About</router-link>
    </div>
  </div>
</template>

<script>
// What is export default?
export default {
  name: 'App'
}
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navigation").style.bottom = "32px";
  } else {
    document.getElementById("navigation").style.bottom = "-32px";
  }
  prevScrollpos = currentScrollPos;
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
</style>
