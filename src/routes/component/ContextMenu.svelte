<!-- 
Github @dukenmarga, July 2022
Context Menu is small menu that displayed when user right-click the mouse on browser.
Think of it as a way to show Refresh option on Microsoft Windows when right-click on desktop.
Known bug:
    - If the browser loads the content for the first time, showMenu set to false.
    Hence, we cannot get menu.h and menu.y dimension, since context menu has not been available at DOM.
    The first right click will not shown properly when right-click occurs around the edge (bottom part
    and right part) of the browser.

Inspired from: Context Menu https://svelte.dev/repl/3a33725c3adb4f57b46b597f9dade0c1?version=3.25.0
-->

<script>
	import { fly } from "svelte/transition";

    // pos is cursor position when right click occur
    let pos = { x: 0, y: 0 }
    // menu is dimension (height and width) of context menu
    let menu = { h: 0, y: 0 }
    // browser/window dimension (height and width)
    let browser = { h: 0, y: 0 }
    // showMenu is state of context-menu visibility
    let showMenu = false;
    // to display some text

    function rightClickContextMenu(e){
        showMenu = true
        browser = {
            w: window.innerWidth,
            h: window.innerHeight
        };
        pos = {
            x: e.clientX,
            y: e.clientY
        };
        // If bottom part of context menu will be displayed
        // after right-click, then change the position of the
        // context menu. This position is controlled by `top` and `left`
        // at inline style. 
        // Instead of context menu is displayed from top left of cursor position
        // when right-click occur, it will be displayed from bottom left.
        if (browser.h -  pos.y < menu.h)
            pos.y = pos.y - menu.h
        if (browser.w -  pos.x < menu.w)
            pos.x = pos.x - menu.w
    }
    function onPageClick(e){
        // To make context menu disappear when
        // mouse is clicked outside context menu
        showMenu = false;
    }
    function getContextMenuDimension(node){
        // This function will get context menu dimension
        // when navigation is shown => showMenu = true
        let height = node.offsetHeight
        let width = node.offsetWidth
        menu = {
            h: height,
            w: width
        }
    }
    let menuItems = [
        // {
        //     'text': "Set Reminder",
        //     'class': 'fa-regular fa-bell'
        // },
        // {
        //     'text': "Archieved",
        //     'class': 'fa-regular fa-file-archive'
        // },
        
        {
            'text': 'Change Color',
            'class' : 'fa-regular fa-palette'
        },
        {
            'text': "Deleted",
            'class': 'fa-regular fa-trash-can',
            'destructive': true
        },
    ]

</script>
<svelte:head>
    <!-- You can change icon sets according to your taste. Change `class` value in `menuItems` above to represent your icons. -->
    <!-- <link rel="stylesheet" href="/icon/css/mfglabs_iconset.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</svelte:head>

{#if showMenu}
<div
    transition:fly={{duration: 100}}
    use:getContextMenuDimension 
    style="top: {pos.y}px; left: {pos.x}px; " 
    class="absolute flex bg-[#2E3032] rounded-[0.65rem] flex-col px-0.5 py-1.5"
    >
    {#each menuItems as item}
        <button class="flex flex-row bg-transparent rounded
        hover:bg-[#404244] w-full items-center gap-[5px]
        py-[0.175rem] px-2.5 text-2.5xs {item.destructive ? 'text-[#FB5869]' : 'text-white'}">
            <i class="{item.class} text-2xs" style="font-weight: 300; 
            font-family: 'Font Awesome 5 Pro';"></i>
            {item.text}
        </button>
    {/each}
</div>
{/if}

<svelte:window on:contextmenu|preventDefault={rightClickContextMenu} 
on:click={onPageClick} />

