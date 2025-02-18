import React, {useRef, useState } from 'react'
import { useJsApiLoader, GoogleMap, DirectionsRenderer, Marker } from '@react-google-maps/api';
import { Grid, Card, CardContent, Box } from '@material-ui/core';

import useStyles from './styles';
  const waypoint =  [{
    location: { lat: 48.8584, lng: 2.2945 },
    stopover: true
  }];

const ItineraireCalcul = ({coordinates, nameOrigin, nameDestination}) => {

    const classes = useStyles();

    const { isLoaded } = useJsApiLoader({
        googleMapsApiKey: "AIzaSyAqnvUQXThyd6YuwSocRRKb3NKcvzWw40A",
        libraries: ['places'],
    })

    const [map, setMap] = useState(/** @type google.maps.Map */ (null))
  
    /** @type React.MutableRefObject<HTMLInputElement> */
    const originRef = useRef()
    /** @type React.MutableRefObject<HTMLInputElement> */
    const destiantionRef = useRef()
  
    //TODO :  Faire un boucle pour ajouter n addStop
    /** @type React.MutableRefObject<HTMLInputElement> */
    const addStopRef = useRef()
  
    const [directionsResponse, setDirectionsResponse] = useState(null)
  
    async function calculateRoute() {
      if (originRef.current.value === '' || destiantionRef.current.value === '') {
        return
      }
  
      // eslint-disable-next-line no-undef
      const directionsService = new google.maps.DirectionsService()
  
      const results = await directionsService.route({
        origin: originRef.current.value,     
        destination: destiantionRef.current.value,
        travelMode: window.google.maps.TravelMode.DRIVING,
      })
  
      setDirectionsResponse(results) 
    }
  
    function clearRoute() {
      setDirectionsResponse(null)
      originRef.current.value = ''
      destiantionRef.current.value = ''
    }

    
    if (!isLoaded) {
      return <div data-testid="iti_1" >Attend je charge la page 🏋🏾🏆</div>
    }

console.log(nameDestination)
  return (

    <Grid container spacing={3} style={{ width: '100%' }}>
            <Grid item xs={12} md={4}>
              <Card elevation={4}>
                <CardContent>
                    <Box display="flex" justifyContent="space-between">
                        <label>Origin</label>
                        <input id="originRef" type="text" placeholder="origin" ref={originRef} value={nameOrigin.name} />
                    </Box>

                    <Box display="flex" justifyContent="space-between">
                        <label>Destination</label>
                        <input id="Destination" type="text" placeholder="Destination" ref={destiantionRef} value={nameDestination}/>
                    </Box>

                    <Box display="flex" justifyContent="space-between">
                        <label>Add stop</label>
                        <input id="AddStop" type="text" placeholder="AddStop" ref={addStopRef} />
                    </Box>
                    <Box display="flex" justifyContent="space-between">
                        <button  type="submit" onClick={calculateRoute}>
                            Search
                        </button>
                        <button type="submit" onClick={clearRoute}>
                            Clear
                        </button>
                    </Box>
                </CardContent>
              </Card>
            </Grid>
            <Grid item xs={12} md={8}>
            <div className={classes.mapContainer}>
                <GoogleMap
                    center={coordinates}
                    zoom={15}
                    mapContainerStyle={{ width: '100%', height: '80%' }}
                    options={{
                    zoomControl: false,
                    streetViewControl: false,
                    mapTypeControl: false,
                    fullscreenControl: false,
                    }}
                    onLoad={map => setMap(map)}>
                    <Marker position={coordinates} />
                    {directionsResponse && (
                    <DirectionsRenderer directions={directionsResponse} />
                    )}
                </GoogleMap>
            </div>
        </Grid>
    </Grid>

  )
}

export default ItineraireCalcul;