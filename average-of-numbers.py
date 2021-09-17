count = 0
total = 0
largist = None
smalist = None
while True:
    try:
        num = input('Enter number: ')
        if num == 'done':
            break
        
        re_num = float(num)
        
    except:
        print('Error, please inter a number.')
        continue
    
    count += 1
    total += re_num

    if (largist == None) or (re_num > largist):
        largist = re_num
        
    if (smalist == None) or (re_num < smalist):
        smalist = re_num
        

average = total / count
print(' Average:', average, '\n Smalist number is:', smalist, '\n largist number is:', largist)
