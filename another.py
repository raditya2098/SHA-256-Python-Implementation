'''from more_itertools import sliced
global h0,h1,h2,h3,h4,h5,h6,h7,k

h0= 0x6a09e667
h1= 0xbb67ae85
h2= 0x3c6ef372
h3= 0xa54ff53a
h4= 0x510e527f
h5= 0x9b05688c
h6= 0x1f83d9ab
h7= 0x5be0cd19

k=[0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
   0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
   0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
   0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
   0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
   0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
   0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
   0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

def rotate(ip,n):
    r1=ip[0:len(ip)-d]
    r2=ip[len(ip)-d:]
    return (r2+r1)
'''
'''def shift_right(bit_string,n):
    bit_list=[]
    bit_string=check_b(bit_string)
    for i in range(len(bit_string)):
        bit_list.append(bit_string[i])
    count=0
    while count <= n-1:
        bit_list.pop(-1)
        count+=1
    front_append=['0']*n
    front_append+=bit_list
    ret_str=''.join(map(str,front_append))
    return(ret_str)
msg=input("Enter the message:\t")
l=[]
for ch in msg:
    l.append(ch)
#print(l)
m=[]
for i in l:
    m.append(ord(i))
#print(m)

binary=[]
for i in m:
    x=bin(i)[2:].zfill(8)
    binary.append(x)
#print(binary)    
bin_str=''.join(map(str,binary))
n1=len(bin_str)
print(n1)
n=n1

mod=int(n1%512)
if(mod<447):
    padding=447-mod
elif(mod==447):
    padding=0
else:
    excess=mod-447
    padding=512-excess
binary.append('1')
n1+=1
while padding!=0:
    binary.append('0')
    n1+=1
    padding-=1
bin_str=''.join(map(str,binary))

n_bin=bin(n)[2:].zfill(64)
str_complete=bin_str+n_bin
n1=len(str_complete)
print(n1)
#print(str_complete,"\n",n1)

l=list(sliced(str_complete,512))
#print(l)
count=0

for cha in l:
    a=h0
    b=h1
    c=h2
    d=h3
    e=h4
    f=h5
    g=h6
    h=h7
    rounds=0
    w1=list(sliced(cha,32))
    w=[]
    for i in w1:
        w.append(i)
    for i in range(0,48):
        w.append('00000000000000000000000000000000')
    while(rounds!=64):
        if(rounds>=16):
            s0=(int(rotate(str(w[rounds-15]),7))^int(rotate(str(w[rounds-15]),18))^(int(w[rounds-15])>>3))
            s1=(int(rotate(str(w[rounds-2]),17))^int(rotate(str(w[rounds-2]),19))^(int(w[rounds-2])>>10))
            w[rounds]=(int(w[rounds-16])+s0+int(w[rounds-7])+s1)

        x=w[rounds]
        ch=((e&f)^((~e)&g))
        ma=(((a&b)^(a&c)^(b&c))%(2**32))
        si0=((int(rotate(str(a),2))^int(rotate(str(a),13))^int(rotate(str(a),22)))%(2**32))
        si1=((int(rotate(str(e),6))^int(rotate(str(e),11))^int(rotate(str(e),25)))%(2**32))
        temp1=(int(si1)+((int(h)+int(ch)+((int(k[rounds])+int(x))%(2**32)))%(2**32)))
        temp2=(si0+(ma+temp1))
        h=g
        g=f
        f=e
        e=(d+((temp1)%(2**32)))
        d=c
        c=b
        b=a
        a=temp2

        rounds+=1

        print("ma=",ma," e0=",si0," Ch=",ch," e1=",si1)

        
    h0=((h0+a)%(2**32))
    h1=((h1+b)%(2**32))
    h2=((h2+c)%(2**32))
    h3=((h3+d)%(2**32))
    h4=((h4+e)%(2**32))
    h5=((h5+f)%(2**32))
    h6=((h6+g)%(2**32))
    h7=((h7+h)%(2**32))


H10=hex(h0).split('x')[-1]
H11=hex(h1).split('x')[-1]
H12=hex(h2).split('x')[-1]
H13=hex(h3).split('x')[-1]
H14=hex(h4).split('x')[-1]
H15=hex(h5).split('x')[-1]
H16=hex(h6).split('x')[-1]
H17=hex(h7).split('x')[-1]

H0='0'
H1='0'
H2='0'
H3='0'
H4='0'
H5='0'
H6='0'
H7='0'

if(len(H10)==7):
    H0+=str(H10)
elif(len(H10)==6):
    H0+='0'
    H0+=str(H10)
elif(len(H10)==8):
    H0=H10
if(len(H11)==7):
    H1+=str(H11)
elif(len(H11)==6):
    H1+='0'
    H1+=str(H11)
elif(len(H11)==8):
    H1=H11
if(len(H12)==7):
    H2+=str(H12)
elif(len(H12)==6):
    H2+='0'
    H2+=str(H12)
elif(len(H12)==8):
    H2=H12
if(len(H13)==7):
    H3+=str(H13)
elif(len(H13)==6):
    H3+='0'
    H3+=str(H13)
elif(len(H13)==8):
    H3=H13
if(len(H14)==7):
    H4+=str(H14)
elif(len(H14)==6):
    H4+='0'
    H4+=str(H14)
elif(len(H14)==8):
    H4=H14
if(len(H15)==7):
    H5+=str(H15)
elif(len(H15)==6):
    H5+='0'
    H5+=str(H15)
elif(len(H15)==8):
    H5=H15
if(len(H16)==7):
    H6+=str(H16)
elif(len(H16)==6):
    H6+='0'
    H6+=str(H16)
elif(len(H16)==8):
    H6=H16
if(len(H17)==7):
    H7+=str(H17)
elif(len(H17)==6):
    H7+='0'
    H7+=str(H17)
elif(len(H17)==8):
    H7=H17

hash_value=str(H0)+str(H1)+str(H2)+str(H3)+str(H4)+str(H5)+str(H6)+str(H7)
print('h=',hash_value)



def rotate_r(bit_string,n):
    bit_list=[]
    for i in range(len(bit_string)):
        bit_list.append(bit_string[i])
    count=0
    while count <= n-1:
        list_main=list(bit_list)
        var_0=list_main.pop(-1)
        list_main=list([var_0]+list_main)
        bit_list=list(list_main)
        count+=1
    lm=[]
    for ch in list_main:
        if ch!='b':
            lm.append(ch)
    bin_str=''.join(map(str,lm))
    return(int(bin_str,2))

    return(''.join(map(str,list_main)))
x=2026797449
print(int(rotate_r(bin(x),6))^int(rotate_r(bin(x),11))^int(rotate_r(bin(x),25)))
'''
def rotate_r(bit_string,n):
    bit_list=[]
    bit_list1=[]
    bit_list2=[]
    for i in range(len(bit_string)):
        bit_list1.append(bit_string[i])
    #print(len(bit_list1))
    empty=0
    for i in range(2,len(bit_list1)):
        bit_list2.append(bit_list1[i])
    
    empty=32-len(bit_list2)    
    for i in range(0,empty):
        bit_list.append('0')
    for ch in bit_list2:
        bit_list.append(ch)
    #print(bit_list)
    count=0
    while count <= n-1:
        list_main=list(bit_list)
        var_0=list_main.pop(-1)
        list_main=list([var_0]+list_main)
        bit_list=list(list_main)
        count+=1
    lm=[]
    for ch in list_main:
        if ch!='b':
            lm.append(ch)
        
    bin_str=''.join(map(str,lm))
    return(int(bin_str,2))

def check_b(string1):
    l=[]
    l1=[]
    for i in range(len(string1)):
        l.append(string1[i])
    empty=0
    for ch in l:
        if ch!='b':
            l1.append(ch)
    empty=32-len(l1)
    x=[]
    for i in range(0,empty):
        x.append('0')
    for ch in l1:
        x.append(ch)
    st=''.join(map(str,x))
    return st
x=2108187653
cc=check_b(bin(x))

print(int(check_b(bin(rotate_r((cc),17))),2))
print(check_b(bin(x)))
print(check_b(bin(rotate_r(bin(x),17))))
print(check_b(bin(rotate_r(bin(x),17))))
