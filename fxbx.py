#!/bin/python3

from data.objects import Schedule
from json import load, dump, JSONDecodeError


try:
    with open("schedules.json", "r") as file:
        userSchedule = load(file)

except JSONDecodeError:


