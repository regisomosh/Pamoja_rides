document.addEventListener('DOMContentLoaded', function() {
    mapboxgl.accessToken = 'pk.eyJ1IjoiYWNlc2F2dnkiLCJhIjoiY2x0dWcwdG9uMWFkYTJpdWxtYjdyYzN2dyJ9.XMJlWnkwkPEnHWX6mh_XwQ';
    const map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v11',
        center: [36.8219, 1.2921],
        zoom: 8
    });

    let start = null;
    let destination = null;
    const speedLimitKmPerHour = 80; // Custom speed limit in km/hr




    


map.on('click', function(event) {
const lng = event.lngLat.lng;
const lat = event.lngLat.lat;

// Reverse geocode the clicked coordinates to obtain the location name
fetch(`https://api.mapbox.com/geocoding/v5/mapbox.places/${lng},${lat}.json?access_token=${mapboxgl.accessToken}`)
    .then(response => response.json())
    .then(data => {
        const locationName = data.features[0].place_name;

        // Display the location name in the input form
        if (!startPointSelected()) {
            document.getElementById('startPoint').value = locationName;
        } else if (!destinationSelected()) {
            document.getElementById('destination').value = locationName;
        }
    })
    .catch(error => {
        console.error('Error fetching location:', error);
    });
});

// Check if the start point is selected
function startPointSelected() {
return !!document.getElementById('startPoint').value;
}

// Check if the destination is selected
function destinationSelected() {
return !!document.getElementById('destination').value;
}












    map.on('click', function(event) {
        const lng = event.lngLat.lng;
        const lat = event.lngLat.lat;

        if (!start) {
            start = [lng, lat];
            console.log('Start:', start);
        } else if (!destination) {
            destination = [lng, lat];
            console.log('Destination:', destination);

            const url = `https://api.mapbox.com/directions/v5/mapbox/driving/${start[0]},${start[1]};${destination[0]},${destination[1]}?geometries=geojson&access_token=${mapboxgl.accessToken}`;

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    const distance = data.routes[0].distance; // Distance in meters
                    const timeInSeconds = distance / (speedLimitKmPerHour * 1000 / 3600); // Time in seconds
                    
                    const routeCoordinates = data.routes[0].geometry.coordinates;

                    if (map.getSource('route')) {
                        map.getSource('route').setData({
                            'type': 'Feature',
                            'properties': {},
                            'geometry': {
                                'type': 'LineString',
                                'coordinates': routeCoordinates
                            }
                        });
                    } else {
                        map.addSource('route', {
                            'type': 'geojson',
                            'data': {
                                'type': 'Feature',
                                'properties': {},
                                'geometry': {
                                    'type': 'LineString',
                                    'coordinates': routeCoordinates
                                }
                            }
                        });

                        map.addLayer({
                            'id': 'route',
                            'type': 'line',
                            'source': 'route',
                            'layout': {
                                'line-join': 'round',
                                'line-cap': 'round'
                            },
                            'paint': {
                                'line-color': '#888',
                                'line-width': 8
                            }
                        });
                    }

                    const instructions = document.getElementById('instructions');
                    const steps = data.routes[0].legs[0].steps;

                    let tripInstructions = '';
                    for (const step of steps) {
                        tripInstructions += `<li>${step.maneuver.instruction}</li>`;
                    }
                    instructions.innerHTML = `<p><strong>Trip duration: ${Math.round(
                        timeInSeconds / 60
                    )} min 🚗 </strong></p><ol>${tripInstructions}</ol>`;
                })
                .catch(error => {
                    console.error('Error fetching route:', error);
                });

            start = null;
            destination = null;
        } else {
            start = [lng, lat];
            console.log('Start:', start);
        }
    });

    map.addControl(new mapboxgl.NavigationControl());
});
