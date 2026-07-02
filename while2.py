while True:
    int=input('Enter a number: ')
    if int=='done':
        break
    try:
        int=int(int)
        print(int)
    except ValueError:
        print('Invalid input')
        continue
    total=total+int
    count=count+1
    if count>0:
        average=total/count
        print('Average: ', average) 
        print('Total: ', total)
        print('Count: ', count)
        else:
            print('Average: 0')
        