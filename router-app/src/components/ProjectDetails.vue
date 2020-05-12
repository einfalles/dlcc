<template>
    <H1>{{ content }}</H1>
</template>

<script>
export default {
  props: {
    projectid: String,
    content: Object
  },
  name: "projdets"
};
</script>