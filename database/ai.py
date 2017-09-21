import random
import os
from database.cat_facts import catfacts

def create_response(sentence):
    msg = {}
    
    #8 Ball
    eight_ball = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it',
              'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
              'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
              'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no',
              'Outlook not so good', 'Very doubtful']
    
    if "!8ball" in sentence:
        num = random.randint(0, (len(eight_ball)-1))
        msg = eight_ball[num]
        
    #Cat Facts
    if sentence == '!catfacts':
        num = random.randint(0, (len(catfacts)-1))
        msg = catfacts[num]
                       
    #Responses    
    #if "lunch" in sentence.lower():
     #   msg = "Is it on the PCard?"    
    #if "dinner" in sentence.lower():
     #   msg = "Is it on the PCard?"   
    if "dorm" in sentence.lower():
        msg = "*Residence Hall"

    return msg


