<template>
  <div class="hello">
    <vue-fuse
      placeholder="Search Books of the Bible"
      :keys="['name']" 
      :list="workList" 
      eventName="results"
    >
    </vue-fuse>
    <button @click="pushModal" >Modal</button>
    <div v-for="work in results">
      <h1>{{ work.name }}</h1>
      <div v-for="content in work.content">
        <!-- {{ content}} -->
        <router-link :to="{ name: 'project', params: { projectid: content._uid, content: content}}">
          <component :is="content.type" :block="content" :key="content._uid"></component>
        </router-link>
        <!-- <router-view></router-view> -->
      </div>
    </div>
    <!-- <router-view></router-view> -->
  </div>
</template>

<script>
import axios from 'axios';
import sub_sub_header from './SubSubHeader.vue';
import poo from './Poo.vue';
export default {
  name: 'Work',
  components: {
    sub_sub_header,
    poo
  },
  data () {
    return {
      showModal: this.$route.meta.showModal,
      results: [],
      workList:[
        {
            "tags": [
                "design"
            ],
            "creation_date": "2020-04-16",
            "name": "Sunsama",
            "_id": "2020-04-16-7bcd3334-598f-4731-8c5c-8d7266959c7c",
            "content": [
                {
                    "_uid": "BUY6Drn9e2",
                    "type": "sub_sub_header",
                    "title": "Heading Size"
                },
                {
                  "_uid": "BUY6Drn9e3",
                    "type": "poo",
                    "title": "This is a description"
                }
            ]
        },
        {
            "tags": [],
            "creation_date": "2020-01-01",
            "name": "Latch",
            "_id": "2020-01-01-0f76e253-6585-43b1-a890-f33c6abfcaed",
            "content": [
                {
                  "_uid": "BUY6Drn9e14",
                    "type": "sub_sub_header",
                    "title": "Heading Size"
                },
                {
                  "_uid": "BUY6Drn9e5",
                    "type": "poo",
                    "title": "This is a description"
                }
            ]
        },
        {
            "tags": [],
            "creation_date": "2020-04-02",
            "name": "BCGDV",
            "_id": "2020-04-02-84ab3091-b0d0-4477-84e8-6cd066c996ea",
            "content": [
                {
                  "_uid": "BUY6Drn9e6",
                    "type": "sub_sub_header",
                    "title": "Heading Size"
                },
                {
                  "_uid": "BUY6Drn9e7",
                    "type": "poo",
                    "title": "This is another description"
                }
            ]
        }
    ]
    }
  },
  methods: {
    pushModal() {
      this.$search('John', this.books, { keys: ['name'] }).then(result => {
        this.results = result
      })
    },
    getWorkData() {
      // axios
      //   .get('./db001.json')
      //   .then(response => (
      //     this.workList.push({'title':'hello'})
      //   ));
      console.log("fuck");
    }
  },
  created () {
    this.$on('results', results => {
      this.results = results
    })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
