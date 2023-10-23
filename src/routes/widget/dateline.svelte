<script lang="ts">
	import { selected_date } from "./titleline.svelte";

    let first_date = selected_date.getDate() - selected_date.getDay() + 1;
    let second_date = first_date + 1;
    let third_date = first_date + 2;
    let fourth_date = first_date + 3;
    let fifth_date = first_date + 4;

    let today = selected_date.getDate();

</script>

<div class="flex flex-row gap-3">
    <div class="px-2 w-fit">
        <div class="text-2xs text-red font-semibold select-none">00:00</div>
    </div>

    <div class="flex flex-row justify-around w-full">


        <div class="flex items-baseline {(today !== first_date) ? 'text-[#D0D0D0]' : ''}">
        <div class="font-bold text-3xl">
        {first_date}
    </div>
        <div class="text-2xs font-semibold">/</div>
        <div class="w-0.5"></div>
        <div class="text-2xs font-semibold">
            <!-- Mon -->
            월
        </div>
    </div>

    <div class="flex items-baseline {today !== second_date ? 'text-[#D0D0D0]' : ''}">
        <div class="font-bold text-3xl">
    {second_date}
</div>
    <div class="text-2xs font-semibold">/</div>
    <div class="w-0.5"></div>
    <div class="text-2xs font-semibold">
        <!-- Tue -->
        화
    </div>
</div>

<div class="flex items-baseline {today !== third_date ? 'text-[#D0D0D0]' : ''}">
        <div class="font-bold text-3xl">
    {third_date}
</div>
<div class="text-2xs font-semibold">/</div>
<div class="w-0.5"></div>
<div class="text-2xs font-semibold">
    <!-- Wed -->
    수
</div>
</div>

<div class="flex items-baseline {today !== fourth_date ? 'text-[#D0D0D0]' : ''}">
        <div class="font-bold text-3xl">
    {fourth_date}
</div>
<div class="text-2xs font-semibold">/</div>
<div class="w-0.5"></div>
<div class="text-2xs font-semibold">
    <!-- Thu -->
    목
</div>
</div>

<div class="flex items-baseline {today !== fifth_date ? 'text-[#D0D0D0]' : ''}">
        <div class="font-bold text-3xl">
    {fifth_date}
</div>
<div class="text-2xs font-semibold">/</div>
<div class="w-0.5"></div>
<div class="text-2xs font-semibold">
    <!-- Fri -->
    금
</div>
</div>
</div>
</div>