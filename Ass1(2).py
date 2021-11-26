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

shirt_style = int(input("\n Now enter 1 for a POLO and enter 2 for a T-shirt "))

if shirt_style == 1:
    print("\n You selected POLO ") 

elif shirt_style == 2:
    print(" You selected T-shirt")    

else:
    print (" Choose 1 or 2 ")

print ("\nSelect the trouser you wants to buy? ")

class Trouser():
    def __init__(self, Trouser_color, num_of_Trouser):
        self.Trouser_color = Trouser_color
        self.num_Trouser = num_of_Trouser

print (" 1 == Black Trouser 2.9$ ")
print (" 2 == Blue Trouser 5.4$ ")
print (" 3 == white Trouser 4.8$ ")         

Trouser_color = int(input())

if Trouser_color == 1:
    print (" You selected Black Trouser ")
    VOTS = 2.9

elif Trouser_color == 2: 
    print (" You selected Blue Trouser ")  
    VOTS =5.4

elif Trouser_color == 3:
    print (" You selected white Trouser ")   
    VOTS =4.8

else: 
    print (" Please select 1 to 3 ") 

quantity = 2 
