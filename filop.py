def add_data():
    with open('../Files/test.txt', 'w') as f:
        s=input('Enter a sentence:')
        f.write(s)
def dis_data():
    with open('../Files/test.txt', 'r') as f:
        s=f.read()
        print(s)
def count():
    try:
        v,c,d,sp=0,0,0,0
        with open('../Files/test.txt', 'r') as f:
            s=f.read()
            for i in s:
                if i.isspace()==True:
                    sp+=1
                if i.isalpha()==True:
                    if i in 'AEIOUaeiou':
                        v+=1
                    else:
                        c+=1
                if i.isdigit()==True:
                    d+=1
        print(sp,v,c,d)
    except EOFError():
        f.close()
def search():
    f=open('../Files/test.txt', 'r')
    r=f.read()
    w=input('enter the word to be searched--')
    flag=True
    try:
        while True:
            for i in r:
                if i==w:
                    print('Found')
                    flag=True
    except EOFError:
        f.close()
    if flag==False:
        print('No records found')
def size():
    with open('../Files/test.txt', 'r') as f:
        s=f.read()
        print('Size of the file:',len(s))
        l=f.readlines()
        print('No. of the lies:',len(l))
def main_menu():
    ch='y'
    while ch=='y':
        print('Enter 1,2,3,4,5')
        c=int(input('Enter your choice:'))
        if c==1:
            add_data()
        elif c==2:
            dis_data()
        elif c==3:
            count()
        elif c==4:
            search()
        elif c==5:
            size()
        else:
            print('Quit')
        ch=input('Do you want to contiue:')
main_menu()

