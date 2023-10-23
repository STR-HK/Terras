import json
from api import app
from datetime import datetime

def set_schedule(id: int, key: str, value: str):
    try:
        f = open(f'schedule_{id}.txt', 'r', encoding='utf-8')
        schedule = json.loads(f.read())
        f.close()
    except:
        raise Exception('Schedule not found')
        

    schedule[key] = value

    f = open(f'schedule_{id}.txt', 'w', encoding='utf-8')
    f.write(json.dumps(schedule, indent=4, sort_keys=True, default=str))
    f.close()

def get_schedule(id: int):
    f = open(f'schedule_{id}.txt', 'r', encoding='utf-8')
    schedule = json.loads(f.read())
    f.close()

    return schedule

def save_schedule(id: int, schedule: dict):
    f = open(f'schedule_{id}.txt', 'w', encoding='utf-8')
    f.write(json.dumps(schedule, indent=4, sort_keys=True, default=str))
    f.close()

#  / ---------------------------------------- /

@app.get("/schedule/info", tags=["schedule-core"])
def get_schedule_info(id: int):
    return get_schedule(id)

@app.post("/schedule/create", tags=["schedule-core"])
def create_schedule(id: int):
    f = open(f'schedule_{id}.txt', 'w')
    f.write(json.dumps({
        'id': id,
    }, indent=4, sort_keys=True, default=str))
    f.close()


@app.post("/schedule/title", tags=["schedule-set"])
def set_schedule_title(id: int, title: str):
    set_schedule(id, 'title', title)

@app.put("/schedule/attachment", tags=["schedule-add"])
def add_schedule_attachment(id: int, attachment_id: int):
    schedule = get_schedule(id)
    
    if 'attachments' not in schedule:
        schedule['attachments'] = []

    schedule['attachments'].append(attachment_id)

    save_schedule(id, schedule)

@app.delete("/schedule/attachment", tags=["schedule-add"])
def remove_schedule_attachment(id: int, attachment_id: int):
    schedule = get_schedule(id)
    
    if 'attachments' not in schedule:
        return

    schedule['attachments'].remove(attachment_id)

    save_schedule(id, schedule)

@app.put("/schedule/comment", tags=["schedule-add"])
def add_schedule_comment(id: int, comment_id: int):
    schedule = get_schedule(id)
    
    if 'comments' not in schedule:
        schedule['comments'] = []

    schedule['comments'].append(comment_id)

    save_schedule(id, schedule)

@app.delete("/schedule/comment", tags=["schedule-add"])
def remove_schedule_comment(id: int, comment_id: int):
    schedule = get_schedule(id)
    
    if 'comments' not in schedule:
        return

    try:
        schedule['comments'].remove(comment_id)
    except:
        raise Exception('Comment not found')

    save_schedule(id, schedule)

@app.post("/schedule/external", tags=["schedule-set"])
def set_schedule_external(id: int, external: str):
    set_schedule(id, 'external', external)

@app.post("/schedule/archived", tags=["schedule-set"])
def set_schedule_archived(id: int, archived: bool):
    set_schedule(id, 'archived', archived)

@app.post("/schedule/deleted", tags=["schedule-set"])
def set_schedule_deleted(id: int, deleted: bool):
    set_schedule(id, 'deleted', deleted)

@app.post("/schedule/status", tags=["schedule-set"])
def set_schedule_status(id: int, status: str):
    set_schedule(id, 'status', status)

@app.put("/schedule/link", tags=["schedule-add"])
def add_schedule_link(id: int, link: str):
    schedule = get_schedule(id)
    
    if 'links' not in schedule:
        schedule['links'] = []

    schedule['links'].append(link)

    save_schedule(id, schedule)

@app.delete("/schedule/link", tags=["schedule-add"])
def remove_schedule_link(id: int, link: str):
    schedule = get_schedule(id)
    
    if 'links' not in schedule:
        return

    schedule['links'].remove(link)

    save_schedule(id, schedule)

@app.post("/schedule/author", tags=["schedule-set"])
def set_schedule_author(id: int, author: str):
    set_schedule(id, 'author', author)

@app.post("/schedule/due_date", tags=["schedule-set"])
def set_schedule_due_date(id: int, due_date: datetime):
    set_schedule(id, 'due_date', due_date)

@app.post("/schedule/created_date", tags=["schedule-set"])
def set_schedule_created_date(id: int, created_date: datetime):
    set_schedule(id, 'created_date', created_date)

@app.post("/schedule/start_date", tags=["schedule-set"])
def set_schedule_start_date(id: int, start_date: datetime):
    set_schedule(id, 'start_date', start_date)

@app.post("/schedule/end_date", tags=["schedule-set"])
def set_schedule_start_date(id: int, start_date: datetime):
    set_schedule(id, 'end_date', start_date)

@app.post("/schedule/updated_date", tags=["schedule-set"])
def set_schedule_updated_date(id: int, updated_date: datetime):
    set_schedule(id, 'updated_date', updated_date)


@app.put("/schedule/user", tags=["schedule-add"])
def add_schedule_user(id: int, user: str):
    schedule = get_schedule(id)
    
    if 'users' not in schedule:
        schedule['users'] = []

    schedule['users'].append(user)

    save_schedule(id, schedule)

@app.delete("/schedule/user", tags=["schedule-add"])
def remove_schedule_user(id: int, user: str):
    schedule = get_schedule(id)
    
    if 'users' not in schedule:
        return

    schedule['users'].remove(user)

    save_schedule(id, schedule)

@app.put("/schedule/checklist", tags=["schedule-add"])
def add_schedule_checklist(id: int, checklist_id: int):
    schedule = get_schedule(id)
    
    if 'checklists' not in schedule:
        schedule['checklists'] = []

    schedule['checklists'].append(checklist_id)

    save_schedule(id, schedule)

@app.delete("/schedule/checklist", tags=["schedule-add"])
def remove_schedule_checklist(id: int, checklist_id: int):
    schedule = get_schedule(id)
    
    if 'checklists' not in schedule:
        return

    schedule['checklists'].remove(checklist_id)

    save_schedule(id, schedule)







@app.post("/schedule/important", tags=["schedule-set"])
def set_schedule_important(id: int, important: bool):
    set_schedule(id, 'important', important)