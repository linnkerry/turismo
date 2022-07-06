/*
(function(exports) {
        "use strict";
        function initMap() {
            if(navigator.geolocation){
                navigator.geolocation.getCurrentPosition((position)=>{
                    this.latitude = position.coords.latitude;
                    this.longitude = position.coords.longitude;
                     exports.map = new google.maps.Map(document.getElementById("map"), {
                        center: {
                          lat: this.latitude,
                          lng: this.longitude
                        },
                        zoom: 8
                      });
                });
            }else{
                alert("Tu navegador no soporta geolocalizacion!");
            }
        }
        exports.initMap = initMap;
})((this.window = this.window || {}));*/

 // This example requires the Places library. Include the libraries=places
      // parameter when you first load the API. For example:
      // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
      function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -9.933696, lng: -76.248372},
          zoom: 17
        });
        var defaultBounds = new google.maps.LatLngBounds(
          new google.maps.LatLng(-9.882317, -76.334159),
          new google.maps.LatLng(-9.977334, -76.160785));
        var options = {
          bounds: defaultBounds,
        };

        var card = document.getElementById('pac-card');
        var input = document.getElementById('pac-input');
        var countries = document.getElementById('country-selector');

        map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

        var autocomplete = new google.maps.places.Autocomplete(input, options);

        // Set initial restrict to the greater list of countries.
        autocomplete.setComponentRestrictions(
            {'country': ['pe']});

        // Specify only the data fields that are needed.
        autocomplete.setFields(
            ['address_components', 'geometry', 'icon', 'name']);

        var infowindow = new google.maps.InfoWindow();
        var infowindowContent = document.getElementById('infowindow-content');
        infowindow.setContent(infowindowContent);
        var marker = new google.maps.Marker({
          map: map,
          anchorPoint: new google.maps.Point(0, -29)
        });

        autocomplete.addListener('place_changed', function() {
          infowindow.close();
          marker.setVisible(false);
          var place = autocomplete.getPlace();
          if (!place.geometry) {
            // User entered the name of a Place that was not suggested and
            // pressed the Enter key, or the Place Details request failed.
            window.alert("No details available for input: '" + place.name + "'");
            return;
          }

          // If the place has a geometry, then present it on a map.
          if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
          } else {
            map.setCenter(place.geometry.location);
            map.setZoom(16);  // Why 17? Because it looks good.
          }
          marker.setPosition(place.geometry.location);
          marker.setVisible(true);

          var address = '';
          if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
          }


          console.log(place.geometry.location.lat());
          console.log(place.geometry.location.lng());
          $("#latitude").val(place.geometry.location.lat());
          $("#longitude").val(place.geometry.location.lng());

          infowindowContent.children['place-icon'].src = place.icon;
          infowindowContent.children['place-name'].textContent = place.name;
          infowindowContent.children['place-address'].textContent = address;
          infowindow.open(map, marker);
        });

        // Sets a listener on a given radio button. The radio buttons specify
        // the countries used to restrict the autocomplete search.

        autocomplete.setComponentRestrictions({'country': ['pe']});


      }