<template>
    <p>{{block.title}}</p>
</template>

<script>
export default {
  props: {
    block: Object
  },
  name: "text"
};
</script>