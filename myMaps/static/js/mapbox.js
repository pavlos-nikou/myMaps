async function getToken() {
  response = await fetch(window.location.href + "key")
  mapboxToken = await response.text()
  return mapboxToken
}

async function getDirections(path, modeOfTransport = "driving",) {
  url = window.location.href + `directions/${modeOfTransport}/${path.startPoint.long},${path.startPoint.lat};${path.endPoint.long},${path.endPoint.lat}`
  response = await fetch(url)
  response = await response.text()
  return JSON.parse(response)
}

drawRoute = (map, coordinates) => {
  if (map.getLayer("route")) {
    map.removeLayer('route');
    map.removeSource('route');
  }
  // console.log(coordinates);
  map.addLayer({
    id: 'route',
    type: 'line',
    source: {
      type: 'geojson',
      data: {
        type: 'Feature',
        properties: {},
        geometry: {
          type: 'LineString',
          coordinates: coordinates
        }
      }
    },
    layout: {
      'line-join': 'round',
      'line-cap': 'round'
    },
    paint: {
      'line-color': '#FF0000', // Route color
      'line-width': 3 // Route width
    }
  });
}


// initiate map
let map;

(async () => {
  mapboxToken = await getToken()
  mapboxgl.accessToken = mapboxToken;
  map = new mapboxgl.Map({
    container: 'map', // Specify the container ID
    style:
      'mapbox://styles/mapbox/streets-v12', // Specify which map style to use
    center: [33.259772, 35.071663], // Specify the starting position
    zoom: 9 // Specify the starting zoom
  });
  // let userElement = document.getElementById('user-data')
  // let routes = JSON.parse(userElement.dataset.routes)
  // console.log(routes);
  // let route = await getDirections(routes[0])
  // drawRoute(map, route.routes[0].geometry.coordinates)
})()


// expand routes
const routesWindow = document.querySelector(".routes")
const routesExpandButton = document.querySelector(".iconcontainer")
const routesCloseButton = document.querySelector(".close_button_container")
const routesContainer = document.querySelector(".route_container")

routesExpandButton.addEventListener("click", e => {
  routesWindow.classList.add("expand_1")
  routesExpandButton.classList.add("hidden")
  routesContainer.classList.remove("hidden")
  routesCloseButton.classList.remove("hidden")
})

routesCloseButton.addEventListener("click", e => {
  routesWindow.classList.remove("expand_1")
  routesExpandButton.classList.remove("hidden")
  routesContainer.classList.add("hidden")
  routesCloseButton.classList.add("hidden")
})


// show routes when pressed
const showRouteButtons = document.querySelectorAll(".route")
let userElement = document.getElementById('user-data')
let routes = JSON.parse(userElement.dataset.routes)

showRouteButtons.forEach(showRouteButton => {
  showRouteButton.addEventListener("click", async (e) => {
    let routeName = showRouteButton.dataset.routename
    showRouteButtons.forEach(button => {
      console.log(button);
      button.style.backgroundColor = "#457b9d"
    });
    showRouteButton.style.backgroundColor = "#1d3557"
    routes.forEach(async route => {
      if (route.routeName == routeName) {
        let routeDirections = await getDirections(route)
        drawRoute(map, routeDirections.routes[0].geometry.coordinates)
      }
    })
  })
});


//create routes

function addCoordinates(longLat, latInput, longInput) {
  if (enableClickStart || enableClickEnd) {
    latInput.value = longLat.lat
    longInput.value = longLat.lng
  }

}

const pinButtons = document.querySelectorAll(".location_pin_button")
console.log(pinButtons);
let startPinButton = pinButtons[0]
let endPinButton = pinButtons[1]

let enableClickStart;
startPinButton.addEventListener("click", () => {
  enableClickStart = true
  let latInput = document.querySelector("#start_lat")
  let longInput = document.querySelector("#start_long")
  map.on("click", e => {
    let longLat = e.lngLat
    if (enableClickStart) {
      latInput.value = longLat.lat
      longInput.value = longLat.lng
    }
    enableClickStart = false
  })
})
let enableClickEnd;
endPinButton.addEventListener("click", () => {
  enableClickEnd = true
  let latInput = document.querySelector("#end_lat")
  let longInput = document.querySelector("#end_long")
  map.on("click", e => {
    let longLat = e.lngLat
    if (enableClickEnd) {
      latInput.value = longLat.lat
      longInput.value = longLat.lng
    }
    enableClickEnd = false
  })
})