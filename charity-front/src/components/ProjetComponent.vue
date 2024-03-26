<script setup lang="ts">

import axios from 'axios';
import { ref } from 'vue';

const apiData = ref<any>([]);

// Fonction pour récupérer les données depuis votre API Flask
const fetchData = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/api/charity/projet');
    apiData.value = response.data; // Stocker les données dans la variable réactive
  } catch (error) {
    console.error('Erreur lors de la récupération des données:', error);
  }
};

function getUrlImage(image:any){
  return "http://127.0.0.1:5000/charity/static/charity_img/"+image
     
};

fetchData();

</script>

<template>

   <h1>Projet works</h1>


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

</template>

<style>

</style>