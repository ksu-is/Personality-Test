__author__ = 'chintanpanchamia'
import csv
f = open('record.csv','rb')

DEBUG_NEEDED = True 

#initializing variables
profile_counter = 0
openness = 0
conscientiousness = 0
extraversion = 0
agreeableness = 0
neuroticism = 0

#loop through the lines of file record.csv
for i in f:
    profile_counter = profile_counter + 1 #incrementing the counter
    my_list = [] #creating a new empty list
    i = i.strip()
    f1 = open(i,'rb')
    csvreader = csv.reader(f1)
    for row in csvreader:
        my_list.append(float(row[0]))
    agreeableness = agreeableness + my_list[0] 
    openness = openness + my_list[1]
    conscientiousness = conscientiousness + my_list[2]
    extraversion = extraversion + my_list[3]
    neuroticism = neuroticism + my_list[4]
    #debugging print statements
    if DEBUG_NEEDED:
        print("agreeableness = " + agreeableness + ", openness = " + openness + ", conscientiousness = " + conscientiousness)
        print("extraversion = " + extraversion + ", neuroticism = " + neuroticism)

i = 0
compute = [0,0,0,0,0]

compute[0] = float(agreeableness)/profile_counter
compute[1] = float(openness)/profile_counter
compute[2] = float(conscientiousness)/profile_counter
compute[3] = float(extraversion)/profile_counter
compute[4] = float(neuroticism)/profile_counter

compute[0] = (compute[0]/5)*100
agreeableness = compute[0]
compute[1] = (compute[1]/5)*100
openness = compute[1]
compute[2] = (compute[2]/5)*100
conscientiousness = compute[2]
compute[3] = (compute[3]/5)*100
extraversion = compute[3]
compute[4] = (compute[4]/5)*100
neuroticism = compute[4]

m = max(compute)
pointer = 0
for i in compute:
    if m == i:
        pointer = compute.index(i)

dominant = ''
if pointer == 0:
    dominant = 'agreeableness'
elif pointer == 1:
    dominant = 'openness'
elif pointer == 2:
    dominant = 'conscientiousness'
elif pointer == 3:
    dominant = 'extraversion'
else:
    dominant = 'neuroticism'

compute1 = compute
i = 0
compute1.remove(m)
m2 = max(compute1)
for i in compute:
    if m2 == i:
        pointer = compute.index(i)
dominant2 = ''
if pointer == 0:
    dominant2 = 'agreeableness'
elif pointer == 1:
    dominant2 = 'openness'
elif pointer == 2:
    dominant2 = 'conscientiousness'
elif pointer == 3:
    dominant2 = 'extraversion'
else:
    dominant2 = 'neuroticism'

i = 0
compute1.remove(m2)
m3 = max(compute1)
for i in compute:
    if m3 == i:
        pointer = compute.index(i)

dominant3 = ''
if pointer == 0:
    dominant3 = 'agreeableness'
elif pointer == 1:
    dominant3 = 'openness'
elif pointer == 2:
    dominant3 = 'conscientiousness'
elif pointer == 3:
    dominant3 = 'extraversion'
else:
    dominant3 = 'neuroticism'

print ('Detailed Social Comfort Levels of the room at the moment:\n')
print ('Openness to Experiences: ' + str(openness))
print ('Conscientiousness: ' + str(conscientiousness))
print ('Extraversion: ' + str(extraversion))
print ('Agreeableness: ' + str(agreeableness))
print ('Neuroticism: ' + str(neuroticism))

result = ''

if(dominant is 'openness'):
    if(dominant2 is 'conscientiousness'):
        if(dominant3 is 'extraversion'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'extraversion'):
        if(dominant3 is 'conscientiousness'):
            result = 'Loud'
        elif(dominant3 is 'agreeableness'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'agreeableness'):
        if(dominant3 is 'conscientiousness'):
            result = 'Routine'
        elif(dominant3 is 'extraversion'):
            result = 'Loud'
        else:
            result = 'Ambient'
    else:
        if(dominant3 is 'agreeableness'):
            result = 'Quiet'
        elif(dominant3 is 'conscientiousness' or 'extraversion'):
            result = 'Routine'
elif(dominant is 'conscientiousness'):
    if(dominant2 is 'openness'):
        if(dominant3 is 'neuroticism' or 'agreeableness'):
            result = 'Ambient'
        else:
            result = 'Routine'
    if(dominant2 is 'extraversion'):
        if(dominant3 is 'openness' or 'agreeableness'):
            result = 'Loud'
        else:
            result = 'Routine'
    if(dominant2 is 'agreeableness'):
        if(dominant3 is 'openness' or 'extraversion'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'neuroticism'):
        if(dominant3 is 'agreeableness' or 'openness'):
            result = 'Ambient'
        else:
            result = 'Routine'
elif(dominant is 'extraversion'):
    if(dominant2 is 'openness'):
        if(dominant3 is 'agreeableness' or 'conscientiousness'):
            result = 'Loud'
        else:
            result = 'Routine'
    if(dominant2 is 'conscientiousness'):
        if(dominant3 is 'openness'):
            result = 'Loud'
        elif(dominant3 is 'agreeableness'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'agreeableness'):
        if(dominant3 is 'openness'):
            result = 'Loud'
        elif(dominant3 is 'conscientiousness'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'neuroticism'):
        if(dominant3 is 'openness' or 'conscientiousness'):
            result = 'Routine'
        else:
            result = 'Ambient'
elif(dominant is 'agreeableness'):
    if(dominant2 is 'openness' or 'extraversion'):
        if(dominant3 is 'conscientiousness'):
            result = 'Loud'
        else:
            result = 'Ambient'
    if(dominant2 is 'conscientiousness'):
        if(dominant3 is 'openness' or 'extraversion'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'neuroticism'):
        if(dominant3 is 'openness'):
            result = 'Quiet'
        else:
            result = 'Ambient'
else:
    if(dominant2 is 'openness' or 'agreeableness'):
        if(dominant3 is 'conscientiousness'):
            result = 'Quiet'
        else:
            result = 'Ambient'
    if(dominant2 is 'conscientiousness'):
        if(dominant3 is 'openness' or 'extraversion'):
            result = 'Routine'
        else:
            result = 'Ambient'
    if(dominant2 is 'extraversion'):
        if(dominant3 is 'Agreeableness'):
            result = 'Ambient'
        else:
            result = 'Routine'

print ('Summarized Social Comfort Level of the room is: ' + result)
