import turtle
t = turtle.Turtle()
mylist = ["purple","red","orange","blue","green"]
#print("By Manmohan Mirkar")
#turtle.write('By Manmohan Mirkar!')
turtle.color('black')
Style = ('Courier', 100, 'italic')
turtle.write('Manmohan      Mirkar!!', font=Style, align='center')
for i in range(200):
    t.color(mylist[i%5])
    t.pensize(i/10+1)
    t.forward(i)
    t.left(59)