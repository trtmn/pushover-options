import json

data = {
    "Good Morning!": {
        "retry": "",
        "title": "School Pickup",
        "message": "Good Morning! Just making sure you're awake!"
                   " Message me in discord so I know you're up! 😉",
        "expire": "",  # only for Emergency
        "ttl": "600",
        "priority": "1",
        "sound": ""
    },
    "Headed your way": {
        "retry": "",
        "title": "School Pickup",
        "message": "Headed your way now!",
        "expire": "", # only for Emergency
        "ttl": "600",
        "priority": "1",
        "sound": ""
    },
    "We're Here": {
        "retry": "60",
        "message": "We're Here!",
        "expire": "40", # only for Emergency
        "ttl": "",
        "priority": "2", # This one is set as Emergency Priority
        "title": "URGENT: SCHOOL PICKUP",
        "sound": "alien"
    },
}
pretty_data = json.dumps(data, indent=4)

if __name__ == '__main__':

    #output the pretty json to a file
    with open("data.json", "w") as file:
        file.write(pretty_data)
    print("JSON data written to data.json")