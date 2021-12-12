
<script>
	import Globe from './Globe.svelte';
	import Momo from './Momo.svelte';
	import { onMount } from 'svelte';

	let url = "https://raw.githubusercontent.com/cankadir/GlobalNews/main/DATA/NYT_Climate.json";

	//Load Data
	let data;
	onMount(async () => {
		const res = await fetch( url );
		let data_lots = await res.json();
		data = data_lots;
	});

</script>

<svelte:head>
	<link rel="stylesheet" href="https://miniature.earth/demo/photo-locations/style.css">
	<script src="https://miniature.earth/miniature.earth.js"></script>
</svelte:head>


{#if data}
	<Globe {data}/>
{:else}
	<p> Please Wait...</p>
{/if}

