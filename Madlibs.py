#Madlibs Project

#This is first method using simple basic code.

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("verb: ")
famous_person = input("famous person: ")


matlabs = f"Computer programming is so {adj}! It makes me so exicted all the time because \ I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person} "
print(matlabs)


#This is Second method using Modules.

from sample_madlibs import hp, code, zombie, hugergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hugergames]) 
    m.matlib()
