#ini adalah program membuat random password
# dibuat pada 06/11/2024
# dibuat oleh M Fagian Darmawan
import os
os.system("cls")
print(30 * "\033[38;5;13m=")
print("PROGRAM RANDOM PASSWORD".center(30))
print(30 * "\033[38;5;13m=")

import random
passlen = int(input("enter the length of password = "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
P="".join(random.sample(s,passlen))
print(P)