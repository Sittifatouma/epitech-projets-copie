import axios from 'axios';

export const getPlacesData = async (type, sw, ne) => {
  try {
    const {
      data: { data },
    } = await axios.get(
      `https://travel-advisor.p.rapidapi.com/${type}/list-in-boundary`,
      {
        params: {
          bl_latitude: sw.lat,
          tr_latitude: ne.lat,
          bl_longitude: sw.lng,
          tr_longitude: ne.lng,
        },
      
        headers: {
          'X-RapidAPI-Key':
            '6d491c9c48msh30e5abb72a551f4p13e118jsn6e1074011151',
          'X-RapidAPI-Host': 'travel-advisor.p.rapidapi.com',
        },
      }
      
    //  `http://172.27.0.3:8080/activity?bl_latitude=48.856&tr_latitude=2.352&bl_longitude=2.553&tr_longitude=49.857`,
   
 //   `http://172.27.0.3:8080/activity/test`,
 //`http://172.27.0.3:8080/activity/test`, 
 //`http://172.18.0.3:8080/activity?`,
  // {
  //   params: {
  //     bl_latitude: sw.lat,
  //     tr_latitude: ne.lat,
  //     bl_longitude: sw.lng,
  //     tr_longitude: ne.lng,
  //   },
  //   headers: {
  //     'Access-Control-Allow-Origin' : '*'
  //   }
  // }
    
    );
    return data;
  } catch (error) {
    console.log(error);
  }
};
