from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)

prizeDict = {"small" : 6.95, "medium" : 11.50, "large" : 15.50}
ammoutDict = {"small" : 0, "medium" : 0, "large" : 0}
question = 0

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


def buttonPressed():
    global question, quest_label, anwser_entry, prizeLabel
    sizeList = list(ammoutDict.keys())
    ammoutDict[sizeList[question]] = anwser_entry.get()
    question += 1
    progress()
    if question >= 3:
        totaalPrijs = 0
        for ammoutValue, prizeValue in zip(ammoutDict.values(), prizeDict.values()):
            totaalPrijs += (ammoutValue * prizeValue)
        quest_label.config("Uw totaal: " + totaalPrijs)
    else:
        textMessage = ("Hoeveel " + str(sizeList[question]) + " pizza's wilt u hebben?")
        quest_label.config(text=textMessage)
        prizeLabel.config("Prijs (" + str(sizeList[question]) + "): " + str(prizeDict[sizeList[question]]))


# the progressbar itself
pb = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=280)
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# shows percentage of progressbar
value_label = tk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# shows questions for pizza's
quest_label = tk.Label(root, font=("Helvetica", 12), bg="light gray", text=("Hoeveel small pizza's wilt u hebben?"))
quest_label.grid(column=0, row=2, columnspan=2)

# number entry 
anwser_entry = tk.Entry(root, justify="center")
anwser_entry.insert(0, int(0))
anwser_entry.grid(column=0, row=3, columnspan=2)

# comfirm button
anwser_button = tk.Button(root, text="Bevestig", width=7, command=buttonPressed)
anwser_button.grid(column=1, row=3, columnspan=2)

# show prize label
prizeLabel = tk.Label(root, font=("Helvetica", 12), bg="light gray", width=13, text=("Prijs (small): " + str(prizeDict["small"])))
prizeLabel.grid(column=0, row=4, columnspan=2)

# run program
progress()

root.mainloop()

# smallprize = 6.95
# mediumprize = 11.50
# largeprize = 15.50
# smallammout = int(input("Hoeveel kleine pizza's wilt u hebben? "))
# mediumammout = int(input("Hoeveel medium pizza's wilt u hebben? "))
# largeammout = int(input("Hoeveel large pizza's wilt u hebben? "))

# pizzaprijs = (smallprize * smallammout) + (mediumprize * mediumammout) + (largeprize * largeammout)

# print("De prijs voor " + str(smallammout) + " kleine pizza's, " + str(mediumammout) + " medium pizza's en " + str(largeammout) + " large pizza's is in totaal " + str(pizzaprijs) + " euro.")