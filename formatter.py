import json
f = open("save.json")

j = json.loads(f.read())

print(j)

for i in j:
    print(i)
    i["type"] = "quiz"
                 
    i["layout"] = "CLASSIC"
    i["numberOfAnswers"] = 0
    i["questionFormat"] = 0
    i["resources"] = ""
    i["time"] = 20000
    i["video"] = {
        "fullUrl": "",
        "startTime": 0,
        "endTime": 0
    }
    i["pointsMultiplier"] = 1
print(j)

f.close()
w = open("corrected.json", "w")
w.write(json.dumps(j))
w.close()