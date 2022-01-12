import random as r
score = 0
def importpos(value):
    posx = r.randint(0,3)
    posy = r.randint(0,3)
    while array2d[posx][posy] != " ":
        posx = r.randint(0,3)
        posy = r.randint(0,3)
    array2d[posx][posy] = value  
array = []
array2d = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
bombs= int(input("how many bombs? (there are 16 spaces so don't go over 16) \n"))
for x in range(bombs):
    importpos("x")
for x in range(16-bombs):
    importpos("1")
guessarray = [[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]
for x in range(4):
    for y in range(4):
        guessarray[x][y] = "?"
for x in range(16-bombs):
    for x in range(4): print(guessarray[x])
    gx = int(input("input row for where your guess is \n"))
    gy = int(input("input column for where your guess is \n"))
    gx -= 1
    gy -= 1
    while guessarray[gx][gy] != " ":
        print("that position has already been verified. Please input new co ordinates.")
        gx = int(input("input row for where your guess is \n"))
        gy = int(input("input column for where your guess is \n"))
        gx -= 1
        gy -= 1
    if array2d[gx][gy] == "x":
        guessarray = array2d
        print("that space was a bomb! you lose! ")
        break
    elif array2d[gx][gy] == "1":
        score += 1
        guessarray[gx][gy] = "1"
print("your score was :", score)
