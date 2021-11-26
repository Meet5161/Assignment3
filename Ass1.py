print ("The main purpose to make this program is to get familier with Python language and I really liked this project as a part of my curriculum because I learnt plenty of things while making this little bit Software. \n ")

print (" Welcome to AM's Shirt Cost Calculator \n")

print (" \n These are the available Colors we have. ")

print (" 1 == Black 4.3$ ")
print (" 2 == Blue  2.8$ ")
print (" 3 == white 8.5$ ")
print (" 4 == Yellow 3$ ")
print (" 5 == Orange 5.1$ ")

print (" \n What type of colour do you want to order? ")

class Shirts():
    def __init__(self,shirt_style, shirt_color, quantity_shirts):
        self.shirt_style = shirt_style
        self.shirt_color = shirt_color
        self.quantity_shirts = quantity_shirts

shirt_color = int(input())

if shirt_color == 1:
    print (" You selected Black ")
    VOT = 4.3

elif shirt_color == 2: 
    print (" You selected Blue ")  
    VOT =2.8

elif shirt_color == 3:
    print (" You selected white ")   
    VOT =8.5

elif shirt_color == 4:
    print (" You selected Yellow ")
    VOT =3

elif shirt_color == 5:
    print (" You selected Orange ")    
    VOT =5.1

else: 
    print (" Please select 1 to 5 ")  