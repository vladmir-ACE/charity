
<script  lang="ts">
import axios from 'axios';
import Swal from 'sweetalert2';

export default{
     data(){
          return  {
               categorie:{
                    libelle:"",
                    description:""
               },
               categories:Array<{id:Number,libelle:string,description:string}>()
          }
     },
     name: "Categories",
     methods:{
          // add categories
          addCategorie(){
               axios.post("http://127.0.0.1:5000/api/charity/add_cat",this.categorie)
               .then(response=>{
                    console.log("response",response.data);
                    this.categorie={
                         libelle:"",
                         description:""
                    }
                    Swal.fire({
                         text: "Sucess categorie add",
                         icon: "success"
                         });
                    this.listCategorie();
                    
               }).catch((error)=>{console.log(error)})

          },
          // liste of categorie
          listCategorie(){
               axios.get("http://127.0.0.1:5000/api/charity/list_cat")
               .then(response=>{
                    this.categories=response.data;
                    console.log("response",response.data);
               }).catch((error)=>{console.log(error)})
          },

          // update categories 
           async UpdateCategorie(categorie:any){
          const { value: formValues } = await Swal.fire({
          title: "Update categories",
          html: `
          <div class="mb-3">
          
          <input type="text" placeholder="Libelle" class="form-control" id="swal-input1" value="${categorie.libelle}"  >
          </div>
          <div class="mb-3">
          
          <input type="text" placeholder="Description" class="form-control" id="swal-input2" value="${categorie.description}">
          </div>
          `,
          focusConfirm: false,
          preConfirm: () => {
          return [
               document.getElementById("swal-input1").value,
               document.getElementById("swal-input2").value
          ];
          }
          });
          if (formValues) {
               console.log(formValues);
     
           let data={
               libelle:formValues[0],
               description:formValues[1]
           }
             // update request
          axios.put("http://127.0.0.1:5000/api/charity/update/"+categorie.id,data)
               .then(response=>{
                    console.log("response",response.data);
                    
                    Swal.fire({
                         text: response.data.message,
                         icon: "success"
                         });
                    this.listCategorie();
                    
               }).catch((error)=>{
                    Swal.fire({
                         text: "Error during Update",
                         icon: "error"
                         });
                    console.log(error)})
          }},


          // delete function 
          deleteCategorie(cat:any){
               Swal.fire({
                    text:'Do you want to delete product !!',
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
                         axios.delete("http://127.0.0.1:5000/api/charity/delete/"+cat.id)
                         .then(response=>{
                              console.log("response",response.data);
                              
                              Swal.fire({
                                   text: response.data.message,
                                   icon: "success"
                                   });
                              this.listCategorie();
                              
                         }).catch((error)=>{
                              Swal.fire({
                                   text: "Error during delete",
                                   icon: "error"
                                   });
                              console.log(error)})
                    } 
                    })

                }
          
          

     },
     mounted() {
         this.listCategorie()
     },
}



</script>

<template>
     <h1>Categorie work</h1>
     <div class="d-flex justify-content-center ">
       <div class="card f-card">
          <form class="w-100" @submit.prevent="addCategorie">
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
      </div>
      
      <br><br>

      <div class="d-flex justify-content-center ">
          <table class="table table-dark table-striped">
               <thead>
               <tr>
                    <th scope="col">#</th>
                    <th scope="col">Libelle</th>
                    <th scope="col">description</th>
                    <th scope="col">actions</th>
               </tr>
               </thead>
               <tbody>
               <tr v-for="(item,index) in categories">
                    <th scope="row">{{ index+1 }}</th>
                    <td>{{ item.libelle }}</td>
                    <td>{{ item.description }}</td>
                    <td>
                         <span><a class="btn btn-warning" v-on:click="UpdateCategorie(item)">&#9998;</a></span> <span></span> <span></span>
                         <span><a class="btn btn-danger" v-on:click="deleteCategorie(item)">&#10006;</a></span>
                    </td>
                    
               </tr>
               
               </tbody>
               </table>

      </div>
</template>

<style>

.f-card{
     width: 500px;
     padding: 5%;
     border-color: black;

}
</style>