
<script  lang="ts">
import axios from 'axios';

export default{
     data(){
          return  {
               categorie:{
                    libelle:"",
                    description:""
               },
               categories:Array<{libelle:string,description:string}>()
          }
     },
     name: "Categories",
     methods:{
          addCategorie(){
               axios.post("http://127.0.0.1:5000/api/charity/add_cat",this.categorie)
               .then(response=>{
                    console.log("response",response.data);
                    this.categorie={
                         libelle:"",
                         description:""
                    }
                    
               }).catch((error)=>{console.log(error)})

          },
          listCategorie(){
               axios.get("http://127.0.0.1:5000/api/charity/list_cat")
               .then(response=>{
                    this.categories=response.data;
                    console.log("response",response.data);
               }).catch((error)=>{console.log(error)})

          }
     }
}



</script>

<template>
     <h1>Categorie work</h1>
     <div class="d-flex justify-content-center ">
       <form class="w-25" @submit.prevent="addCategorie">
          <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Libelle</label>
          <input type="text" class="form-control" id="exampleInputEmail1" v-model="categorie.libelle"  >
          </div>
          <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Description</label>
          <input type="text" class="form-control" id="exampleInputPassword1" v-model="categorie.description">
          </div>
          <button type="submit" class="btn btn-block btn-primary">Submit</button>
       </form>
      </div>

      

</template>

<style>
</style>