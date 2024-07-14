from turtle import *
speed("fastest")
###fd(170)
# rt(90)
# fd(100)
# rt(60)
# fd(100)
# rt(60)
# fd(100)
# rt(60)
# fd(100)
s=8
d=100
for i in range(s):
    fd(d)
    lt(360/s)
    write(i, font=("Arial",12,"normal"))
    circle(360/s)





mainloop()

