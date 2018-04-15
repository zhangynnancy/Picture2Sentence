def process():
    file=open("IN_of_place365.txt")
    processed=[line.strip().split(' ') for line in file.readlines()]
    infile=open("result.txt","w")
    for line in processed:
         for i in range(len(line)):
             if(i!=1):
                 infile.write(line[i])
                 infile.write(' ')
         infile.write('\n')

def dict_made():
    file=open('categories_places365.txt')
    processed=[line.strip().split('/') for line in file.readlines()]
    processed=[line[2:] for line in processed]
    places=[]
    for line in processed:
        if len(line)>1:
            str1=""
            for i in range(len(line)-1):
               str1+=line[i]+"/"
            #print(line[-2])
            str2=line[len(line)-1].strip().split(' ')[0]      	 
            str1=str1+str2
            places.append(str1)
            #places.append(line[0])

        else:
            places.append(line[0].strip().split(' ')[0])

    return places

def match(word,places):
    for i in range(len(places)):
        if(word==places[i]):
            return i
    return -1

def get_result():
    file=open("../../../output")
    result=[line.strip() for line in file.readlines()]
    del result[1]
    object_result=[]
    motion_result=[]
    place_result=[]
    
    line=result[0]
    i=0
    
    if(line=="person"):
        i=i+1;
        line=result[i]
        while(line!="motion"):
            object_result.append(line)
            i=i+1
            #print(i)
            line=result[i]
        i=i+2
        line=result[i]
        while(line!="place"):
            motion_result.append(line)
            i=i+1
            line=result[i]
        i=i+1
        line=result[i]
        while(i<len(result)):
            place_result.append(result[i])
            i=i+1
            
    return object_result,motion_result,place_result
 
def get_num(object_result):
    num=0
    for i in range(0,len(object_result),2):
        if(object_result[i][0:6]=="person"):
            num+=1

    return num
def get_jieci(num):
    file=open("place365.txt")
    processed=[line.strip().split() for line in file.readlines()]
    return processed[num][1]
    
def get_place(motion_result):
    place=motion_result[0]
    place_result=""
    for i in range(len(place)):
        if(place[i]=='>'):
            place_result=place[i+2:]
    return place_result        

class_need = ['applying eye makeup', 'applying lipstick', 'playing basketball', 'playing basketball dunk', 'doing bench press', 'biking', 
                  'blowing dry hair', 'blowing candles', 'doing body weight squats', 'brushing teeth', 'cutting in kitchen', 
                  'drumming', 'cutting hair', 'doing hand stand pushups', 'doing head massage', 'playing hula hoop', 'juggling balls', 'playing jump rope', 
                  'jumping jack', 'knitting', 'mopping floor', 'playing guitar', 'playing piano', 'playing pommel horse', 
                  'doing pull ups', 'doing push ups', 'SalsaSpin', 'shaving beard', 'playing soccer juggling', 'playing table tennis', 'playing TaiChi',
                  'swing tennis', 'typing', 'doing wall push ups', 'writing on board']   

#def get real_motion(motion):
#    for i in range(len(class_need)):
        
       
object_result,motion_result,place_result=get_result()
places=dict_made()
#qindex=match('atrium/public',places)

num=get_num(object_result)
place=get_place(motion_result)
index=match(place,places)
jieci=get_jieci(index)
if(num>1):
    print(str(num)+" persons are "+place_result[0]+" "+jieci+" the "+place)
else:
    print(str(num)+" person is "+place_result[0]+" "+jieci+" the "+place)

