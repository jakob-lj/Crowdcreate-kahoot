import os
import json

questions = []

def save(q):
    string = json.dumps(q)
    f = open("save2.json", "w")
    f.write(string)
    f.close()

for pers in range(4):
    os.system("clear")
    name = input("SKRIV INN DITT NAVN >>> ")
    for spm in range(4):
        print("Working with spm %i" % (spm + 1))
        sss = input("Hva er ditt spørsmål? >>>> ")
        answers = []
        a = input("Hva er rett svar? >>> ")
        answers.append({"answer":a, "correct": True})
        
        for i in range(1, 4):
            w = input("Skriv inn et feil svar %i/3 >>> " % i)
            answers.append({"answer": w, "correct":False})

        questions.append({
                "question": "%s: %s" % (name, sss),
                "choices": answers,
        })

        save(questions)


