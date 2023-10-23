<!--<script lang="ts">-->
<!--	import { fly } from 'svelte/transition';-->
<!--	import { download } from '../download.js';-->
<!--	import { increase_brightness } from './app.ts';-->

<!--	let download_clickeds = new Array(1).fill(false);-->
<!--	let download_clickonces = new Array(1).fill(false);-->

<!--	let editmode = true;-->

<!--	function resizeInputOnDynamicContent(node) {-->

<!--		const measuringElement = document.createElement('div');-->
<!--		document.body.appendChild(measuringElement);-->

<!--		/** duplicate the styles of the existing node, but-->
<!--		 remove the measuring element from the viewport. */-->
<!--		function duplicateAndSet() {-->
<!--			const styles = window.getComputedStyle(node);-->
<!--			measuringElement.innerHTML = node.value;-->
<!--			measuringElement.style.fontSize = styles.fontSize;-->
<!--			measuringElement.style.fontFamily = styles.fontFamily;-->
<!--			measuringElement.style.paddingLeft = styles.paddingLeft;-->
<!--			measuringElement.style.paddingRight = styles.paddingRight;-->
<!--			measuringElement.style.boxSizing = 'border-box';-->
<!--			measuringElement.style.border = styles.border;-->
<!--			measuringElement.style.width='max-content';-->
<!--			measuringElement.style.position = 'absolute';-->
<!--			measuringElement.style.top = '0';-->
<!--			measuringElement.style.left = '-9999px';-->
<!--			measuringElement.style.overflow = 'hidden';-->
<!--			measuringElement.style.visibility = 'hidden';-->
<!--			measuringElement.style.whiteSpace = 'pre';-->
<!--			measuringElement.style.height = '0';-->
<!--			node.style.width = measuringElement.getBoundingClientRect().width + 4 + 'px';-->

<!--		}-->

<!--		duplicateAndSet();-->
<!--		/** listen to any style changes */-->
<!--		const observer = new MutationObserver(duplicateAndSet)-->
<!--		observer.observe(node, { attributes: true, childList: true, subtree: true });-->

<!--		node.addEventListener('input', duplicateAndSet);-->
<!--		return {-->
<!--			destroy() {-->
<!--				observer.disconnect(node);-->
<!--				node.removeEventListener('input', duplicateAndSet)-->
<!--			}-->
<!--		}-->
<!--	}-->
<!--</script>-->

