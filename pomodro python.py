import time
from datetime import timedelta
import os

def pomodoro_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        remaining = end_time - time.time()
        print(f"\rKalan süre: {str(timedelta(seconds=int(remaining)))}", end="")
        time.sleep(1)
    print("\rZaman doldu!                ")

def main():
    work_duration = 25 * 60
    short_break_duration = 5 * 60
    long_break_duration = 15 * 60
    pomodoro_count = 0

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"--- Pomodoro #{pomodoro_count + 1} ---")
        print("Çalışma süresi başladı!")
        pomodoro_timer(work_duration)
        pomodoro_count += 1

        if pomodoro_count % 4 == 0:
            print("Uzun mola süresi başladı!")
            pomodoro_timer(long_break_duration)
        else:
            print("Kısa mola süresi başladı!")
            pomodoro_timer(short_break_duration)

if __name__ == "__main__":
    main()
