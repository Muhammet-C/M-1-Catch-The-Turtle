import tkinter as tk
import random

## Oyun ayarları
score = 0
geriye_say_suresi = 5

genislik = 1200
yukseklik = 700

kaplumbaga_gorunme_suresi = 1000  # Kaplumbağanın görünme süresi (ms cinsinden)

## Fonksiyonlar
def geriye_say(sayac):
    if sayac > 0:
        geriye_say_etiketi.config(text=str(sayac))
        sayac -= 1
        pencere.after(1000, geriye_say, sayac)
    else:
        geriye_say_etiketi.config(text="Oyun bitti! R tuşuna basarak tekrar oyna.")
        hide_turtle()

def show_turtle():
    turtle.place(x=random.randint(0, genislik - 50), y=random.randint(0, yukseklik - 50))
    global turtle_hareket_id
    turtle_hareket_id = pencere.after(kaplumbaga_gorunme_suresi, hide_turtle)

def hide_turtle():
    turtle.place_forget()
    if geriye_say_etiketi.cget("text") != "Oyun bitti! R tuşuna basarak tekrar oyna.":
        show_turtle()

def increase_score():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

def restart_game(event):
    if geriye_say_etiketi.cget("text") == "Oyun bitti! R tuşuna basarak tekrar oyna.":
        global score
        score = 0
        score_label.config(text="Score: 0")
        geriye_say(geriye_say_suresi)
        show_turtle()
        restart_label.place_forget()  # "R tuşuna basarak tekrar oyna" yazısını ekrandan kaldır

## GUI
pencere = tk.Tk()
pencere.title("Catch The Turtle")
pencere.geometry(f"{genislik}x{yukseklik}")

geriye_say_etiketi = tk.Label(pencere, text="", font=("Arial", 24))
geriye_say_etiketi.place(relx=0.50, rely=0.15, anchor="center")

turtle = tk.Label(pencere, text="🐢", font=("Arial", 30))

score_label = tk.Label(pencere, text="Score: 0", font=("Arial", 16))
score_label.pack()

turtle.bind("<Button-1>", lambda event: increase_score())
pencere.bind("r", restart_game)  # R tuşuna basıldığında restart_game fonksiyonunu çağır

geriye_say(geriye_say_suresi)
show_turtle()

restart_label = tk.Label(pencere, text="R tuşuna basarak tekrar oyna.", font=("Arial", 12), fg="red") # Oyun sonu mesajı gösteriyor.

pencere.mainloop()