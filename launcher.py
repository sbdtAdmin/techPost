import os
import threading
import time

threading.Thread(target=os.system, daemon=True, args=("""python main.py "TelegaCoder" """,)).start()
time.sleep(30)
threading.Thread(target=os.system, daemon=True, args=("""python main.py "AIworker" """,)).start()
time.sleep(50)
threading.Thread(target=os.system, daemon=True, args=("""python main.py "CoderOnline" """,)).start()

while True:
    time.sleep(120)