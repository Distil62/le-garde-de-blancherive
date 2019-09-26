import sched, time
from datetime import datetime
import random

minutesRandom = random.randint(0, 59)

s = sched.scheduler(time.time, time.sleep)

def lol(sc, msg):
    print(datetime.now().minute)
    s.enter(1, 1, lol, (sc, msg,));

s.enter(3, 1, lol, (s, "lol",));
s.run()