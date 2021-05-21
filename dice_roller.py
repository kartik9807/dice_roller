import random #imported random module
def dice():# making a function for dice rolling
    while(True): # putting in loop
        a = input("Press entry to roll the dice :) ")
        if(a=="exit"):
            exit(0)
        dice = random.randint(1,6)
        if(dice==1):
            print("[     ]")
            print("[  0  ]")
            print("[     ]\n")
        if(dice==2):
            print("[0    ]")
            print("[     ]")
            print("[    0]\n")
        if(dice==3):
            print("[  0  ]")
            print("[  0  ]")
            print("[  0  ]\n")
        if(dice==4):
            print("[0   0]")
            print("[     ]")
            print("[0   0]\n")
        if(dice==5):
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]\n")
        if(dice==6):
            print("[0   0]")
            print("[0   0]")
            print("[0   0]\n")
            
dice() # calling function
