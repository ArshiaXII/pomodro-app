import time
from datetime import timedelta
import os
from playsound import playsound
import threading
import tkinter as tk

def play_alarm():
    alarm_sound = "alarm.mp3"  # Burada alarm sesi için kullanmak istediğiniz ses dosyasını belirtin
    playsound(alarm_sound)

def pomodoro_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining = end_time - time.time()
        remaining_str = str(timedelta(seconds=int(remaining)))
        timer_label.config(text=f"Kalan süre: {remaining_str}")
        time.sleep(1)
    timer_label.config(text="Zaman doldu!")
    play_alarm()

def start_pomodoro():
    work_duration = 25 * 60
    short_break_duration = 5 * 60
    long_break_duration = 15 * 60
    pomodoro_count = 0

    while True:
        timer_label.config(text="Çalışma süresi başladı!")
        pomodoro_timer(work_duration)
        pomodoro_count += 1

        if pomodoro_count % 4 == 0:
            timer_label.config(text="Uzun mola süresi başladı!")
            pomodoro_timer(long_break_duration)
        else:
            timer_label.config(text="Kısa mola süresi başladı!")
            pomodoro_timer(short_break_duration)

def start_thread():
    threading.Thread(target=start_pomodoro, daemon=True).start()

# GUI oluştur
root = tk.Tk()
root.title("Pomodoro Timer")

timer_label = tk.Label(root, text="Pomodoro Timer'a hoş geldiniz!", font=("Arial", 16))
timer_label.pack(pady=20)

start_button = tk.Button(root, text="Başlat", command=start_thread, width=20)
start_button.pack(pady=10)

root.mainloop()
