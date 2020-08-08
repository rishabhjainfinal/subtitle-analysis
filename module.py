from collections import Counter 
import os

def most_common(name_of_serial_or_movie,files,directory_name=''):        
    if directory_name != '':
        for index,file in enumerate(files):
            files[index]=os.path.join(directory_name,file)

    inall=[]
    count={}
    # files with subtitle
    def alltalks(file_name):
        file = open(file_name, 'r', encoding="utf8")
        a = file.readlines()
        talking = []

        for i in range(len(a)):
            # for integers
            try:
                if int(a[i]):
                    continue
            except:
                pass

            # timeline
            if '-->' in a[i]:
                pass

            # empty space
            elif a[i] == '\n':
                pass

            # messages
            else:
                text = a[i]
                text = text.replace('\n', '').replace('?', '').replace('.', '').replace(',', '').replace(
                    '-', '').replace('!', '').replace('"', '').replace('<i>', '').replace('</i>', '')
                talking.append(text)

        return talking

    #readsubtitles
    for i in files:
        a=alltalks(i)
        inall=inall+a

    # print(inall)
    # print("length=",len(inall))

    for items in inall:
        for i in items.split(' '):
            # for i in j:           for leters count
                # print(i)
            i=i.capitalize()
            if i in count.keys():
                count[i]=count[i]+1
            else:
                count[i] = 1

    # print(count)
    # print(len(count))

            # forjust1winner
    # Keymax = max(count, key=count.get) 
    # print("the most used word is : ",Keymax,' ',count['keymax'],'times') 

    print()
    print('most common silent words')
    print("fuck:",count['Fuck'],'times') 
    print("shit:",count['Shit'],'times') 
    print("bitch:",count['Bitch'],'times') 
    print()

    # finding highest values in a Dictionary    
    k = Counter(count)
    high = k.most_common(10)  
    print(f'10 most common words used in {name_of_serial_or_movie}:') 
    print("words: count") 
    for i in high: 
        print(i[0]," :",i[1]," ") 


