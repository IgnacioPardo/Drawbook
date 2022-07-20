from IPython.display import IFrame, display, HTML
import random
import string
import pickle

def get_random_string(length, chars=False):
    # choose from all lowercase letter
    letters = string.ascii_lowercase + "1234567890" + ("_-" if chars else "")
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def excalidraw_room_gen():
    return ','.join([get_random_string(20), get_random_string(22, True)])
     
def excalidraw_iframe(room):
    return IFrame(src='https://excalidraw.com/#room=' + room, width=1000, height=600)

def load_drawings(path):
    try:
        with open(path, 'rb') as f:
            data = pickle.load(f)
            return {"path": path, "rooms": data}
    except:
        return {"path": path, "rooms": {}}

def save_drawings(data):
    with open(data["path"], 'wb') as f:
        pickle.dump(data["rooms"], f, pickle.HIGHEST_PROTOCOL)

def _draw(drawings, room):
    if room not in drawings["rooms"]:
        drawings["rooms"][room] = excalidraw_room_gen()
        save_drawings(drawings)
    
    room_id = drawings["rooms"][room]
    display(HTML("<style>@media print {.excalibtn { display: none }}</style><a class='excalibtn' href='https://excalidraw.com/#room=" + room_id + "'><img src='https://img.shields.io/badge/Open%20in-%20Excalidraw-lightgrey'></a>"))
    display(excalidraw_iframe(room_id))
