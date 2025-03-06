from data.objects import Schedule
from json import load, dump, JSONDecodeError

def loadSchedule(file="data/schedule.json") -> Schedule:

    '''loads a Schedule from a json file'''

    try:
        with open(file, "r") as f:
            userSchedule = Schedule()
            jsondata = load(f) 

            for block, attr in jsondata.items():
                userSchedule.add_block(attr[0], attr[1], attr[2])

        return userSchedule

    except (FileNotFoundError, JSONDecodeError):
        with open(file, "w") as f:
            pass # just creating the file.

        return Schedule()

    # except Exception as err:
    #     print(f"Unexcpected error: {err}")


def dumpSchedule(sched: Schedule, file="data/schedule.json") -> None:
    '''dumps a Schedule into a json file'''

    if len(sched.get_all_blocks()) > 0: # to save time if the list is empty 
        
        dictSched = dict()

        for i, block in enumerate(sched.get_all_blocks()):
            dictSched[i] = [block.title, block.description, block.duration]

        with open(file, "w") as f:
            dump(dictSched, f, indent=1)