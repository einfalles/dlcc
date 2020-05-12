<template>
  <div class="foo">
    <h2>{{block.title}}</h2>
  </div>
</template>

<script>
export default {
  props: {
    block: Object
  },
  name: "sub_sub_header"
};
</script>