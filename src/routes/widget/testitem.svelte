<script lang="ts">
  import type { Schedule } from "../timeitem/app.js";
  import { download } from "../download.js";
  import { fly } from 'svelte/transition';
  import { increase_brightness } from "../timeitem/app.js";

  export let schedule: Schedule;
  let unit = 3.5 / 60
  export let count: number;
  function subtractTime(
    startHour: number, startMinute: number,
    endHour: number, endMinute:number
  ): number[] {
    let deltaHour = endHour - startHour
    let deltaMinute = endMinute - startMinute
    if (deltaMinute < 0) {
      deltaHour -= 1
      deltaMinute += 60
    }
    return [deltaHour, deltaMinute]
  }
  export let startTime: Date = new Date(2023, 9, 16, 10, 30, 0, 0);
  export let endTime: Date = new Date(2023, 9, 16, 12, 30, 0, 0);

  export let title: string;
  export let accentColor: string;
  export let attachments: Schedule['attachments'] = [];
  let download_clickeds = [false]
  let download_clickonces = [false]

  export let checklists: Schedule['checklists'] = [];
  let checklists_clickeds = [false]
  let checklists_finished_count = 0

  let expandable: boolean = false;
  let expandImage = 'grid_isometric.png';

  let dueDate: Date;

  if (schedule) {
    if (schedule?.startTime) {
      startTime = schedule?.startTime;
    }
    if (schedule?.endTime) {
      endTime = schedule?.endTime;
    }

    if (schedule?.title) {
      title = schedule?.title;
    }
    if (schedule?.accentColor) {
      accentColor = schedule?.accentColor;
    }
    if (schedule?.attachments) {
      attachments = schedule?.attachments
    }
    if (schedule?.checklists) {
      checklists = schedule?.checklists
      checklists.forEach(checkitem => {
        if (checkitem.finished) {
          checklists_clickeds.push(true)
          checklists_finished_count += 1
        } else {
          checklists_clickeds.push(false)
        }
      })
    }

    if (schedule?.expandable) {
      expandable = schedule?.expandable
    }
    if (schedule?.expandImage) {
      expandImage = schedule?.expandImage
    }

    if (schedule?.dueDate) {
      dueDate = schedule?.dueDate
    }
  }

  let timeDataBeforeStart = subtractTime(8, 0, startTime.getHours(), startTime.getMinutes())
  let timeBeforeStart = timeDataBeforeStart[0] * 60 + timeDataBeforeStart[1]
  let timeDataLength = subtractTime(startTime.getHours(), startTime.getMinutes(), endTime.getHours(), endTime.getMinutes())
  let timeLength = timeDataLength[0] * 60 + timeDataLength[1]

  let show = false;
  let showTimeout: number = 1000 * Math.random();
  setTimeout(() => {
    show = true;
  }, showTimeout);

  export function lessElasticOut(t: number) {
    return Math.sin((-13.0 * (t + 1.0) * Math.PI) / 2) * Math.pow(2.0, -20.0 * t) + 1.0;
  }

</script>

