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
                                sda=size_data3

                                I=0
                                while I!=1000:
                                    I+=1
                                    SDA3=""
                                    lenf3=len(sda2)
                                    Clock=0
                                    long111=len(sda)
                                            
                                                
                                    while Clock<long111:
                                                    sda12=""
                                                    sda12=sda[Clock:Clock+1]
                                                    
                                                    if sda12=="1":
                                                        sda1=sda[Clock+1:Clock+21]

                                                        DR=2**24
                                                        sda11=""

                                                        while sda1!=sda3:
                                                            DR-=1
                                                            
                                                        
                                                            if assxw3==0:

                                                                
                                                                #DR=11140083
                                                                sda11=format(DR,'024b')
                                                                sda2=sda11
                                                            lenf2=len(sda2)  
                                                            block3=0
                                                            sda3=""
                                                            sda5=""
                                                            sda8=""
                                                            sda4=""
                                                            
                                                            count3+=1
                                                            #print(count4)
                                                            #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                                            #print(len(sda2))
                                                            F=0
                                                            B=0
                                                            count4=-1
                                                         
                                                            lenf2=len(sda2)
                                                            #print(lenf2)
                                                            N2=-1
                                                            N1=1
                                                            N5=0
                                                            long2=1
                                                            
                                                            N8=len(sda2)
                                                            while N1!=0:
                                                                N2+=1
                                                                long=len(sda2)
                                                                long2=long-N2
                                                                if long2<=0:
                                                                    B=1
                                                                    N1=0
                                                                if B==0:
                                                                    N=int(sda2[:long-N2],2)
                                                                    if N==0:
                                                                        B=1
                                                                        N1=0
                                                                    N5=N//((2**4)-1)
                                                                    N1=N%((2**4)-1)
                                                                #print(N2)
                                                            Bias=bin(N5)[2:]
                                                            if N5==0:
                                                                B=1
                                                            long61=len(Bias)
                                                            long62=0
                                                            if B==0:
                                                                long62=len(sda2[long-N2:])
                                                            NS=long61
                                                            NS1=N8-long62
                                                            NS2=NS1-1-long61
                                                            Nj=len(bin(N2)[2:])
                                                            #print(N2)
                                                            if Nj>(2**5)-1:
                                                                B=1
                                                            
                                                            
                                                            
                                                            C="0"+str((2**5)-1)+"b"
                                                            if assxw3==0:

                                                                N1=1
                                                                N5=0
                                                                N6=0
                                                                N11=2**16
                                                               
                                                                
                                                             
                                                            
                                                                
                                                                while N6!=1:
                                                                        N11-=1
                                                                        #print(N11)
                                                                
                                                                        long=len(sda2)
                                                                    
                                                                        
                                                                        N=int(sda2,2)
                                                                        if N==0:
                                                                                N11=1
                                                                                N6=1	                                    
                                                                        if N11==0:
                                                                                N11=(2**16)-1
                                                                 
                                                                        N5=N//(N11)
                                                                        
                                                                        N1=N%(N11)
                                                                        
                                                                Bias=bin(N5)[2:]
                                                                Bias2=format(N2,C)
                                                                
                                                                
                                                                
                                                                
                                                                                    
                                                            Bias3=format(N2,C)
                                                                   
                                                       
                                                            if B==0:
                                                                if assxw3==0:
                                                                    sda3="1"+Bias+sda2
                                                                else:
                                                                    sda3="1"+Bias+sda2[long-N2:]
                                                            #print(N2)
                                                            if B==1:
                                                                if assxw3==0:
                                                                    sda3="0"+Bias+sda2
                                                                else:
                                                                    sda3="0"+Bias+sda2[long-N2:]
                                                                
                                                            
                                                            sda8=""
                                                            Circle=0
                                                            Long888=len(sda3)
                                                            while Circle<Long888:
                                                              if sda3[Circle:Circle+1]=="0":
                                                                
                                                                sda8=sda8+"1"
                                                              if sda3[Circle:Circle+1]=="1":  
                                                                sda8=sda8+"0"
                                                              Circle+=1

                                                            sda3=sda8
                                                            sda2=sda3
                                                            #print(len(sda3))
                                                            #n = int(sda2, 2)
                                                                                                                            
                                                                    
                                                            #n = int(sda2, 2)                                                                                     
                                                                    
                                                            #qqwslenf=len(sda2)
                                                            #qqwslenf=(qqwslenf/8)*2
                                                            #qqwslenf=str(qqwslenf)
                                                            #qqwslenf="%0"+qqwslenf+"x"
                                                            #jl=binascii.unhexlify(qqwslenf % n)
                                                            #print(len(jl))
                                                            #
                                                            #
                                                            #print(len(jl))
                                                            
                                                            assxw3+=1  
                                                            if assxw3==2**15:
                                                                #print(Bias2)

                                                                sda3=Bias3+Bias2+sda3
                                                                sda6=sda3
                                                                
                                                                
                                                                
                                                                T4=format(N11,'016b')
                                                                
                                                                
                                                                sda3=T4+sda3

                                                                sda3="1"+sda3
                                                                lenf=len(sda3)
                                                                add_bits118=""
                                                                count_bits=20-lenf%20
                                                                z=0
                                                                if count_bits!=20:
                                                                    while z<count_bits:
                                                                            add_bits118="0"+add_bits118
                                                                            z=z+1
                                                                    sda3=add_bits118+sda3
                                                                
                                                                #print(len(sda3))
                                                                #print(sda3)

                                                                #print(sda11)
                                                                #print(len(sda1))
                                                                #print(sda1)
                                                                
                                                                assxw3=0

                                                        
                                                        SDA3=SDA3+sda11    
                                                        Clock+=21
                                                        #print("F")
                                                    else:
                                                        sda1=sda[Clock+1:Clock+25]
                                                        SDA3=SDA3+sda1
                                                        Clock+=25
                                                    

                                                    #print(sda3)
                                                        
                                                    
                                    sda=SDA3                                                                                                                                                    
											                                                                                            
											                                                                                            
                                            
                                assxw1=1    
                                    #print(assxw)
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

                                        while I!=1000:
                                            I+=1
                                            SDA3=""
                                            
                                            lenf3=len(sda2)
                                            Clock=0
                                            long111=len(sda)

                                            
                                            
                                                
                                            while Clock<long111:
                                                    sda1=sda[Clock:Clock+24]
                                                    
                                                    if assxw3==0:
                                                        sda2=sda1
                                                    lenf2=len(sda2)  
                                                    block3=0
                                                    sda3=""
                                                    sda5=""
                                                    sda8=""
                                                    sda4=""
                                                    
                                                    count3+=1
                                                    #print(count4)
                                                    #######################################################Jurijus Pacalovas Exection Program######################################################################################
                                                    #print(len(sda2))
                                                    F=0
                                                    B=0
                                                    count4=-1
                                                 
                                                    lenf2=len(sda2)
                                                    #print(lenf2)
                                                    N2=-1
                                                    N1=1
                                                    N5=0
                                                    long2=1
                                                    
                                                    N8=len(sda2)
                                                    while N1!=0:
                                                        N2+=1
                                                        long=len(sda2)
                                                        long2=long-N2
                                                        if long2<=0:
                                                            B=1
                                                            N1=0
                                                        if B==0:
                                                            N=int(sda2[:long-N2],2)
                                                            if N==0:
                                                                B=1
                                                                N1=0
                                                            N5=N//((2**4)-1)
                                                            N1=N%((2**4)-1)
                                                        #print(N2)
                                                    Bias=bin(N5)[2:]
                                                    if N5==0:
                                                        B=1
                                                    long61=len(Bias)
                                                    long62=0
                                                    if B==0:
                                                        long62=len(sda2[long-N2:])
                                                    NS=long61
                                                    NS1=N8-long62
                                                    NS2=NS1-1-long61
                                                    Nj=len(bin(N2)[2:])
                                                    #print(N2)
                                                    if Nj>(2**5)-1:
                                                        B=1
                                                    
                                                    
                                                    
                                                    C="0"+str((2**5)-1)+"b"
                                                    if assxw3==0:

                                                        N1=1
                                                        N5=0
                                                        N6=0
                                                        N11=2**16
                                                       
                                                        
                                                     
                                                    
                                                        
                                                        while N6!=1:
                                                                N11-=1
                                                                #print(N11)
                                                        
                                                                long=len(sda2)
                                                            
                                                                
                                                                N=int(sda2,2)
                                                                if N==0:
                                                                        N11=1
                                                                        N6=1	                                    
                                                                if N11==0:
                                                                        N11=(2**16)-1
                                                         
                                                                N5=N//(N11)
                                                                
                                                                N1=N%(N11)
                                                                
                                                         
                                                           
                                                          
                                                                                                   
                                                                #print(N5)
                                                                if N1==0 and N5!=0:
                                                                        N6=1
                                                                Bias=bin(N5)[2:]
                                                        Bias2=format(N2,C)
                                                        
                                                        
                                                        
                                                        
                                                                            
                                                    Bias3=format(N2,C)
                                                           
                                               
                                                    if B==0:
                                                        if assxw3==0:
                                                            sda3="1"+Bias+sda2
                                                        else:
                                                            sda3="1"+Bias+sda2[long-N2:]
                                                    #print(N2)
                                                    if B==1:
                                                        if assxw3==0:
                                                            sda3="0"+Bias+sda2
                                                        else:
                                                            sda3="0"+Bias+sda2[long-N2:]
                                                    
                                                    sda8=""
                                                    Circle=0
                                                    Long888=len(sda3)
                                                    while Circle<Long888:
                                                      if sda3[Circle:Circle+1]=="0":
                                                        
                                                        sda8=sda8+"1"
                                                      if sda3[Circle:Circle+1]=="1":  
                                                        sda8=sda8+"0"
                                                      Circle+=1

                                                    sda3=sda8
                                                    sda2=sda3
                                                    #print(len(sda3))
                                                    #n = int(sda2, 2)
                                                                                                                    
                                                            
                                                    #n = int(sda2, 2)                                                                                     
                                                            
                                                    #qqwslenf=len(sda2)
                                                    #qqwslenf=(qqwslenf/8)*2
                                                    #qqwslenf=str(qqwslenf)
                                                    #qqwslenf="%0"+qqwslenf+"x"
                                                    #jl=binascii.unhexlify(qqwslenf % n)
                                                    #print(len(jl))
                                                    #
                                                    #
                                                    #print(len(jl))
                                                    
                                                    assxw3+=1  
                                                    if assxw3==2**15:
                                                        #print(Bias2)

                                                        sda3=Bias3+Bias2+sda3
                                                        sda6=sda3
                                                        
                                                        
                                                        T4=format(N11,'016b')
                                                       
                                                        
                                                        
                                                        sda3=T4+sda3

                                                        sda3="1"+sda3
                                                        lenf=len(sda3)
                                                        add_bits118=""
                                                        count_bits=20-lenf%20
                                                        z=0
                                                        
                                                        while z<count_bits:
                                                                add_bits118="0"+add_bits118
                                                                z=z+1
                                                        sda3=add_bits118+sda3
                                                        Clock+=24
                                                        #print(len(sda6))
                                                        if len(sda3)!=20:
                                                            sda3="0"+sda1#25
                                                        else:
                                                            sda3="1"+sda3#21
                                                        #print(sda3)
                                                        SDA3=SDA3+sda3
                                                        
                                                        
                                                        assxw3=0
                                
                                            sda=SDA3
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
