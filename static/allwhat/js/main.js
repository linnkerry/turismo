// Mapa Openstreetmap
    var loc = window.location;
 //   var pathName = loc.pathname.substring(0, loc.pathname.lastIndexOf('/') + 1);

  //  console.log(loc.href.substring(0, loc.href.length - ((loc.pathname + loc.search + loc.hash).length - pathName.length)));

	function our_layers(map,options){
	    var coordenadas = [];
		var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
				maxZoom: 18,
				attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
			});
		var OpenTopoMap = L.tileLayer('http://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
			maxZoom: 18,
			attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
		});
		var url = loc.href+"incidence_data/";

		var points = new L.GeoJSON.AJAX(url,{
			pointToLayer: function (feature, latlng) {
			    coordenadas.push(latlng.lat+','+latlng.lng);
                return L.marker(latlng, {
                    icon: L.icon({
                        iconUrl: loc.href+"static/img/alerta.svg",
                        iconSize: [24, 28],
                        iconAnchor: [12, 28],
                        popupAnchor: [0, -25]
                    }),
					title: feature.properties.agente,
                    riseOnHover: true
                });
            },
//			onEachFeature: function(feature,layer){
//				layer.bindPopup(""+feature.properties.typeinsidence+"");
//			}
		});
		//datasets.addTo(map);
		points.addTo(map);

		var baseLayers = {
			"OSM": osm,
			"OpenTopoMap":OpenTopoMap
		}
		var groupedOverlays = {
		  "Layers": {
		    "incidences": points
		  }
		};
		L.control.groupedLayers(baseLayers, groupedOverlays).addTo(map);
		function createButton(label, container) {
		    var btn = L.DomUtil.create('button', '', container);
		    btn.setAttribute('type', 'button');
		    btn.innerHTML = label;
		    return btn;
		}
        console.log(coordenadas);
		addressPoints = addressPoints.map(function (p) { return [p[1], p[0]]; });
        var heat = L.heatLayer(addressPoints).addTo(map);
    }
