<template>
  <div class="d-flex justify-content-center align-items-center">
    <div class="card mb-3 d-flex justify-content-center align-items-center" style="max-width: 540px;">
      <div class="row g-0">
        <div  class="col-md-4">
          <img :src="imageUrl" alt="Uploaded image" class="img-fluid rounded-start" >
        </div>
        <div class="col-md-8">
          <div class="card-body" v-if="couleurs.length > 0 && face_position && face_position !='Neutral' ">
            <h5 class="card-title">Résultats :</h5>
            <ul class="list-group text-start">
              <li class="list-group-item">Couleur primaire : {{ couleurs[0] }}</li>
              <li class="list-group-item">Couleur secondaire : {{ couleurs[1] }}</li>
              <li class="list-group-item" >Position visage : {{ face_position }}</li>
              <!--li class="list-group-item">Emotions :
                <span v-for="emotion in emotions" :key="emotion">{{ emotion }}</span>
              </li-->
            </ul>
          </div>
          <div class="card-body" v-else-if="couleurs.length > 0 ">
            <h5 class="card-title">Résultats :</h5>
            <ul class="list-group text-start">
              <li class="list-group-item">Couleur primaire : {{ couleurs[0] }}</li>
              <li class="list-group-item">Couleur secondaire : {{ couleurs[1] }}</li>
              <li class="list-group-item" >Position visage : Aucun visage</li>
              <!--li class="list-group-item">Emotions :
                <span v-for="emotion in emotions" :key="emotion">{{ emotion }}</span>
              </li-->
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<!--template>
<div class="d-flex justify-content-center align-items-center">
<div class="card mb-3 d-flex justify-content-center align-items-center" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img :src="imageUrl" alt="Uploaded image" class="img-fluid rounded-start" >
    </div>
    <div class="col-md-8">
      <div class="card-body" v-if="couleurs.length > 0 ">
        <h5 class="card-title">Résultats :</h5>
        <ul  class="list-group text-start"  >
          <li class="list-group-item">Couleur nominal :  {{ couleurs[0] }}
            <span v-for="prediction in predictions" :key="prediction.id"> {{ prediction.value }}</span>
          </li>
          <li class="list-group-item">Couleur secondaire : {{ couleurs[1] }}</li>
          <li class="list-group-item">Prédiction : {{ prediction.genre }}</li>
        </ul>
      </div>
    </div>
  </div>
</div>
</div>
  </div>
</template-->


<script>
export default {
  props: {
    imageUrl: String,
    couleurs: {
    type: Array,
    default: () => []
  },
  emotions: {
    type: Array,
    default: () => []
  },
  prediction: Object,
  face_position : String
  
  }
}
</script>

<style scoped>
.card {
  width: 300px;
  margin-bottom: 20px;
}

.card-img-top {
  max-width: 100%;
  height: auto;
}
</style>
