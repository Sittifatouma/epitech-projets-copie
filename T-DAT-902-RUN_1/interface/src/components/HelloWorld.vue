<template>
  <div>
    <b-navbar variant="faded" type="light"></b-navbar>


 <div class="container text-center marg">
    <div class="row align-items-end">
      <div class="col-2">
      </div>
      <div class="col-8">
        <div class="card text-center">
  <div class="card-header">
    <ul class="nav nav-pills card-header-pills">
      <li class="nav-item">
        <a class="nav-link active" href="#">Bienvenue !</a>
      </li>
    </ul>
    <h2 class="card-title">Description du projet</h2>
  </div>
 
  <div class="card-body">
    <p class="card-text">
      
      Nostradamovies est un projet BigData qui permet de prédire le genre d'un film en se basant sur son affiche. <br>
      Sélectionnez une affiche de film ci-dessous pour connaître son genre.
    </p>

          <ImageDisplay v-if="file" :image-url="imageUrl" :couleurs="couleurs" :face_position="face_position"/>
          <img :src="imageUrl_test" alt="Uploaded image" class="img-fluid rounded-start"  v-if="imageUrl_test">
          <h1 v-if="genre">Genre du film : {{genre}}</h1>

  </div>
</div>
      </div>
      <div class="col-2">
        
              <!--img :src="imageUrl_test" alt="Uploaded image" class="img-fluid rounded-start"  v-if="imageUrl_test"-->

      </div>
   </div>
 </div>



    <div>
      <!--ImageDisplay v-if="file" :image-url="imageUrl"/-->

      <form @submit.prevent="onSubmit">
        <input type="file" @change="onFileSelected"><br><br>
        <button class="btn btn-primary" type="submit">Prédire</button>
      </form>
      
      
    </div>


    
  </div>
</template>

<script>
import ImageDisplay from './ImageDisplay.vue';

export default {
  components: {
    ImageDisplay
  },
  data() {
    return {
      file: null,
      couleurs: [],
      emotions: [],
      prediction : null,
      imageUrl_test : null,
      face_position : null,
      num_faces : null, 
      genre : null,
      i:null
     
    }
  },
  computed: {
    imageUrl() {
      if (!this.file) {
        return null
      }
      return URL.createObjectURL(this.file)
    }
  },
  methods: {
    onFileSelected(event) {
      //genre= null
      this.file = event.target.files[0];
      this.couleurs = [];
      this.emotions = [];
      this.prediction = null;
      this.imageUrl_test = null;
      this.num_faces = null;
      this.genre = null;
    },
    async onSubmit() {
  console.log('Soumission du formulaire');
  
  const formData = new FormData();
  formData.append('file', this.file);
  
  console.log('Données du formulaire :', formData);
  
  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    body: formData
  });
  
  console.log('Réponse de l\'API :', response);
  
  const data = await response.json();
  
  console.log('Données de la réponse :', data);

  //const { image, couleurs } = data.prediction;

  //console.log('Image:', data.prediction.image);
  console.log('Couleurs recuperé:', data.prediction.couleurs);

  //this.imageUrl = data.prediction.image;
  this.imageUrl_test = URL.createObjectURL(new Blob([new Uint8Array(data.prediction.image)])); // Convert the image back to a URL
  this.couleurs = data.prediction.couleurs;
  this.emotions = data.prediction.emotions;  
  this.face_position = data.prediction.face_position; 
  this.genre="";
  //console.log(this.genre)
  for (this.i in data.prediction.genre) {
  
  switch (data.prediction.genre[this.i]) {
    case 'Comedy':
      this.genre += 'Comedy ';
      break;
    case 'Documentary':
      this.genre += 'Documentary ';
      break;
    case 'Horror':
      this.genre += 'Horror ';
      break;
    case 'N/A':
      this.genre += 'N/A ';
      break;
    case 'Short':
      this.genre += 'Short ';
      break;
    case 'Sport':
      this.genre += 'Sport ';
      break;
    case 'Western':
      this.genre += 'Western ';
      break;
    case 'Action_Adventure_Sci-Fi':
      this.genre += 'Action_Adventure_Sci-Fi ';
      break;
    case 'Animation_Family_Fantasy':
      this.genre += 'Animation_Family_Fantasy ';
      break;
    case 'Music_Musical':
      this.genre += 'Music_Musical ';
      break;
    case 'Crime_Mystery_Thriller':
      this.genre += 'Crime_Mystery_Thriller ';
      break;
    case 'Drama_Romance':
      this.genre += 'Drama_Romance ';
      break;
    case 'History_Biography_War':
      this.genre += 'History_Biography_War ';
      break;
    case 'Reality_TV_News':
      this.genre += 'Reality_TV_News ';
      break;
  }
}

    
  //this.genre =  data.prediction.genre;    
  
   
   

  
  this.

  console.log('image recuperé:', this.imageUrl_test)
}

  }
}
</script>

<style scoped>
.marg {
   margin-top: 10px;
   margin-bottom: 10px;
}


</style>