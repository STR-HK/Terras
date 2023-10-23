<script lang="ts" context="module">
	import ContextMenu from "./component/ContextMenu.svelte";
	import Dateline from "./widget/dateline.svelte";
	import Searchline from "./widget/searchline.svelte";
	import Testitem from "./widget/testitem.svelte";
	import Titleline from "./widget/titleline.svelte";
	import { example_16 } from "./data/example_16.js";
	import { example_17 } from "./data/example_17.js";
	import { example_18 } from "./data/example_18.js";

	// function fetchAPI(method: string, path: string, data: Object) {
	// 	let url: string = 'http://asphodel.kro.kr:7474' + path
	// 	if (Object.keys(data).length === 0) {
	// 		return fetch(url, {
	// 			method: method,
	// 		}).then(response => response.json())
	// 		.catch(error => console.log(error))
	// 	} else {
	// 		return fetch(url, {
	// 			method: method,
	// 			headers: {
	// 				'Content-Type': 'application/json'
	// 			},
	// 			body: JSON.stringify(data)
	// 		}).then(response => response.json())
	// 		.catch(error => console.log(error))
	// 	}
	// }

	async function getSchedules(year: number, month: number, date: number) {
		if (date == 16) {
			return example_16
		} else if (date == 17) {
			return example_17
		} else if (date == 18) {
			return example_18
		} else if (date == 19) {
			return example_17
		} else if (date == 20) {
			return example_16
		}
	}

</script>


<div class="w-full bg-white p-4 rounded-[0.65rem] overflow-scroll overflow-x-hidden">
	<Titleline></Titleline>
	<div class="h-1.5"></div>
	<Searchline></Searchline>
	<div class="h-4"></div>
	<Dateline></Dateline>
	<div class="h-3"></div>
	
	<div class="flex flex-row gap-3 w-full">
		<div class="px-2 flex flex-col gap-[3rem] text-2xs font-semibold">
			<div style="line-height: 0.5rem">08:00</div>
			<div style="line-height: 0.5rem">09:00</div>
			<div style="line-height: 0.5rem">10:00</div>
			<div style="line-height: 0.5rem">11:00</div>
			<div style="line-height: 0.5rem">12:00</div>

			<div style="line-height: 0.5rem">13:00</div>
			<div style="line-height: 0.5rem">14:00</div>
			<div style="line-height: 0.5rem">15:00</div>
			<div style="line-height: 0.5rem">16:00</div>
			<div style="line-height: 0.5rem">17:00</div>
			<div style="line-height: 0.5rem">18:00</div>

			<div style="line-height: 0.5rem">19:00</div>
			<div style="line-height: 0.5rem">20:00</div>
			<div style="line-height: 0.5rem">21:00</div>
			<div style="line-height: 0.5rem">22:00</div>
			<div style="line-height: 0.5rem">23:00</div>
			<div style="line-height: 0.5rem">00:00</div>
		</div>

		<div class="w-full bg-[#D0D0D0] h-[0.01rem]" style="position: absolute; z-index: -1;"></div>
<!--	-->
		<div class="flex flex-row gap-3 w-full overflow-hidden">
			<div class="w-1/5 overflow-hidden h-full pr-0.5 flex flex-row">
				{#await getSchedules(2023, 9, 16) then schedules}
					{#each schedules as schedule, i}
						<Testitem schedule={schedule} count={i}></Testitem>
					{/each}
				{/await}
			</div>
			<div class="w-1/5 overflow-hidden h-full pr-0.5 flex flex-row">
				{#await getSchedules(2023, 9, 17) then schedules}
					{#each schedules as schedule, i}
						<Testitem schedule={schedule} count={i}></Testitem>
					{/each}
				{/await}
			</div>
			<div class="w-1/5 overflow-hidden h-full pr-0.5 flex flex-row">
				{#await getSchedules(2023, 9, 18) then schedules}
					{#each schedules as schedule, i}
						<Testitem schedule={schedule} count={i}></Testitem>
					{/each}
				{/await}
			</div>
			<div class="w-1/5 overflow-hidden h-full pr-0.5 flex flex-row">
				{#await getSchedules(2023, 9, 19) then schedules}
					{#each schedules as schedule, i}
						<Testitem schedule={schedule} count={i}></Testitem>
					{/each}
				{/await}
			</div>
			<div class="w-1/5 overflow-hidden h-full flex flex-row">
				{#await getSchedules(2023, 9, 20) then schedules}
					{#each schedules as schedule, i}
						<Testitem schedule={schedule} count={i}></Testitem>
					{/each}
				{/await}
			</div>
		</div>
	</div>
</div>

<div class="flex flex-col bg-[#FFF97D] items-center justify-between py-3 rounded-[0.65rem] h-full w-[4rem]">
	<div class="w-[2.1rem] h-[2.1rem] rounded-[9999px]"
		style="background-image: url('profile/profile.jpg'); background-size: cover; background-position: center;"
	></div>

	<div class="w-full p-1.5 flex gap-4 flex-col">
		<button class="flex items-center justify-center w-full p-1.5 rounded-[9999px]">
			<i class="fa-regular fa-chart-pie text-1.5xs text-black " style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>
		<button class="flex items-center justify-center w-full p-1.5 rounded-[9999px]">
			<i class="fa-regular fa-bell text-1.5xs text-black " style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>
		<button class="flex items-center justify-center w-full bg-black p-1.5 rounded-[9999px]">
			<i class="fa-regular fa-calendar text-1.5xs text-[#FFF97D] " style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>
		<button class="flex items-center justify-center w-full p-1.5 rounded-[9999px]">
			<i class="fa-regular fa-folder-open text-1.5xs text-black " style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>
		<button class="flex items-center justify-center w-full p-1.5 rounded-[9999px]">
			<i class="fa-regular fa-gear text-1.5xs text-black " style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>


	</div>

	<div class="w-full">
		<button class="w-full" on:click={function() {alert('logged out')}}>
			<i class="fa-regular fa-arrow-right-from-bracket text-1.5xs text-black" style="font-weight: 900; 
			font-family: 'Font Awesome 5 Pro';"></i>
		</button>
		
	</div>
</div>



<ContextMenu></ContextMenu>