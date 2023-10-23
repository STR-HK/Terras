<script lang="ts" context='module'>
	

    export let selected_date = new Date('2023-10-16');

    // setInterval(() => {
    //     // add 1 day to selected_date
    //     selected_date.setDate(selected_date.getDate() + 1);
    // }, 1000);

    let selected_year = selected_date.getFullYear();
    let selected_month = selected_date.getMonth() + 1;
</script>

<div class="flex justify-between">
    <!-- <button class="flex text-lg" style="transition: all 0.05s ease-in-out;">
        <div class="font-semibold">
            May,
        </div>
        <div style="width: 0.25rem;"></div>
        <div class="text-neutral-500">
            2023
        </div>
    </button> -->

    <button class="flex items-center text-lg" style="transition: all 0.05s ease-in-out;">
        <div class="font-semibold">
            {selected_year}년
        </div>
        <div style="width: 0.25rem;"></div>
        <div class="text-neutral-500">
            {selected_month}월
        </div>
        <div style="width: 0.65rem;"></div>
        <i class="fa-regular fa-chevron-down text-xs" style="font-weight: 500;
            font-family: 'Font Awesome 5 Pro';"></i>
    </button>

    <div class="bg-black text-white rounded-[9999px] text-2xs 
    flex items-center font-semibold p-0.5 h-fit">
        <button class="flex text-2xs bg-white text-black rounded-[9999px] px-3 py-1"
        style="transition: all 0.05s ease-in-out;">
            <!-- Card -->
            카드
        </button>
        <button class="flex text-2xs bg-black text-white rounded-[9999px] px-3 py-1"
        style="transition: all 0.05s ease-in-out;">
            <!-- Block -->
            블록
        </button>
        <button class="flex text-2xs bg-black text-white rounded-[9999px] px-3 py-1"
        style="transition: all 0.05s ease-in-out;">
            <!-- Table -->
            표
        </button>
    </div>

    <div class="flex flex-row gap-1 items-center">
        <div class="text-2xs text-neutral-500">
            <!-- Show: -->
            보기:
        </div>

        <button class="flex items-center text-2xs bg-[#f5f5f5] border-black border-1 rounded-[9999px] px-3 py-1.5
        hover:bg-[#e6e6e6] active:bg-[#cccccc]"
        style="transition: all 0.05s ease-in-out;">
            <!-- 1 Weeks -->
            1주
            <div class="w-1"></div>

            <i class="fa-regular fa-chevron-down" style="font-weight: 400; 
            font-family: 'Font Awesome 5 Pro';"></i>
        </button>

        <button class="flex items-center text-2xs bg-[#54AEEA] text-white rounded-[9999px]
        px-3 py-1.5"
        style="transition: all 0.05s ease-in-out;">
            <i class="fa-regular fa-link" style="font-weight: 300; 
            font-family: 'Font Awesome 5 Pro';"></i>
            <div class="w-1"></div>
            <!-- Share -->
            공유
        </button>
    </div>
</div>