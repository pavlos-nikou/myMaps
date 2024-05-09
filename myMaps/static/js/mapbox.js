async function getToken() {
  response = await fetch(window.location.href + "key")
  mapboxToken = await response.text()
  return mapboxToken

}

(async () => {
  mapboxToken = await getToken()
  mapboxgl.accessToken = mapboxToken;
  const map = new mapboxgl.Map({
    container: 'map', // Specify the container ID
    style:
      'mapbox://styles/mapbox/streets-v12', // Specify which map style to use
    center: [33.259772, 35.071663], // Specify the starting position
    zoom: 9 // Specify the starting zoom
  });
})()

let userElement = document.getElementById('user-data');
let paths = JSON.parse(userElement.dataset.paths);

console.log('Paths:', paths);