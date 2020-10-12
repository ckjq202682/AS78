#AS78

face = input("happy, sad or suprised")

def happy():
    print("      _____     ")
    print("    .'     '.   ")
    print("   /  o   o  \  ")
    print("  |           | ")
    print("  |  \     /  | ")
    print("   \  '---'  /  ")
    print("    '._____.'   ")

def sad():
    print("      _____     ")
    print("    .'     '.   ")
    print("   /  o   o  \  ")
    print("  |           | ")
    print("  |   .---.   | ")
    print("   \ /     \ /  ")
    print("    '._____.'   ")

def suprised():
    print("      _____     ")
    print("    .'     '.   ")
    print("   /  o   o  \  ")
    print("  |    ___    | ")
    print("  |   /   \   | ")
    print("   \  \___/  /  ")
    print("    '._____.'   ")

if face == "happy":
    happy()
elif face == "sad":
    sad()
elif face == "suprised":
    suprised()



