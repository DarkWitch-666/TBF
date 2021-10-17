import time
import sys
import os
# animation sooooooooooooon............
animation = [" Installing...\n", " Installing..\n", " Installing...\n",]
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    #modules
    os.system("pip3 install colorama")
    os.system("pip3 install requests")
    #os.system("pip3 install ")
    print("\n     Installing complete!       \n")
    sys.exit()
sys.exit(" type: python3 tbf.py")