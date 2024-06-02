<script setup lang="ts">

import router from "./router"


</script>

<template>
  
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Charity App</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        
        <li class="nav-item">
          <a class="nav-link" href="#"><router-link to="/categorie">Catégories</router-link></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <router-link to="/projet">Projet</router-link>
          
          </a>
        </li>
        
      </ul>
      
    </div>
  </div>
</nav>

<div class="container" id="app">
 <router-view></router-view>
</div>
</template>

<style>

</style>
