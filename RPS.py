import tkinter as tk
import random
import os
from PIL import Image, ImageTk
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

root=tk.Tk()
root.title("Rock Paper Scissor")
icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "icon.png"))
root.iconphoto(False, icon)
root.geometry("400x500")
root.resizable(False,False)

choices=["Rock","Paper","Scissors"]
user_score=0
comp_score=0

def play(user_choice):
    global user_score,comp_score
    comp_choice=random.choice(choices)
    user_lab.config(text=f"Your Choice: {user_choice}")
    comp_lab.config(text=f"Computer Choice: {comp_choice}")
    if(user_choice==comp_choice):
        result_lab.config(text="Its a Draw")
    elif(
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Scissors" and comp_choice == "Paper") or
        (user_choice == "Paper" and comp_choice == "Rock")
    ):
        user_score+=1
        result_lab.config(text="You Win")
    else:
        comp_score+=1
        result_lab.config(text="You lose")
    score_lab.config(
        text=f"Score\nYou: {user_score}  |  Computer: {comp_score}"
    )

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_lab.config(text="Your Choice: ")
    comp_lab.config(text="Computer Choice: ")
    result_lab.config(text="")
    score_lab.config(text="Score\nYou: 0  |  Computer: 0")

title=tk.Label(root,text="Rock Paper Scissor",font=("Arial",18,"bold"))
title.pack(pady=10)
score_lab = tk.Label(root, text="Score\nYou: 0  |  Computer: 0", font=("Arial", 12))
score_lab.pack(pady=10)
user_lab = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_lab.pack()
comp_lab = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
comp_lab.pack()
result_lab = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_lab.pack(pady=10)

btn_fr=tk.Frame(root)
btn_fr.pack(pady=20)

rock_img = Image.open(os.path.join(BASE_DIR, "r.png"))
rock_img = rock_img.resize((80, 80), Image.Resampling.LANCZOS)
rock_img = ImageTk.PhotoImage(rock_img)

paper_img = Image.open(os.path.join(BASE_DIR, "pap.png"))
paper_img = paper_img.resize((80, 80), Image.Resampling.LANCZOS)
paper_img = ImageTk.PhotoImage(paper_img)

scissor_img = Image.open(os.path.join(BASE_DIR, "sci.png"))
scissor_img = scissor_img.resize((80, 80), Image.Resampling.LANCZOS)
scissor_img = ImageTk.PhotoImage(scissor_img)

tk.Button(btn_fr, text="Rock",image=rock_img, compound="top", command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_fr, text="Paper",image=paper_img, compound="top", command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_fr, text="Scissors",image=scissor_img,compound="top", command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)
tk.Button(root, text="New Game", width=15, command=reset_game).pack(pady=20)

root.mainloop()