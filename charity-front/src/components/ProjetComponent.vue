<script  lang="ts">

import axios from 'axios';
import Swal from 'sweetalert2';
import { ref } from 'vue';

// const apiData = ref<any>([]);

// // Fonction pour récupérer les données depuis votre API Flask
// const fetchData = async () => {
//   try {
//     const response = await axios.get('http://127.0.0.1:5000/api/charity/projet');
//     apiData.value = response.data; // Stocker les données dans la variable réactive
//   } catch (error) {
//     console.error('Erreur lors de la récupération des données:', error);
//   }
// };

// function getUrlImage(image:any){
//   return "http://127.0.0.1:5000/charity/static/charity_img/"+image
     
// };

// fetchData();

export default{
     data(){
          return  {


               editStatus:false,

               projet:{
                    id:0,
                    libelle:"",
                    description:"",
                    image:"",
                    categorie_id:0
               },
               categorie:{
                id:Number,
                libelle:String,
                    description:String,

               },
               categories:Array<{id:Number,libelle:string,description:string}>(),
               projets:Array<{id:Number,libelle:string,description:string,image:string}>()
          }
     },
     name: "projets",
     methods:{
      // selection de l'image 
      onImageChange(event:any){
        this.projet.image=event.target.files[0];
      },

      //liste Categorie 

     async listCategorie(){
               axios.get("http://127.0.0.1:5000/api/charity/list_cat")
               .then(response=>{
                    this.categories=response.data;
                    console.log("response",response.data);
               }).catch((error)=>{console.log(error)})
          },

          // add categories
          addProjet(){
            console.log(this.projet);
            
            const formData= new FormData();
            formData.append('libelle',this.projet.libelle);
            formData.append('description',this.projet.description);
            formData.append('image',this.projet.image);
            formData.append('categorie_id',this.projet.categorie_id.toString());

               axios.post("http://127.0.0.1:5000/api/charity/add_project",formData,{
                headers:{'Content-Type':'multipart/form-data'}
               })
               .then(response=>{
                    console.log("response",response.data);
                    this.projet={
                         id:0,
                      libelle:"",
                    description:"",
                    image:"",
                    categorie_id:0
                    }
                    Swal.fire({
                         text: "Sucess projet add",
                         icon: "success"
                         });
                    this.listProjet();
                    
               }).catch((error)=>{console.log(error)})

          },

          // updateProject 
          updateProject(){
              console.log(" update");
              console.log(this.projet);
              let id=this.projet.id
            
               axios.put("http://127.0.0.1:5000/api/charity/update/projet/"+id,this.projet,{
               })
               .then(response=>{
                    console.log("response",response.data);
                    this.projet={
                         id:0,
                      libelle:"",
                    description:"",
                    image:"",
                    categorie_id:0
                    }
                    this.editStatus=false
                    Swal.fire({
                         text: "Sucess Update projet add",
                         icon: "success"
                         });
                    this.listProjet();
                    
               }).catch((error)=>{console.log(error)})

          },

          // deleteProjet 
          deleteProjet(projet:any){
               Swal.fire({
                    text:'Do you want to delete project !!',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Yes',
                    customClass: {
                    actions: 'my-actions',
                    cancelButton: 'order-1 right-gap',
                    confirmButton: 'order-2',
                    denyButton: 'order-3',
                    },
                    }).then((result) => {
                    if (result.isConfirmed) {

                         // delete request
                         axios.delete("http://127.0.0.1:5000/api/charity/delete/projet/"+projet.id)
                         .then(response=>{
                              console.log("response",response.data);
                              
                              Swal.fire({
                                   text: response.data.message,
                                   icon: "success"
                                   });
                              this.listProjet();
                              
                         }).catch((error)=>{
                              Swal.fire({
                                   text: "Error during delete",
                                   icon: "error"
                                   });
                              console.log(error)})
                    } 
                    })

                },
          // liste of categorie
         async listProjet(){
               axios.get("http://127.0.0.1:5000/api/charity/list_project")
               .then(response=>{
                    this.projets=response.data;
                    console.log("response",response.data);
               }).catch((error)=>{console.log(error)})
          },
          getUrlImage(image:any){
           return "http://127.0.0.1:5000/charity/static/image/"+image
          },

          getProjectToUpdate(updateProject:any){
               this.editStatus=true;
               this.projet.libelle=updateProject.libelle;
               this.projet.description=updateProject.description;
               this.projet.id=updateProject.id;
             
          }
          
          

     },
     mounted() {
         this.listProjet()
         this.listCategorie()
     },
}



</script>

<template>

   <h1>Projet Crud</h1>

<!-- 
<div class="row ">
<div v-for="(item, index) in apiData" :key="index" class="col-md-3">
  <div class="card" style="width: 18rem;">
    <img :src="getUrlImage(item.image)" :alt="item.image" class="image">
    <div class="card-body">      
      <p>{{item.categorie}}</p>
    <h5 class="card-title">{{item.libelle}}</h5>
    <p class="card-text">{{item.description}}</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
   </div>
  </div> 
  </div>
</div>

-->
<!-- add Project -->

     <div class="d-flex justify-content-center ">
       <div class="card f-card">
          <form class="w-100" @submit.prevent="editStatus?updateProject():addProjet()">
          <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Libelle</label>
          <input type="text" class="form-control" id="exampleInputEmail1" v-model="projet.libelle"  >
          </div>
          <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Description</label>
          <input type="text" class="form-control" id="exampleInputPassword1" v-model="projet.description">
          </div>
          <div class="mb-3" v-if="editStatus==false">
          <label for="visuel" class="form-label">Visuel</label>
          <input type="file" class="form-control" @change="onImageChange" id="visuel" accept="image/*">
          </div>
          <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Categorie</label>
          <select  class="form-control" id="exampleInputPassword1" v-model="projet.categorie_id" required>
          <option v-for="(item,index) in categories" :value="item.id">
           {{ item.libelle }}
          </option>
          </select>
          </div>
          <button type="submit" class="btn btn-block btn-primary">{{editStatus ?'edit':'submit'}}</button>
       </form>
       </div>
      </div>

      <br>
      <br>
      
<!--list project -->
<div class="d-flex justify-content-center ">
          <table class="table table-dark table-striped">
               <thead>
               <tr>
                    <th scope="col">#</th>                   
                    <th scope="col">image</th>                   
                    <th scope="col">Libelle</th>
                    <th scope="col">description</th>
                    <th scope="col">actions</th>
               </tr>
               </thead>
               <tbody>
               <tr v-for="(item,index) in projets">
                    <th scope="row">{{ index+1 }}</th>
                    <td><img :src="getUrlImage(item.image)" :alt="item.image" class="image" style="border-radius: 10%; width: 50px; height:50px;"></td>
                    <td>{{ item.libelle }}</td>
                    <td>{{ item.description }}</td>
                    <td>
                         <span><a class="btn btn-warning" v-on:click="getProjectToUpdate(item)">&#9998;</a></span> <span></span> <span></span>
                         <span><a class="btn btn-danger" v-on:click="deleteProjet(item)">&#10006;</a></span>
                    </td>
                    
               </tr>
               
               </tbody>
               </table>

      </div>



</template>

<style>

</style>