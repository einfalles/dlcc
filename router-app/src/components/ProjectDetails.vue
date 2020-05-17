<template>
  
  <div id="base">
    <div v-for="block in content">
      <!-- <component :is="block" :block="block"></component> -->
      {{block}}
    </div>
  </div>
</template>

<script>
import sub_sub_header from './SubSubHeader.vue';
import poo from './Poo.vue';

export default {
  components: {
    sub_sub_header,
    poo
  },
  props: {
    projectid: String,
    content: Array
  },
  name: "projdets"
};
</script>