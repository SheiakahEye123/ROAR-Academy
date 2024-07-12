import os

source = "motto.txt"
print(os.path.dirname(os.path.abspath(__file__)))
try:
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    handle = open(path+"/"+source, "+wt")

    handle.write("Fiat Lux!" + "\n")

except:
    print("Wrong!")
    exit

finally:
    handle.close()

try:
    path = os.path.dirname(os.path.abspath(__file__))
    handle = open(path+"/"+source, "+at")

    handle.write("Let there be Light!")
except:
    print("Wrong!")
    exit

finally:
    handle.close()