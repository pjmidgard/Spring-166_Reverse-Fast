from time import time
cvf=0
import os
import binascii
namez = input("c  for compress or e for extract: ")
#@Author Jurijus Pacalovas
class compression:
    def cryptograpy_compression(self):
                

        
            
    
                self.name = "@Author: Jurijus Pacalovas"
                print(self.name)
                if namez=="e":
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                           print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit                    
                    namea=""
                    namem=""
                    namema="?"
                    Times_of_compression1=0
                    blockw=5
                    blockw1=4
                    assxw1=0
                    assxw2=0
                    block2=0
                    sda4=""
                        
                    count1=12
                    count2=0
                    count3=0
                    count4=-1
                    count6=0
                    assxw1=0
                    assxw3=0
                    Times_of_compression=0
                    assxw2=0
              

                    assxw=0
                    blockw=5
                    blockw1=4
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    
                    nac=len(nameas)

                    Times_of_compression=0
                    
                    countraz=0
                    assxw=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    count4=-1
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=2
                    block2=0

                    count_time_of_copression=0
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                       
                    sda3=""

                    sscvf=0
                        
                    qqqqwzl=0

                    block=0

                    x=0
                    x1=0
                    x2=0
                    x = time()

            
                    
                    with open(nameas, "w") as f4:
                            f4.write(s)
                   
                    with open(name, "rb") as binary_file:

           
                  
                        # Read the whole file at once
                        
                        data = binary_file.read()
                        
                    
                        
                        s=str(data)
                        
            
                  
                        lenf1=len(data)
                        lenf5=len(data)
                        
            
                  
                        
                        if lenf1>((2**32)-1)+((2**24)-1):
                            print("This file is too big");
                            raise SystemExit
                        if lenf1==0:
                            
                            raise SystemExit

                        assx=0
                        qqqwz=0
                        
            
                   
                        while assx<10:
                       
                            aas1=0
                            a1=0

                
           
                    
                            cvf=cvf+1
                            
                
                    
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

      
                                    
                                    
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                    
                                
                                    
                                    if countraz==1:

                                        
                                        
                                        

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1


                                    
                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)

                                Number_save2=int(sda[:32],2)
                                sda=sda[32:]
                                


                                size_data3=sda
                                if size_data3[0:9]=="000000001":
                                    size_data3=size_data3[9:]
                                elif size_data3[0:8]=="00000001":
                                    size_data3=size_data3[8:]
                                elif size_data3[0:7]=="0000001":
                                    size_data3=size_data3[7:]
                                elif size_data3[0:6]=="000001":
                                    size_data3=size_data3[6:]
                                elif size_data3[0:5]=="00001":
                                    size_data3=size_data3[5:]
                                elif size_data3[0:4]=="0001":
                                    size_data3=size_data3[4:]
                                elif size_data3[0:3]=="001":
                                    size_data3=size_data3[3:]
                                elif size_data3[0:2]=="01":
                                    size_data3=size_data3[2:]
                                elif size_data3[0:1]=="1":
                                    size_data3=size_data3[1:]
                                
                                
                                sda2=size_data3
                                #print(sda2)
                                sda=size_data3

                                I=0

                                while I!=1:
                                            I+=1
                                            SDA3=""
                                            
                                            lenf3=len(sda2)
                                            Clock=0
                                            long111=len(sda)
                                            lenf116=Number_save2

                                            
                                            SDA4=sda[lenf116:]
                                            #print(lenf116)
                                                
                                            while Clock<lenf116:
                                                    
                                                    
                                                    
                                                    sda14=sda[Clock:Clock+1]
                                                    Clock+=1
                                                    if sda14=="0":
                                                            sda12=sda[Clock:Clock+22]
                                                            
                                                            
                                                            Number_compress_or_not=int(sda12,2)
                                                                
                                                            Number_compress_or_not=-Number_compress_or_not
                                                            Number_compress_or_not+=2**24
                                                            Number_compress_or_not1=Number_compress_or_not
                                                            Number_save=format(Number_compress_or_not1,'024b')
                                                            sda3=Number_save
                                                            Clock+=22
                                                            #print(len(sda3))
                                                            
                                                                
                                                                
                                                                
                                                            #print(len(sda3))
                                                            #os.system("pause")
                                                    elif sda14=="1":
                                                            sda12=sda[Clock:Clock+23]
                                                           
                                                            sda3="0"+sda12
                                                            #print(len(sda3))
                                                            Clock+=23
                                                            
                                                        
                                                                
                                                            
                                                        
                                                            
                                                    
                                                    
                                                        
                                                    
                                                    
                                                              
                                                    SDA3=SDA3+sda3
                                                    
                                                        
                                            sda=SDA3+SDA4        
                                        
                                assxw=1
                                    
                                if assxw==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(sda2)
                                        #os.system("pause")
                                        
                                        
                                            
               
                                        n = int(SDA3, 2)
                                        qqwslenf=len(SDA3)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        assxw1=1
                                     
                                            
                                            
                                            #print(assxw1)
                                            
                                        if assxw1==1:
                                        
                                                assx=10
                                                if assx==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)                                  

                           
    
            
    def cryptograpy_unpack(self):                       
                    if namez=="c":
                        name = input("What is name of file? ")
                        if os.path.exists(name):
                           print('Path is exists!')
                        else:
                            print('Path is not exists!')
                            raise SystemExit
                        namea=""
                        namem=""
                        namema="?"
                        block2=0
                        
                        count1=12
                        count2=0
                        count3=0
                        count4=-1
                        count6=0
                        assxw1=0
                        assxw3=0
                        Times_of_compression=0
                        assxw2=0
              

                        assxw=0
                        blockw=5
                        blockw1=4
                        nameas=name
                        
                        nac=len(nameas)

                        long=len(name)
                   
                        name_cut=len(".bin")
                    
                        nameas=name+".bin" 
                        countraz=0
                        cvf=2
                        cvf1=0
                        s=""
                        e2=0
                        e3=2
                        e4=""
                        c=2
                        sw=2
                        elw=0
                       
                        sda3=""

                        sscvf=0
                        
                        qqqqwzl=0

                        block=0

                        x=0
                        x1=0
                        x2=0
                        x = time()
                       
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            
                            data = binary_file.read()

                        
                            s=str(data)
                            lenf1=len(data)
                            lenf5=len(data)
                            
                            if lenf1>(2**32)-1:
                                print("This file is too big");
                                raise SystemExit
                            if lenf1==0:
                            	raise SystemExit
                            
                            assx=0
                            
                            qqqwz=0
                            while assx<10:
                          
                                aas1=0
                                a1=0
                                
                                cvf=cvf+1
                                
                                countraz=countraz+1

                                with open(nameas, "ab") as f2:
                                    if countraz==1:
                                        sda=bin(int(binascii.hexlify(data),16))[2:]
                                        lenf=len(sda)
                                        
                                        lenf1=len(data) 
                                        xc=(lenf1*8)-lenf
                                        z=0
                                        if xc!=0:
                                            while z<xc:
                                                sda="0"+sda
                                                z=z+1
                                        sda2=sda

                                        
                                            
                                        
                                       
                                        
                                        #print(I)
                                        I=0

                                        while I!=1:
                                            I+=1
                                            SDA3=""
                                            
                                            lenf3=len(sda2)
                                            Clock=0
                                            long111=len(sda)

                                        
                                            lenf112=lenf1//240
                                            lenf114=lenf112*240
                                            #print(lenf114)
                                            
                                            
                                            
                                            SDA4=sda[lenf114*8:]     
                                            while Clock<lenf114*8:
                                                    sda12=sda[Clock:Clock+24]
                                                    

                                                    Number_compress_or_not=int(sda12,2)
                                                    Number_compress_or_not2=Number_compress_or_not
                                                    if Number_compress_or_not>=2**23 and len(sda12)==24:
                                                        Number_compress_or_not-=2**24
                                                        Number_compress_or_not=-Number_compress_or_not
                                                        Number_save=format(Number_compress_or_not,'022b')
                                                        sda3="01"+Number_save[1:]
                                                        
                                                        if len(sda3)!=23:
                                                            sda3=sda12#10
                                                            if sda12[:2]!="10":
                                                                raise SystemExit
                                                        else:
                                                            sda3="0"+Number_save#23
                                                            Number_compress_or_not=-Number_compress_or_not
                                                            Number_compress_or_not+=2**24
                                                            Number_compress_or_not1=Number_compress_or_not
                                                            #print(sda3)
                                                            if Number_compress_or_not2!=Number_compress_or_not1:
                                                                raise SystemExit
                                                            
                                                            
                                                            
                                                        #print(len(sda3))
                                                        #os.system("pause")
                                                    elif Number_compress_or_not<2**23 and len(sda12)==24:
                                                        Number_compress_or_not+=2**24
                                                        
                                                        Number_save=format(Number_compress_or_not,'022b')
                                                        sda3="00"+Number_save
                                                        #print(len(sda3))
                                                        if len(sda3)!=24:
                                                            sda3="1"+sda12[1:]#0-1#24
                                                            if sda12[:1]!="0":
                                                                raise SystemExit
                                                                
                                                            
                                                        else:
                                                            raise SystemExit
                                                            
                                                    else:
                                                        sda3="1"+sda12

                                                        #print(sda3)
                                                    
                                                        
                                                    
                                                    
                                                              
                                                    SDA3=SDA3+sda3
                                                    Clock+=24
                                                        
                                            lenf116=len(SDA3)   
                                            sda=SDA3+SDA4
                                    assxw=1
                                    #print(assxw)
                                    if assxw==1:
                                        

                                        
                                        
                                        
                                        
#######################################################Jurijus Pacalovas Exection Program######################################################################################
                                        #2**32#
                                        #print(sda2)
                                        #os.system("pause")
                                        SDA3="1"+SDA3
                                        lenf=len(SDA3)
                                        add_bits118=""
                                        count_bits=8-lenf%8
                                        z=0
                                        if count_bits!=8:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                        SDA3=add_bits118+SDA3
                                        

                                        Number_save1=format(lenf116,'032b')
                                            
                                        SDA3=Number_save1+SDA3
                                        n = int(SDA3, 2)
                                        qqwslenf=len(SDA3)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        #
                                        #
                                        #print(len(jl))
                                            
                                      
                                        assxw1=1
                                     
                                            
                                            
                                            #print(assxw1)
                                            
                                        if assxw1==1:
                                        
                                                assx=10
                                                if assx==10:
                                                       

                                                       
                                                   
                                                       
                                                    f2.write(jl)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)        
                                                                                  														    
                                         



   



            
                     

d=compression()


  
xw=d.cryptograpy_compression()
print(xw)


xw1=d.cryptograpy_unpack()
print(xw1)
