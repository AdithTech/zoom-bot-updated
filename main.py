import json
import time
import webbrowser
from datetime import datetime

data = json.loads(open("meeting.json","r").read())

while True:
    for meeting in data['meetings']:
        for schedule in meeting['schedules']:
            now_day = datetime.today()
            if schedule.get("day") != None:
                if now_day.strftime('%A').lower() == schedule['day'].lower() and now_day.strftime("%H:%M:%S") == schedule['time'].lower():
                    webbrowser.open(
                        f"zoommtg://us04web.zoom.us/join?action=join&confno={meeting['meetingId']}&pwd={meeting['meetingPassword']}"
                    )
            if schedule.get("date") != None:
                if now_day.strftime("%Y-%m-%d").lower() == schedule['date'].lower() and now_day.strftime("%H:%M:%S") == schedule['time'].lower():
                    webbrowser.open(
                        f"zoommtg://us04web.zoom.us/join?action=join&confno={meeting['meetingId']}&pwd={meeting['meetingPassword']}"
                    )
    time.sleep(1)
