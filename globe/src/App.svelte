
<script>
	import Globe from './Globe.svelte';
	import { onMount } from 'svelte';


	let data;
	onMount(async () => {
		const res = await fetch(`https://raw.githubusercontent.com/cankadir/GlobalNews/main/DATA/NYT_Climate.json?token=ALAVRLOU3VEELMLKBZWIWR3BWVLS6`);
		data = await res.json();

		console.log( data )
	});

</script>

<svelte:head>
	<link rel="stylesheet" href="https://miniature.earth/demo/photo-locations/style.css">
	<script src="https://miniature.earth/miniature.earth.js"></script>
</svelte:head>


<body>
	<Globe {data}/>
</body>

