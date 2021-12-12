<script>

    export let data;
    console.log( data );

	window.addEventListener( "earthjsload", function() {

	myearth = new Earth( 'myearth', {

		location: { lat: 20, lng: 90 },
		light: 'none',		
		mapLandColor : '#a5cb7b',
		mapSeaColor : '#bbe6e9'
		
	} );

	var photos = [
		{ location: { lat: 28.7, lng: 82.6 }, src: 'photo-locations/nepal.jpg' },
		{ location: { lat: -2.9, lng: 38.4 }, src: 'photo-locations/kenya.jpg' },
		{ location: { lat: 64.0, lng: -19.7 }, src: 'photo-locations/iceland.jpg' },
		{ location: { lat: 9.5, lng: 99.9 }, src: 'photo-locations/thailand.jpg' },
		{ location: { lat: -38.6, lng: 143.7 }, src: 'photo-locations/australia.jpg' },
		{ location: { lat: 46.7, lng: 9.8 }, src: 'photo-locations/switzerland.jpg' },
		{ location: { lat: 37.7, lng: -119.5 }, src: 'photo-locations/california.jpg' },
		{ location: { lat: 19.5, lng: -155.6 }, src: 'photo-locations/hawaii.jpg' },
		{ location: { lat: 34.6, lng: 135.4 }, src: 'photo-locations/japan.jpg' },
		{ location: { lat: 24.2, lng: -77.8 }, src: 'photo-locations/caribbean.jpg' },
		{ location: { lat: -13.1, lng: -72.5 }, src: 'photo-locations/peru.jpg' },
	];

	myearth.addEventListener( "ready", function() {
		// add photo overlay
		let photo_overlay = this.addOverlay( {
			content: '<div id="photo"><div id="close-photo" onclick="closePhoto(); event.stopPropagation();"></div></div>',
			visible: false,
			containerScale: 1,
			depthScale: 0.5
		} );	


		// add photo pins
		
		for ( var i=0; i < photos.length; i++ ) {
		
			var marker = this.addMarker( {
			
				mesh : "Marker",
				color: (i % 2 == 0) ? '#3a6a39' : '#6a5739',
				location : photos[i].location,
				scale: 0.01,
				offset: 1.6,
				visible: false,
				transparent: true,
				hotspot: true,
				hotspotRadius : 0.75,
				hotspotHeight : 1.3,						
				
				photo_info: photos[i]
				
			} );
			
			marker.addEventListener('click', openPhoto);
			
			// animate marker
			setTimeout( (function() {
				this.visible = true;
				this.animate( 'scale', 0.9, { duration: 140 } );
				this.animate( 'offset', 0, { duration: 1100, easing: 'bounce' } );
			}).bind(marker), 280 * i );
		}
		
	} );

	// close photo overlay when navigating away
	myearth.addEventListener( "change", function() {
		
		if ( ! current_marker || auto_rotate ) return;
		if ( Earth.getAngle( myearth.location, current_marker.location ) > 45 ) {
			closePhoto();
		}
		
	} );
	} );



	var current_marker, auto_rotate;


	function openPhoto() {

	// close current photo
	if ( current_marker ) {
		
		closePhoto();
		window.setTimeout( openPhoto.bind(this), 120 );
		
		return;
	}

	// rotate earth if needed
	if ( myearth.goTo( this.location, { relativeDuration: 100, approachAngle: 12, end: function(){auto_rotate=false;} } ) ) {
		auto_rotate = true;
	}


	document.getElementById('photo').style.backgroundImage = "url("+ this.photo_info.src +")";

	photo_overlay.location = this.location;
	photo_overlay.visible = true;

	setTimeout( function(){
		document.getElementById('photo').className = 'photo-appear';
	}, 120);

	this.animate( 'scale', 0.001, { duration: 150 } );
	current_marker = this;

	}

	function closePhoto() {

		if ( ! current_marker ) return;

		document.getElementById('photo').className = '';

		setTimeout( (function(){
			document.getElementById('photo').style.backgroundImage = 'none';
			photo_overlay.visible = false;
			this.opacity = 0.7;
			this.animate( 'scale', 1, { duration: 150 } );
		}).bind(current_marker), 100 );

		current_marker = false;

	}
</script>


<div id="wrapper">
    <div id="wrapper-in">
        <div id="myearth"></div>
    </div><!--wrapper-in-->
</div><!--wrapper-->



<style>
	
	#back-link {
		position: fixed;
		top: 0;
		left: 0;
		background: #0d130e;
		padding: 0.5em;
		font-size: 26px;
		z-index: 10000;
		border-right: 1px RGBA(255,255,255,0.5) solid;
		border-bottom: 1px RGBA(255,255,255,0.5) solid;
	}
	#back-link img {
		display: block;
		width: 4em;
		height: auto;
	}
	
	@media (max-width: 1199px) {
		#back-link {
			font-size: 20px;
		}
	}
	@media (max-width: 511px) {
		#back-link {
			font-size: 16px;
		}
	}
	
	#legal-footer-wrap {
		position: relative;
		height: 0;
		z-index: 10002;
		font-family: Arial, sans-serif;
	}
	
	#legal-footer {
		position: absolute;
		bottom: 0.5em;
		right: 0.5em;
	}
	
	#legal-footer a {
		text-decoration: none;
		color: inherit;
		padding: 0 0.5em;
		font-size: 10px;
	}
	
	</style>