{#if show}

  <div
    transition:fly={{duration: 2500, easing: lessElasticOut, y: 150}}
    class="rounded-[1.5rem] w-full h-full flex flex-col justify-end relative"
    style="{expandable ? 'background-image: url(' + expandImage +'); ' +
     'background-size: 100%; background-position: top; background-repeat: repeat;' : ''}
     height: {timeLength * unit}rem; left: {-100*count}%; top: {timeBeforeStart * unit}rem; min-width: 100%;"
  >
    <div class="h-auto"></div>
    <div class="rounded-[1.5rem] min-w-full {expandable ? 'h-fit' : 'h-full'}
    overflow-hidden relative flex flex-col gap-3 py-4" style="background-color: {accentColor};">

      <div class="flex flex-row justify-between px-4">
        <div>
          <div class="text-1.5xs font-semibold">
            {title}
          </div>
          <div class="text-2xs">{
            new Intl.DateTimeFormat('ko-KR', {
              hour: 'numeric', minute: 'numeric', hour12: false
            }).format(startTime)
          } - {
            new Intl.DateTimeFormat('ko-KR', {
              hour: 'numeric', minute: 'numeric', hour12: false
            }).format(endTime)
          }</div>
        </div>
        <div>
          <button class="aspect-sqaure">
            <i class="fa-regular fa-ellipsis text-xl"
               style="font-weight: 300; font-family: 'Font Awesome 5 Pro';"
            ></i>
          </button>
        </div>
      </div>

      {#if attachments}
        <div>
          {#each attachments as attachment, i}
            <div class="px-1 py-0.5">
              <button on:click={() => {
								download_clickeds[i] = true;
								download(attachment.toString(), attachment.url)
								setTimeout(() => {
									download_clickonces[i] = true;
									download_clickeds[i] = false;
								}, 400);
							}} class="bg-white rounded-[1rem] p-3 w-full">
                <div class="flex flex-row items-center justify-between">
                  <div class="flex flex-row items-center" style="max-width: calc(100% - 1.5rem); overflow: hidden;">
                    <div class="bg-white aspect-square w-6"
                         style="position: relative;
                         background-image: url({attachment.preview});
                         background-size: 110%;
										     background-position: center;
										     background-repeat: no-repeat;
                    "></div>
                    <div class="w-0.5"></div>
                    <div class="text-1.5xs font-semibold">
                      {attachment.name}
                    </div>
                    <div class="text-1.5xs">.{attachment.ext}</div>
                  </div>
                  {#if !download_clickeds[i]}
                    <div transition:fly={{y: 10}} class="aspect-square">
                      {#if !download_clickonces[i]}
                        <i class="fa-regular fa-cloud-arrow-down text-xs" style="font-weight: 400; font-family: 'Font Awesome 5 Pro';"></i>
                      {:else}
                        <i class="fa-regular fa-check text-xs" style="font-weight: 400;font-family: 'Font Awesome 5 Pro';"></i>
                      {/if}
                    </div>
                  {/if}
                </div>
              </button>
            </div>
          {/each}
        </div>
      {/if}

      {#if checklists && checklists.length > 0}
        <div class="flex flex-col gap-1 px-4">
          <div class="flex flex-row gap-0.5">
            <div class="text-2xs">
              진행 상황:
            </div>
            <div class="text-2xs font-semibold">
              {checklists_finished_count}/{checklists.length}
            </div>
          </div>
          <div class=" h-2.5 rounded-[9999px]" style="background-color: {increase_brightness(accentColor, -40)}">
            <div class="bg-black h-full rounded-[9999px]" style="width: {checklists_finished_count/checklists.length*100}%">

            </div>
          </div>
          <div class="flex flex-row justify-between items-center">
            <div class="flex flex-row gap-0.5 items-center">
              <i class="fa-regular fa-calendar text-2xs" style="font-weight: 300;
      							font-family: 'Font Awesome 5 Pro';"></i>
              <div class="w-[0.01rem]"></div>
              <div class="text-2xs">
                Due Date:
              </div>
              <div class="text-2xs font-semibold">
                {new Intl.DateTimeFormat('ko-KR', {
                  day: 'numeric', month: 'short',
                }).format(dueDate)}
              </div>
            </div>
            <i class="fa-regular fa-triangle-exclamation text-2.5xs" style="font-weight: 600;
      							font-family: 'Font Awesome 5 Pro';"></i>
          </div>
        </div>

        <div class="flex flex-col gap-0.5 px-4">
          {#each checklists as checkitem, i }
            <button on:click={() => {
              checklists_clickeds[i] = !checklists_clickeds[i];
              if (checklists_clickeds[i]) {
                checklists_finished_count += 1
              } else {
                checklists_finished_count -= 1
              }
            }}>
              <div class="flex flex-row items-center gap-1">
                <div class="rounded-sm w-2 h-2
                flex items-center justify-center {checklists_clickeds[i] ? 'bg-black' : ''}"
                     style="border: solid 1px black;">
                  <i class="fa-regular fa-check text-3xs" style="font-weight: 700;
                        {checklists_clickeds[i] ? 'color: ' + accentColor + ';' : 'color: transparent;'}
      							font-family: 'Font Awesome 5 Pro';"></i>
                </div>
                <div class="text-2xs font-semibold {checklists_clickeds[i] ? 'line-through' : ''}">
                  {checkitem.title}
                </div>
              </div>
            </button>
          {/each}
        </div>
        {/if}

    </div>
  </div>

{/if}