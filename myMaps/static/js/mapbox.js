fetch(window.location.href+"key").then(function(response) {
    return response.text();
  }).then(function(mapBoxKey) {
    mapboxgl.accessToken = mapBoxKey;
    console.log(mapBoxKey);
      const map = new mapboxgl.Map({
        container: 'map', // Specify the container ID
        style:
          'mapbox://styles/mapbox/streets-v12', // Specify which map style to use
        center: [-122.42136449, 37.80176523], // Specify the starting position
        zoom: 14.5 // Specify the starting zoom
      });
  }).catch(function(err) {
    console.log('Fetch Error :-S', err);
  });