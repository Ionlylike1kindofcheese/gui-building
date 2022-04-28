from functools import partial
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.resizable(False, False)
root.geometry("300x200")

soortKaas = {"Emmenthaler" : ["J", "J", "J"], "Leerdammer" : ["J", "J", "N"], "Pamigiano Reggiano" : ["J", "N", "J"], "Goudse kaas" : ["J", "N", "N"], "Camembert" : ["N", "J", "J"], "Mozzarella" : ["N", "J", "N"], "Bleu de Rochbaron" : ["N", "N", "J"], "Foume d'Ambert" : ["N", "N", "N"]}
vragenList = ["is de kaas geel?", "Zitten er gaten in de kaas?", "is de kaas belachelijk duur?", "Is uw kaas hard als steen?", "Heeft de kaas blauwe schimmels?", "Heeft uw kaas een korst?"]
nextQuestion = {"is de kaas geel?" : [1,4], "Zitten er gaten in de kaas?" : [2,3], "is de kaas belachelijk duur?" : ["Result","Result"], "Is uw kaas hard als steen?" : ["Result","Result"], "Heeft de kaas blauwe schimmels?" : [5,5], "Heeft uw kaas een korst?" : ["Result","Result"]}
questionAnwsers = []


# updates label with progressbar percentage
def update_progress_label():
    return f"Current Progress: {pb['value']}%"


# updates program progressbar
def progress():
    if pb['value'] < 100:
        pb['value'] += 25
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


# creates or recreates yes/no button
def buttonCreation(currentQuestion):
    global yes_button, no_button
    yes_button = tk.Button(root, text="Ja", padx=15)
    yes_button.bind("<Button-1>", lambda e: nextQuest(nextQuestion[currentQuestion][0], "J"))
    yes_button.grid(column=0, row=3)
    no_button = tk.Button(root, text="Nee", padx=15)
    no_button.bind("<Button-1>", lambda e: nextQuest(nextQuestion[currentQuestion][0], "N"))
    no_button.grid(column=1, row=3)


# handles progressbar and decides on next question
def nextQuest(questionIndex, whichButton):
    global quest_label, questionAnwsers
    print(whichButton)
    questionAnwsers.append(whichButton)
    BoolResult = isinstance(questionIndex, int)
    if BoolResult == True:
        progress()
        quest_label.config(text=vragenList[questionIndex])
        buttonAnnihilation(vragenList[questionIndex])
    elif questionIndex == "Result":
        conclusion(questionAnwsers)


# destroys yes/no button
def buttonAnnihilation(savedQuestion):
    global yes_button, no_button
    yes_button.destroy()
    no_button.destroy()
    buttonCreation(savedQuestion)


# gives results of cheese
def conclusion(anwserList):
    print(anwserList)
    for key, value in soortKaas.items():
        if value == anwserList:
            global quest_label, yes_button, no_button
            progress()
            quest_label.config(text=("Uw kaas is " + key))
            yes_button.destroy()
            no_button.destroy()


# progressbar
pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# progress label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# question label
quest_label = tk.Label(root, text=vragenList[0], font=("Helvetica", 15), bg="light gray")
quest_label.grid(column=0, row=2, columnspan=2)

# run program
progress()
buttonCreation(vragenList[0])

root.mainloop()