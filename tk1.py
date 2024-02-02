from tkinter import *

bomb = 100
score = 0
best_score = 0
press_return = True

def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        label.config(text="")
        update_display()
        update_point()
        update_bomb()
        press_return = False

def update_display():
    global score
    global bomb
    if bomb > 50:
        bomb_label.config(image=normal_photo)
    elif 0 < bomb < 50:
        bomb_label.config(image=no_photo)
    else:
        bomb_label.config(image=bangPhoto)
    fuse_label.config(text="Fuse=" + str(bomb))
    score_label.config(text="Score=" + str(score))
    best_score_label.config(text="Best Score=" + str(best_score))
    fuse_label.after(100, update_display)

def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)

def update_point():
    global score
    global best_score
    score += 1
    if score > best_score:
        best_score = score
    if is_alive():
        score_label.after(3000, update_point)

def click():
    global bomb
    if is_alive():
        bomb += 1

def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        label.config(text="BANG! BANG! BANG!")
        press_return = True
        return False
    else:
        return True

root = Tk()
root.title("Bang Bang")
root.geometry("500x550")

label = Label(root, text="Press[Enter] to start the game", font=('Comic Sans MS', 12), bg="Blue")
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb), font=('Comic Sans MS', 14))
fuse_label.pack()

score_label = Label(root, text="Score: " + str(score), font=('Comic Sans MS', 14))
score_label.pack()

best_score_label = Label(root, text="Best Score: " + str(best_score), font=('Comic Sans MS', 14))
best_score_label.pack()

no_photo = PhotoImage(file="bomb_no.gif")
normal_photo = PhotoImage(file="bomb_normal.gif")
bangPhoto = PhotoImage(file="pow.gif")
bomb_label = Label(root, image=normal_photo)
bomb_label.pack()

click_button = Button(root, text="Click me", font=('Comic Sans MS', 14), bg="#000000", fg="#ffffff", command=click, width=15)
click_button.pack()

root.bind('<Return>', start)

root.mainloop()
