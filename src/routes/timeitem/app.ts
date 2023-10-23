export interface Schedule {
  id: number,
  title?: string,
  attachments?: {
    'id': number,
    'name': string,
    'url': string,
    'ext': string,
    'preview': string,
  }[],
  comments?: number[],
  external?: string,
  archived?: boolean,
  deleted?: boolean,
  status?: string,
  links?: string[],
  author?: number,
  created_date?: Date,
  updated_date?: Date,
  users?: number[],
  checklists?: {
    id: number,
    title: string,
    finished: boolean,
  }[],
  important?: boolean,
  accent_color?: string,
  accentColor?: string,
  startTime?: Date,
  endTime?: Date,
  expandable?: boolean,
  expandImage?: string,
  dueDate?: Date,
}

export function increase_brightness(hex: string, percent: number): string {
  hex = hex.replace(/^\s*#|\s*$/g, '');

  if(hex.length == 3){
      hex = hex.replace(/(.)/g, '$1$1');
  }

  const r = parseInt(hex.substr(0, 2), 16),
      g = parseInt(hex.substr(2, 2), 16),
      b = parseInt(hex.substr(4, 2), 16);

  return '#' +
     ((0|(1<<8) + r + (256 - r) * percent / 100).toString(16)).substr(1) +
     ((0|(1<<8) + g + (256 - g) * percent / 100).toString(16)).substr(1) +
     ((0|(1<<8) + b + (256 - b) * percent / 100).toString(16)).substr(1);
}