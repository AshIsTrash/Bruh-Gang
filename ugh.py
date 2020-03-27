import discord
from random import randint
from discord.ext import commands
while True:
    die = input()
    num = list(die.split('d'))
    if num[0] == '':
        num[0] = 1
    num = [int(x) for x in num]
    rollNum = int(num[0])
    rolls = []
    for dig in range(0,int(num[0])):
        rolls.append(randint(1,num[1]))
    print(rolls, sum(rolls))