import winsound, random

kek = random.randint(262,1000)

while 1:
    winsound.Beep(kek, 100)
    print(kek)
    kek -= 10
    if kek <=47:
        kek = random.randint(262,1000)
