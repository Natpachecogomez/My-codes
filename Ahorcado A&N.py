import random
word=["vaca", "tortuga", "cerdo", "ardilla", "foca", "serpiente", "bufalo", "lobo", "canguro", "mono", "burro", "chiguiro", "hamster", "gato", "arabella", "pedrito"]
rand=random.choice(word)
tries=len(rand)
list=[]
print("Welcome o(*￣︶￣*)o let's play a little")

for i in rand:
    list.append(i)
aux=[]
lcopy=list.copy()

for x in range (len(list)):
    aux.append("-")

while tries!=0:
    let=input("Letra: ")
    try:
        for i in range(len(list)):
            p=lcopy.index(let)
            aux.pop(p)
            aux.insert(p,let)
            lcopy.pop(p)
            lcopy.insert(p, '-')
    except:
        pass
    print(aux)
    
    try:
        p=list.index(let)
    except:
        tries-=1
        print("La letra no está en la palabra")
    if aux==list:
        print("\nYou've won (✿ ◡ ‿ ◡ )")
        break

if tries==0:
    if aux==list:
        print("\nYou've won (✿ ◡ ‿ ◡ )")
    else:
        print("      -----\n      |   |\n      O   |\n     /|\  |   You've lost (┬┬﹏┬┬)\n     / \  |\n          |")