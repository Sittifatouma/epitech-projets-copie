<template>
  <div class="article_box">
      <h1>{{title}}</h1>
      <div class="article_content">
          <div v-for="article in articles" :key="article.id" class="article">
            <div class="article_text">
              <h2 class="title">{{article.title}}</h2>
              <p class="text">{{article.message}}</p>
            </div>
            <img src="../../assets/taureau.png">
          </div>
      </div>
  </div>
</template>

<script>
export default {
    props: ['title'],
    data: function () {
    return {
      articles: [
        {id:1, title:'Titre 1', message:"Laboris pariatur voluptate non tempor. Quis enim est quis cupidatat incididunt sunt non. Duis anim culpa proident qui adipisicing proident mollit cupidatat consectetur proident excepteur pariatur. Deserunt reprehenderit et id nulla voluptate excepteur qui consectetur. Pariatur amet cupidatat duis exercitation fugiat ullamco incididunt. Cillum minim non dolore elit esse elit non cillum elit cillum eiusmod nisi do voluptate. Aliquip anim nostrud id ad. Nostrud nisi do ad do quis pariatur magna aute velit eu elit ad qui. Adipisicing excepteur ipsum deserunt labore elit voluptate enim id laboris quis anim officia dolore commodo. Officia magna et in magna culpa ullamco."},
        {id:2, title:'Titre 2', message:"Ipsum qui fugiat magna nostrud deserunt. In ad aute consectetur aliqua eu anim ullamco incididunt culpa. Enim enim et non aute. Consectetur occaecat laboris non enim laborum occaecat proident ea ipsum do cillum fugiat excepteur. Officia duis do et dolore exercitation sit minim mollit. Tempor et anim esse exercitation eu excepteur ut dolor deserunt non."},
        {id:3, title:'Titre 3', message:"Ipsum qui fugiat magna nostrud deserunt. In ad aute consectetur aliqua eu anim ullamco incididunt culpa. Enim enim et non aute. Consectetur occaecat laboris non enim laborum occaecat proident ea ipsum do cillum fugiat excepteur. Officia duis do et dolore exercitation sit minim mollit. Tempor et anim esse exercitation eu excepteur ut dolor deserunt non."},
        {id:4, title:'Titre 2', message:"Ipsum qui fugiat magna nostrud deserunt. In ad aute consectetur aliqua eu anim ullamco incididunt culpa. Enim enim et non aute. Consectetur occaecat laboris non enim laborum occaecat proident ea ipsum do cillum fugiat excepteur. Officia duis do et dolore exercitation sit minim mollit. Tempor et anim esse exercitation eu excepteur ut dolor deserunt non."},
        {id:5, title:'Titre 3', message:"Ipsum qui fugiat magna nostrud deserunt. In ad aute consectetur aliqua eu anim ullamco incididunt culpa. Enim enim et non aute. Consectetur occaecat laboris non enim laborum occaecat proident ea ipsum do cillum fugiat excepteur. Officia duis do et dolore exercitation sit minim mollit. Tempor et anim esse exercitation eu excepteur ut dolor deserunt non."}

      ],
    
    }
  },

}
</script>

<style scoped>

.article_box {
  width: 100%;
}


.article_content {
    display: flex;   
    overflow-x: scroll;
    overflow-y: hidden;
    width: 100%;
    margin-top: 20px;
}

.article_content .article {
  flex: 0 0 auto;
  width: 550px;
  height: 200px;
  border: solid thin black;
  display: flex;
  margin-right: 30px;
  padding: 10px;
}

.article_content .article .article_text {
  flex: 3;
  margin-right: 15px;
  display: flex;
  flex-direction: column;
}

.article_content .article .article_text h2 {
  font-size: 30px;
}

.article_content .article .article_text p {
 color: gray;
 text-overflow: ellipsis;
 text-align: justify;
}

.article_content .article img {
  flex: 1;
  height: 150px;
}




</style>