<!--{#await scheduleCoreInfo(1) then schedule}-->
<!--	-->
<!--			<div -->
<!--			on:pointerdown={() => {-->

<!--			}}-->
<!--			class="bg-[{schedule.accent_color}] rounded-[1.75rem] h-fit flex flex-col gap-3 py-4"-->
<!--			>-->
<!--				<div class="flex flex-row justify-between px-4">-->
<!--					<div class="flex flex-col">-->
<!--						{#if title}-->
<!--							{#if !editmode}-->
<!--								<div class="text-1.5xs font-semibold">-->
<!--									{title}-->
<!--								</div>-->
<!--							{:else}-->
<!--								<input class="text-1.5xs font-semibold" use:resizeInputOnDynamicContent bind:value={title}>-->
<!--								{/if}-->
<!--						{/if}-->
<!--						{#if schedule.start_date && schedule.end_date}-->
<!--							<div class="text-2xs">{-->
<!--								new Intl.DateTimeFormat('ko-KR', {-->
<!--									hour: 'numeric',-->
<!--									minute: 'numeric',-->
<!--									hour12: false-->
<!--								}).format(schedule.start_date)-->
<!--							} - {-->
<!--								new Intl.DateTimeFormat('ko-KR', {-->
<!--									hour: 'numeric',-->
<!--									minute: 'numeric',-->
<!--									hour12: false-->
<!--								}).format(schedule.end_date)-->
<!--							}</div>-->

<!--						{/if}-->
<!--					</div>-->
<!--					<div>-->
<!--						<i class="fa-regular fa-ellipsis text-xl" style="font-weight: 300;-->
<!--						font-family: 'Font Awesome 5 Pro';" on:click={() => {-->
<!--							editmode = !editmode;-->
<!--						}} ></i>-->
<!--					</div>-->
<!--				</div>-->
<!--	-->
<!--				<div class="flex flex-col px-4">-->
<!--					<div class="flex flex-col gap-1">-->
<!--						<div class="flex flex-row gap-0.5">-->
<!--							<div class="text-2xs">-->
<!--								Completed: -->
<!--							</div>-->
<!--							<div class="text-2xs font-semibold">-->
<!--								2/4 -->
<!--							</div>-->
<!--						</div>-->
<!--						<div class="h-2.5 rounded-[9999px]" style="background-color: {increase_brightness(-->
<!--							schedule.accent_color, 50-->
<!--						)};">-->
<!--							<div class="bg-black h-full rounded-[9999px] w-1/2">-->
<!--		-->
<!--							</div>-->
<!--						</div>-->
<!--						<div class="flex flex-row justify-between items-center">-->
<!--							<div class="flex flex-row gap-0.5 items-center">-->
<!--								<i class="fa-regular fa-calendar text-2xs" style="font-weight: 300; -->
<!--								font-family: 'Font Awesome 5 Pro';"></i>-->
<!--								<div class="w-[0.01rem]"></div>-->
<!--								<div class="text-2xs">-->
<!--									Due Date: -->
<!--								</div>-->
<!--								<div class="text-2xs font-semibold">-->
<!--									31 June-->
<!--								</div>-->
<!--							</div>-->
<!--							<i class="fa-regular fa-triangle-exclamation text-2.5xs" style="font-weight: 600; -->
<!--								font-family: 'Font Awesome 5 Pro';"></i>-->
<!--						</div>-->
<!--					</div>-->
<!--				</div>-->
<!--	-->
<!--				<div class="flex flex-col px-4">-->
<!--					<div class="flex flex-col gap-0.5">-->
<!--						<div class="flex flex-row items-center gap-1">-->
<!--							<div class="rounded-sm w-2 h-2 flex items-center justify-center bg-black" style="border: solid 1px black;">-->
<!--								<i class="fa-regular fa-check text-3xs" style="font-weight: 700; color: {schedule.accent_color};-->
<!--								font-family: 'Font Awesome 5 Pro';"></i>-->
<!--							</div>-->
<!--							<div class="text-2xs font-semibold line-through	">-->
<!--								Wayframes-->
<!--							</div>-->
<!--						</div>-->
<!--						<div class="flex flex-row items-center gap-1">-->
<!--							<div class="rounded-sm w-2 h-2 flex items-center justify-center bg-black" style="border: solid 1px black;">-->
<!--								<i class="fa-regular fa-check text-3xs text-[{schedule.accent_color}]" style="font-weight: 700; color: {schedule.accent_color};-->
<!--								font-family: 'Font Awesome 5 Pro';"></i>-->
<!--							</div>-->
<!--							<div class="text-2xs font-semibold line-through">-->
<!--								Prototpyes-->
<!--							</div>-->
<!--						</div>-->
<!--						<div class="flex flex-row items-center gap-1">-->
<!--							<div class="rounded-sm w-2 h-2 flex items-center justify-center" style="border: solid 1px black;">-->
<!--							</div>-->
<!--							<div class="text-2xs font-semibold">-->
<!--								UI/UX Design-->
<!--							</div>-->
<!--						</div>-->
<!--						<div class="flex flex-row items-center gap-1">-->
<!--							<div class="rounded-sm w-2 h-2 flex items-center justify-center" style="border: solid 1px black;">-->
<!--							</div>-->
<!--							<div class="text-2xs font-semibold">-->
<!--								Design System-->
<!--							</div>-->
<!--						</div>-->
<!--					</div>-->
<!--				</div>-->
<!--				-->
<!--	-->
<!--				<div class="flex flex-col px-4 gap-2">-->
<!--					<div class="flex flex-row items-center justify-between">-->
<!--						<div class="text-2xs">-->
<!--							&lt;!&ndash; Members: &ndash;&gt;-->
<!--							멤버 목록:-->
<!--						</div>-->
<!--						<i class="fa-regular fa-link text-2xs" style="font-weight: 400; -->
<!--						font-family: 'Font Awesome 5 Pro';"></i>-->
<!--					</div>-->
<!--		-->
<!--					<div class="flex flex-row items-center">-->
<!--						<img class="rounded-[9999px] aspect-square w-5" -->
<!--						src="profile/Pfp_001.JPG" alt='Profile'>-->
<!--						<img class="rounded-[9999px] aspect-square w-5" -->
<!--						style="position: relative; left: -0.4rem;"-->
<!--						src="profile/Pfp_002.JPG" alt='Profile'>-->
<!--						<img class="rounded-[9999px] aspect-square w-5" -->
<!--						style="position: relative; left: -0.8rem;"-->
<!--						src="profile/Pfp_003.JPG" alt='Profile'>-->
<!--						<div class="-->
<!--						flex items-center justify-center-->
<!--						rounded-[9999px] aspect-square w-5 text-2xs font-bold" -->
<!--						style="position: relative; left: -0.12rem;">-->
<!--							+3-->
<!--						</div>-->
<!--					</div>-->
<!--		-->
<!--				</div>-->
<!--	-->
<!--				{#if schedule.attachments}-->
<!--					<div>-->
<!--						{#each schedule.attachments as attachment, i }-->
<!--						<div class="px-1 py-0.5">-->
<!--							<button on:click={() => {-->
<!--								download_clickeds[i] = true;-->
<!--								download(-->
<!--									attachment.toString(),-->
<!--								'http://asphodel.kro.kr:5173/font/SFProKRDisplay_regular.woff2')-->
<!--								setTimeout(() => {-->
<!--									download_clickonces[i] = true;-->
<!--									download_clickeds[i] = false;-->
<!--								}, 400);-->
<!--							}} class="bg-white rounded-[1rem] p-3 w-full">-->
<!--								<div class="flex flex-row items-center justify-between">-->
<!--									<div class="flex flex-row items-center">-->
<!--										<div class="bg-white aspect-square w-6" -->
<!--										 style="-->
<!--										 position: relative; -->
<!--										 background-image: url('https://upload.wikimedia.org/wikipedia/commons/3/33/Figma-logo.svg');-->
<!--										 background-size: 50%;-->
<!--										 background-position: center;-->
<!--										 background-repeat: no-repeat;-->
<!--										 "></div>-->
<!--										<div class="text-1.5xs font-semibold">-->
<!--											&lt;!&ndash; Bank App &ndash;&gt;-->
<!--											{attachment}-->
<!--										</div>-->
<!--										<div class="text-1.5xs">.fig</div>-->
<!--									</div>-->
<!--									{#if !download_clickeds[i]}-->
<!--									<div transition:fly={{y: 10}} class="aspect-square">-->
<!--										{#if !download_clickonces[i]}-->
<!--											<i class="fa-regular fa-cloud-arrow-down text-xs" style="font-weight: 400; -->
<!--											font-family: 'Font Awesome 5 Pro';"></i>-->
<!--										{:else}-->
<!--											<i class="fa-regular fa-check text-xs" style="font-weight: 400; -->
<!--											font-family: 'Font Awesome 5 Pro';"></i>-->
<!--										{/if}-->
<!--									</div>-->
<!--									{/if}-->

<!--								</div>-->
<!--							</button>-->
<!--						</div>-->
<!--					{/each}-->
<!--					</div>-->
<!--				{/if}-->
<!--	-->
<!--	-->
<!--				{#if schedule.comments}-->
<!--					<div class="px-4">-->
<!--						{#each schedule.comments as comment}-->
<!--							<div class="flex flex-col gap-1">-->
<!--								<div class="flex flex-row items-center gap-2">-->
<!--									<img class="rounded-[9999px] aspect-square w-5" -->
<!--									src="profile/Pfp_003.JPG" alt='Profile'>-->
<!--									<div class="text-1.5xs font-semibold">-->
<!--										{comment}-->
<!--									</div>-->
<!--								</div>-->
<!--								<div class="text-2xs">-->
<!--									은행 앱의 최종 버전이에요. 꼭 확인해 보세요.-->
<!--								</div>-->
<!--							</div>-->
<!--						{/each}-->
<!--					</div>-->
<!--				{/if}-->
<!--			</div>-->
<!--				-->
<!--			{/await}-->