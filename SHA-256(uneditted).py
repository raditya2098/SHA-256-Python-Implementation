from more_itertools import sliced
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

def check_32(string1):
    if len(string1)==32:
        print('true')
    else:
        print('false')

def shift_right(bit_string,n):
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
    l2=[]
    for i in range(len(string1)):
        l.append(string1[i])
    empty=0
    for ch in l:
        if ch!='b':
            l2.append(ch)
    if(len(l2)==33):
        for i in range(1,33):
            l1.append(l2[i])
    elif(len(l2)>33):
        for i in range((len(l2)-32),len(l2)):
            l1.append(l2[i])
    else:
        for i in range(0,len(l2)):
            l1.append(l2[i])
    empty=32-len(l1)
    x=[]
    for i in range(0,empty):
        x.append('0')
    for ch in l1:
        x.append(ch)
    st=''.join(map(str,x))
    return st
        


def mod32_add(input_set):
    value=0
    for i in range(len(input_set)):
        value+=input_set[i]
    mod_32 = 4294967296
    return(value%mod_32)
    
W=32
M=1<<W
FF=M-1
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
    #print('a=',a,'b=',b,'c=',c,'d=',d,'e=',e,'f=',f,'g=',g,'h=',h
    for i in w1:
        w.append(i)
    print(w)
    print(w[15])
    while(rounds<16):    
        si1a=rotate_r(bin(e),6)
        si1b=rotate_r(bin(e),11)
        si1c=rotate_r(bin(e),25)
        #print(si1a,si1b,si1c)
        ch=((int(e)&int(f))^((~int(e))&int(g)))
        ma=((int(a)&int(b))^(int(a)&int(c))^(int(b)&int(c)))
        si0=(((rotate_r(bin(a),2))^(rotate_r(bin(a),13)))^(rotate_r(bin(a),22)))
        #print(si1a^si1b)
        si1=si1a^si1b^si1c
        #print(si1)
        #if rounds<3:
            #print(int(w[rounds],2))
            #print(e)
        temp1=mod32_add([int(si1),int(h),int(ch),int(k[rounds]),int(str(w[rounds]),2)])
        #if rounds<16:
            #print(rotate_r(bin(e),6))
            #print(int(si1),int(k[rounds]))
            #print(int(h)+int(si1)+int(ch)+int(k[rounds]))+int(x))
        temp2=mod32_add([int(si0),int(ma),int(temp1)])
        h=g
        g=f
        f=e
        e=mod32_add([d,temp1])
        d=c
        c=b
        b=a
        a=temp2

        rounds+=1
        #print('rounds=',rounds-1)
        
        '''if rounds<=16:
            print("ma=",ma," e0=",si0," Ch=",ch," e1=",si1)
            print(int(a)," ",int(b)," ",int(c)," ",int(d)," ",int(e)," ",int(f)," ",int(g)," ",int(h))'''
            

    while(rounds>=16 and rounds!=64):
        print('rounds',rounds)
        zz=int(w[rounds-15],2)
        cc=int(w[rounds-2],2)
        s1a1=check_b(bin(rotate_r(bin(cc),17)))
        s1a2=check_b(bin(rotate_r(bin(cc),19)))
        s1a3=shift_right((check_b(bin(cc))),10)
        #if check_b(bin(cc))=='01100001011000100110001110000000':
            #s1a1=check_b(bin(834678961))
            #s1a2=check_b(bin(1282411564))
        if rounds==31:
            print('  ',cc,(zz))
            #print(w[27])
            #print(int(s1a1,2),int(s1a2,2),int(s1a3,2))
        #print(s1a1,check_32(str(s1a1)),'\n',s1a2,check_32(str(s1a2)),'\n',s1a3,check_32(str(s1a3)))
        #print('cc',cc,check_32(str(cc)),'\nzz',zz,check_32(str(zz)))
        s0a1=check_b(bin(rotate_r(bin(zz),7)))
        s0a2=check_b(bin(rotate_r(bin(zz),18)))
        s0a3=shift_right(check_b(bin(zz)),3)
        s0a=check_b(str(bin(int(s0a1,2)^int(s0a2,2)^int(s0a3,2))))
        s1a=check_b(str(bin(int(s1a1,2)^int(s1a2,2)^int(s1a3,2))))
        #s0=check_b(s0a)
        #s1=check_b(s1a)
        if rounds==31:
            print((s0a1),'     ',int(s0a2,2),'      ',int(s0a3,2))
            print('s0a',int(s0a,2),check_32(str(s0a)),'\ns1a',int(s1a,2),check_32(str(s1a)))
            #print('w-16',int(w[rounds-16],2),check_32(str(w[rounds-16])),'\nw-7',w[rounds-7],check_32(str(w[rounds-7])))
        xb=(int(w[rounds-16],2)+int(s0a,2)+int(w[rounds-7],2)+int(s1a,2))
        if rounds==31:
            print('xb',bin(xb))         
        xa=check_b(bin(xb))
        #if rounds==16 or rounds==17:
           # print('xa',xa,check_32(str(xa)))
        '''for i in range(len(xa)):
            if xa[i]!='b':
                xb.append(xa[i])
        xc=''.join(map(str,xb))
        xaa=str(mod32_add([int(xc)]))
        xa=check_b(bin(int(xaa)))'''
        if rounds==31:
            print('xa',xa)
        w.append(xa)
        
        si1a=rotate_r(bin(e),6)
        si1b=rotate_r(bin(e),11)
        si1c=rotate_r(bin(e),25)
        #print(si1a,si1b,si1c)
        #if rounds==19:
            #print(si1a,si1b,si1c)
        '''print(e,f,g)
            print(int(e)&int(f))
            print((~int(e))&int(g))
            print((int(e)&int(f))^((~int(e))&int(g)))'''
        ch=((int(e)&int(f))^((~int(e))&int(g)))
        ma=((int(a)&int(b))^(int(a)&int(c))^(int(b)&int(c)))
        si0=(((rotate_r(bin(a),2))^(rotate_r(bin(a),13)))^(rotate_r(bin(a),22)))
        #print(si1a^si1b)
        si1=si1a^si1b^si1c
        #print(si1)
        #if rounds<3:
            #print(int(w[rounds],2))
            #print(e)
        if rounds==31:
            print('                                 ',int(k[rounds]),((w[rounds])))
        temp1=mod32_add([int(si1),int(h),int(ch),int(k[rounds]),int(str(w[rounds]),2)])
        #if rounds<16:
            #print(rotate_r(bin(e),6))
            #print(int(si1),int(k[rounds]))
            #print(int(h)+int(si1)+int(ch)+int(k[rounds]))+int(x))
        temp2=mod32_add([int(si0),int(ma),int(temp1)])
            
        if rounds>=30 and rounds<32:
            print("ma=",ma," e0=",si0," Ch=",ch," e1=",si1)
            print(int(a)," ",int(b)," ",int(c)," ",int(d)," ",int(e)," ",int(f)," ",int(g)," ",int(h))
            #print(xa)
            print(temp1)
        h=g
        g=f
        f=e
        e=mod32_add([d,temp1])
        d=c
        c=b
        b=a
        a=temp2

        rounds+=1

        
        
        
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

print(H10," ",H11," ",H12," ",H13," ",H14," ",H15," ",H16," ",H17)


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

