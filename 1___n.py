"""
Created on Thu Aug 15 11:34:16 2019

@author: Dakshveer Singh Chauhan
"""
"""matrix Master 2.0"""


import tkinter as tk 


class matrix:
    
    def show(X):         #function to print martix 
        for i in X:
            for j in i:
                print(j,end='   ')
            print()
    
        
    def emp(x,y):       #function to generate empty nested lists with 
        C=matrix.empty(x)      #
        for i in range(x):
            for j in range(y):
                C[i].append(0)
        return(C)
    def empty(n):#Creates a empty matrix with specified rows
        X=[]
        for t in range(n):
            X.append([])
        return(X)
    
    
    def empty_t(W):
        a,b,c=matrix.order(W)
        E=matrix.emp(a,b)
        for i in range(a):
            for j in range(b):
                E[i][j]+=0
        return(E)
                
    
    #Martix Checking
    def check(A):
        l=len(A[0])
        #print(l)
        for i in A:
            if len(i)==l:
                pass
            else:
                return(False)
                break
        else:
            return(True)
            """Checking """
            
    def order(A):
        if matrix.check(A)==True:
            a=len(A[0])
            b=0
            for j in A:
                b+=1
            return(b,a,"{}x{}".format(b,a))
        else:
            raise(Exception("Martix is invalid"))
            
            
    def issq(W):
        if matrix.check(W)==True:
            if len(W)==len(W[0]):
                return(True)
            else:
                return(False)
    
                
    def index_print(A):
        for i in range(matrix.order(A)[0]):
            for j in range(matrix.order(A)[1]):
                print(i,j,end='     ')
            print()
                
                
    def add(A,B):
        if matrix.order(A)==matrix.order(B):
            ''' '''      
            C=matrix.empty(matrix.order(A)[0])
            
            for h in [t for t in range(matrix.order(A)[0])]:
                for j in [t for t in range(matrix.order(A)[1])]:
                    C[h].append(A[h][j]+B[h][j])
            return(C)
                    #print(h,j,end='  ')
                #print()
    def sub(A,B):
        if matrix.order(A)==matrix.order(B):
            ''' will fill elements in null matrix of desired order'''      
            C=matrix.empty(matrix.order(A)[0])
            
            for h in [t for t in range(matrix.order(A)[0])]:
                for j in [t for t in range(matrix.order(A)[1])]:
                    C[h].append(A[h][j]-B[h][j])
            return(C)
    
    def transpose(Z):
        
        C=matrix.emp(matrix.order(Z)[1],matrix.order(Z)[0])
        for i in range(1,1+len(Z)):
            # iterate through columns
            for j in range(1,1+len(Z[0])):
                C[j-1][i-1] = Z[i-1][j-1]
        return(C)
        
    def mul(A,B):
        if matrix.order(A)[1]==matrix.order(B)[0]:
            C=matrix.emp(matrix.order(A)[0],matrix.order(B)[1])
            for i in range(len(A)):#iterating through rows of A
                for j in range(len(B[0])):#iterating through columns of B
                    for k in range(len(B)):#iterating through rows of B
                        C[i][j]+=A[i][k]*B[k][j]
            return(C)
                
        else:
            raise(Exception("Unsuitable order of matrices for multiplication"))
        
                    
    """ Now we head to check some basic types of matrices their checking"""
    
    #Generating indentity matrix
    
    def gen_identity(n):
        C=matrix.emp(n,n)
        for i in range(matrix.order(C)[0]):
            for j in range(matrix.order(C)[1]):
                if i==j:
                    C[i][j]=1
                else:
                    C[i][j]=0
        return(C)
        
    def is_identity(Q):
        if matrix.issq(Q)==True:
            for i in range(len(Q)):
                for j in range(len(Q)):
                    if i==j:
                        if Q[i][j]==1:
                            pass
                        else:
                            break
                    else:
                        if Q[i][j]==0:
                            pass
                        else:
                            break
                else:
                    continue
                break
            else:
                return(True)
                
    def is_uppertrianglar(Q):
        if matrix.issq(Q)==True:
            for i in range(len(Q)):
                for j in range(len(Q)):
                    if i>j:
                        if Q[i][j]==0:
                            pass
                        else:
                            break
                    else:
                        if Q[i][j]!=0:
                            pass
                        else:
                            break
                else:
                    continue
                break
            else:
                return(True)
                    
    def is_lowertriangular(Q):
        if matrix.issq(Q)==True:
            for i in range(len(Q)):
                for j in range(len(Q)):
                    if i<j:
                        if Q[i][j]==0:
                            pass
                        else:
                            break
                    else:
                        if Q[i][j]!=0:
                            pass
                        else:
                            break
                else:
                    continue
                break
            else:
                return(True)
                    
    def is_null(M):
        for i in range(len(M)):
                for j in range(len(M)):
                    if M[i][j]==0:
                        pass
                    else:
                        break
                else:
                    continue
                break
        else:
            return(True)
            
    def power(A,n):
        if n==1:
            return(A)
        else:
            return(matrix.mul(A,matrix.power(A,n-1)))
            
    def is_idempotent(A):
        if matrix.mul(A,A)==A:
            return(True)
        else:
            return(False)
            
            
    def is_involutry(A):
        if matrix.is_identity(matrix.mul(A,A)):
            return(True)
        else:
            return(False)
            
            
    def is_orthagonal(A):
        if matrix.is_identity(matrix.mul(A,matrix.transpose(A)))==True:
            return(True)
        else:
            return(False)
        
                        
    """ Now dertminant functions"""
    
    def minor(M,i,j):
        return([row[:j]+row[j+1:] for row in (M[:i]+M[i+1:])])
        
        
    def cofactor(M,i,j):
        return(((-1)**(i+j))*matrix.det(matrix.minor(M,i,j)))
        
    def det(A):
        if matrix.issq(A)==True:
            if matrix.order(A)[0]==1:
                return(A[0][0])
            if matrix.order(A)[0]==2:
                return(A[0][0]*A[1][1]-A[0][1]*A[1][0])
            
            else:
                c=0
                for a in range(len(A)):
                    c+=((-1)**a)*(A[0][a])*matrix.det(matrix.minor(A,0,a))
                return(c)
            
                
    def adj(M):
        if matrix.issq(M)==True:
            if matrix.order(M)[0]==1:
                return(M)
            else:
                C=matrix.emp(matrix.order(M)[0],matrix.order(M)[0])
                for i in range(len(M)):
                    for j in range(len(M)):
                        C[i][j]=matrix.cofactor(M,i,j)
                return(matrix.transpose(C))
            
    def mulsca(m,M): 
        C=matrix.empty_t(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                #print(i,j)
                C[i][j]=m*M[i][j]
        return(C)
        
                
    def inverse(M):
        return(matrix.mulsca(1/matrix.det(M),matrix.adj(M)))


class dtls:
    def __init__(self,root):
        self.root=root
        
        
        
        self.Canvas1 = tk.Canvas(self.root,height=200,width=800)
        #self.Canvas1.create_image(310+(newImageSizeWidth)/2,newImageSizeHeight/2,image = self.img)      
        self.Canvas1.config(bg='blue',width =500, height = 150)
        self.Canvas1.create_arc(10,10,150,150,start=45,extent=260,fill="Red",outline="yellow",width=2)
        self.Canvas1.grid(row=0,column=0,columnspan=6,sticky=tk.EW)
        self.la1=tk.Label(self.root,text="Hello",bg="Yellow",width=10)
        self.la1.grid(row=1,column=0,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.root,text="Hello",bg="Orange",fg="White",width=10)
        self.la1.grid(row=1,column=5,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.root,text="Welcome to Details Page",bg="Red",height=7)
        self.la1.grid(row=1,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.root,text="All rights reserved",bg="Black",fg='white')
        self.la1.grid(row=15,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.root,bg='light blue',text="Details Page")
        self.la1.grid(row=2,column=1,columnspan=4,sticky=tk.EW)
        tk.Label(self.root).grid(row=3,column=1)
        
        self.fr1=tk.Frame(self.root)
        self.la1=tk.Label(self.fr1,text='Very felicific to present Matrix Master 2.0 ',bg='ivory2')
        self.la1.grid(row=0)
        self.la1=tk.Label(self.fr1,text=' ',bg='ivory2')
        self.la1.grid(row=1)
        self.la1=tk.Label(self.fr1,text='It would be a sin not to acknowledge the support of family and teachers',bg='ivory2')
        self.la1.grid(row=2)
        self.la1=tk.Label(self.fr1,text='and friends(Yash and Rishi) who showered constructive feedbacks.',bg='ivory2')
        self.la1.grid(row=3)
        self.la1=tk.Label(self.fr1,text=' ',bg='ivory2')
        self.la1.grid(row=4)
        self.la1=tk.Label(self.fr1,text='Thank you all for your support and guidence and valuable time',bg='ivory2')
        self.la1.grid(row=5)
        self.la1=tk.Label(self.fr1,text='',bg='ivory2')
        self.la1.grid(row=6)
        self.la1=tk.Label(self.fr1,text='To all esteemed , feel free to mail me for suggestion or faults on\n',bg='ivory2')
        self.la1.grid(row=7)
        self.la1=tk.Label(self.fr1,text='       dakshveersinghchauhan@gmail.com',bg='ivory3')
        self.la1.grid(row=8)
        self.la1=tk.Label(self.fr1,text=' ',bg='ivory2')
        self.la1.grid(row=9)
        self.la1=tk.Label(self.fr1,text='',bg='ivory2')
        self.la1.grid(row=10)
        
        
        
        self.la1=tk.Label(self.fr1,text='- Dakshveer Singh Chauahn',bg='ivory3')
        self.la1.grid(row=11,sticky=tk.E)
        self.la1=tk.Label(self.fr1,text='{ a noob programmer}',bg='ivory3')
        self.la1.grid(row=12,sticky=tk.E)
        
        tk.Button(self.fr1,text='   EXIT   ',bg='red',command=self.root.destroy).grid(row=15)
        
        self.fr1.grid(row=4,column=1)
        
        
        """click and drag"""
        self.root.overrideredirect(True)
        self.root._offsetx = 0
        self.root._offsety = 0
            
        self.root.bind('<Button-1>',self.clickwin)
        self.root.bind('<B1-Motion>',self.dragwin)
        
             
        
    def dragwin(self,event):
            x = self.root.winfo_pointerx() - self.root._offsetx
            y = self.root.winfo_pointery() - self.root._offsety
            self.root.geometry('+{X}+{Y}'.format(X=x,Y=y))
    
    def clickwin(self,event):
            self.root._offsetx = event.x
            self.root._offsety = event.y

class instr:
    def __init__(self,root):
        self.root=root
        
        
        
        self.Canvas1 = tk.Canvas(self.root,height=200,width=800)
        #self.Canvas1.create_image(310+(newImageSizeWidth)/2,newImageSizeHeight/2,image = self.img)      
        self.Canvas1.config(bg='blue',width =500, height = 150)
        self.Canvas1.create_arc(10,10,150,150,start=45,extent=260,fill="Red",outline="yellow",width=2)
        self.Canvas1.grid(row=0,column=0,columnspan=6,sticky=tk.EW)
        self.la1=tk.Label(self.root,text="Hello",bg="Yellow",width=10)
        self.la1.grid(row=1,column=0,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.root,text="Hello",bg="Orange",fg="White",width=10)
        self.la1.grid(row=1,column=5,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.root,text="Welcome to Details Page",bg="Red",height=7)
        self.la1.grid(row=1,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.root,text="All rights reserved",bg="Black",fg='white')
        self.la1.grid(row=15,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.root,bg='light blue',text="Instructions Page")
        self.la1.grid(row=2,column=1,columnspan=4,sticky=tk.EW)
        tk.Label(self.root).grid(row=3,column=1)
        
        self.fr1=tk.Frame(self.root)
        self.la1=tk.Label(self.fr1,text='Trying to present conspectus of instructions\nfor further information contact us.',bg='ivory2')
        self.la1.grid(row=0)
        self.la1=tk.Label(self.fr1,text=' ',bg='ivory2')
        self.la1.grid(row=1)
        self.la1=tk.Label(self.fr1,text='1 : Order is to be entered like ( m x n) ',bg='ivory2')
        self.la1.grid(row=2,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='2 : You can either "press enter" or press "Refresh" to generate matrix',bg='ivory2')
        self.la1.grid(row=3,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='3 : For defaults and scalar factor press enter{twice for confimation} to lock values',bg='ivory2')
        self.la1.grid(row=4,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='4 : For moving in one box just use arrow keys',bg='ivory2')
        self.la1.grid(row=5,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='5 : For moving focus to near box use shift+repective arrow key',bg='ivory2')
        self.la1.grid(row=6,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='',bg='ivory2')
        self.la1.grid(row=7,sticky=tk.W)
        self.la1=tk.Label(self.fr1,text='To all esteemed , feel free to mail me for suggestion or faults on\n',bg='ivory2')
        self.la1.grid(row=8)
        self.la1=tk.Label(self.fr1,text='       dakshveersinghchauhan@gmail.com',bg='ivory3')
        self.la1.grid(row=9)
        self.la1=tk.Label(self.fr1,text=' ',bg='ivory2')
        self.la1.grid(row=10)
        self.la1=tk.Label(self.fr1,text='',bg='ivory2')
        self.la1.grid(row=11)
        
        
        
        self.la1=tk.Label(self.fr1,text='- Dakshveer Singh Chauahn',bg='ivory3')
        self.la1.grid(row=11,sticky=tk.E)
        self.la1=tk.Label(self.fr1,text='{ a noob programmer}',bg='ivory3')
        self.la1.grid(row=12,sticky=tk.E)
        
        tk.Button(self.fr1,text='   EXIT   ',bg='red',command=self.root.destroy).grid(row=15)
        
        self.fr1.grid(row=4,column=1)
        
        
        """click and drag"""
        self.root.overrideredirect(True)
        self.root._offsetx = 0
        self.root._offsety = 0
            
        self.root.bind('<Button-1>',self.clickwin)
        self.root.bind('<B1-Motion>',self.dragwin)
        
             
        
    def dragwin(self,event):
            x = self.root.winfo_pointerx() - self.root._offsetx
            y = self.root.winfo_pointery() - self.root._offsety
            self.root.geometry('+{X}+{Y}'.format(X=x,Y=y))
    
    def clickwin(self,event):
            self.root._offsetx = event.x
            self.root._offsety = event.y

        
class Home:
    def __init__(self,master):
        self.master=master
        self.master.deiconify()
    
        self.ca=tk.Canvas(self.master,bg="Light Blue",height=75)
        self.ca.create_arc(5,5,70,70,start=45,extent=260,fill="Red",outline="yellow",width=2)
        self.ca.create_text(350,30,text="  MATRIX  MASTER 2.0 ",font=("Helvetica",25))
        self.ca.grid(row=0,column=0,columnspan=7,sticky=tk.EW)
        self.la1=tk.Label(self.master,text="Hello",bg="Yellow",width=10)
        self.la1.grid(row=1,column=0,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.master,text="Hello",bg="Orange",fg="White",width=10)
        self.la1.grid(row=1,column=5,sticky=tk.NS,rowspan=14)
        self.la1=tk.Label(self.master,text="Welcome to Martix Master",bg="Red",height=2)
        self.la1.grid(row=1,column=1,columnspan=5,sticky=tk.EW)
        self.la1=tk.Label(self.master,text="All rights reserved",bg="Black",fg='white')
        self.la1.grid(row=15,column=1,columnspan=7,sticky=tk.EW)
        self.frm=tk.Frame(self.master)
        
        tk.Label(self.frm,bg='darkorchid2',text='COMMON OPERATIONS').grid(row=0,column=0)
        self.b1=tk.Button(self.frm,command=self.main_mul,text='MULTIPLY')
        self.b1.grid(row=1,column=0)
        self.laam=tk.Label(self.frm)
        self.laam.grid(row=1,column=1)
        self.b1=tk.Button(self.frm,command=self.main_add,text='ADD')
        self.b1.grid(row=2,column=0)
        self.laaa=tk.Label(self.frm)
        self.laaa.grid(row=2,column=1)
        self.b1=tk.Button(self.frm,command=self.main_sub,text='SUBTRACT')
        self.b1.grid(row=3,column=0)
        self.laas=tk.Label(self.frm)
        self.laas.grid(row=3,column=1)
        tk.Label(self.frm).grid(row=4,column=0)
        self.b2=tk.Button(self.frm,text='Details',command=self.dtls_)
        self.b2.grid(row=5,column=0)
        self.b2=tk.Button(self.frm,text='Instructions',command=self.instr_)
        self.b2.grid(row=6,column=0)
        self.frm.grid(row=5,column=3)
        #self.la1=tk.Label(self.master,bg='light blue',text="Main Page")
        #self.la1.grid(row=2,column=1,columnspan=3,sticky=tk.EW)
        #tk.Label(self.master).grid(row=3,column=1)
        
        self.la1=tk.Label(self.master,text='First Matrix',bg='darkorchid3')
        self.la1.grid(row=4,column=1,sticky=tk.EW)
        
        
        self.fr1=tk.Frame(self.master)
        
        """First matrix and its fellow"""
        self.la=tk.Label(self.fr1,text="Enter order of first Matrix:")
        self.la.grid(row=0,column=0)
        global omat1
        omat1=tk.Entry(self.fr1,bg='yellow')
        omat1.bind('<Return>',self.refresh1_s)
        omat1.grid(row=0,column=1)
        self.errmat1=tk.Label(self.fr1)
        self.errmat1.grid(row=0,column=3)
        self.b1=tk.Button(self.fr1,text='Refresh',command=self.refresh1)
        self.b1.grid(row=0,column=2)
        self.matr1=tk.Frame(self.fr1)
        self.matr1.grid(row=1,column=0)
        self.fr11=tk.Frame(self.fr1)
        self.b1=tk.Button(self.fr11,command=self.inst_iden1,text='Insert identity')
        self.b1.grid(row=0,column=0)
        self.b1=tk.Button(self.fr11,command=self.print1,text='Print')
        self.b1.grid(row=1,column=0)
        self.b1=tk.Button(self.fr11,command=self.clear1,text='Clear')
        self.b1.grid(row=2,column=0)
        self.b2=tk.Button(self.fr11,command=self.intc_,text='Interchange')
        self.b2.grid(row=3,column=0)
        tk.Label(self.fr11,text='          ').grid(row=0,column=1,rowspan=7)
        self.la1=tk.Label(self.fr11,text='CHECKINGS',bg='grey')
        self.la1.grid(row=0,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i1_1,text='Identity')
        self.b2.grid(row=1,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i2_1,text='Involutry')
        self.b2.grid(row=2,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i3_1,text='Idempotent')
        self.b2.grid(row=3,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i4_1,text='Orthagonal')
        self.b2.grid(row=4,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i5_1,text='Singular')
        self.b2.grid(row=5,column=2,ipadx=5)
        self.b2=tk.Button(self.fr11,command=self.i6_1,text='Determinant')
        self.b2.grid(row=6,column=2,ipadx=5)
        
        tk.Label(self.fr11,text='         ').grid(row=0,column=3,rowspan=7)
        tk.Label(self.fr11,bg='grey',text=' Get ').grid(row=0,column=4)
        self.b2=tk.Button(self.fr11,command=self.inv_1,text='Inverse')
        self.b2.grid(row=1,column=4)
        self.b2=tk.Button(self.fr11,command=self.adj_1,text='Adjoint')
        self.b2.grid(row=2,column=4)
        self.b2=tk.Button(self.fr11,command=self.trns_1,text='Transpose')
        self.b2.grid(row=3,column=4)
        self.fr11.grid(row=1,column=1)
        self.matr11=tk.Frame(self.fr1)
        self.la4=tk.Label(self.matr11)
        self.la4.grid()
        self.matr11.grid(row=2,column=0)
        self.fr111=tk.Frame(self.fr1)
        tk.Label(self.fr111,text='Default:').grid(row=0,column=0)
        tk.Label(self.fr111,text='Scalar:').grid(row=1,column=0)
        self.e_def1=tk.Entry(self.fr111)
        self.e_def1.bind('<Return>',self._def1)
        self.e_def1.grid(row=0,column=1)
        self.e_scf1=tk.Entry(self.fr111)
        self.e_scf1.bind('<Return>',self._scf1)
        self.e_scf1.grid(row=1,column=1)
        self.fr111.grid(row=3,column=0)
        
        self.fr1.grid(row=5,column=1)
        tk.Label(self.master,bg='yellow',text=' ').grid(row=5,column=2,rowspan=5,sticky=tk.NS)
        
        
        tk.Label(self.master).grid(row=6,column=1)
        
        
        
        self.la1=tk.Label(self.master,text='Second Matrix',bg='darkorchid3')
        self.la1.grid(row=7,column=1,sticky=tk.EW)
        
        
        
        self.fr2=tk.Frame(self.master)
        """Second matrix and its fellow"""
        self.la=tk.Label(self.fr2,text="Enter order of second Matrix:")
        self.la.grid(row=0,column=0)
        self.omat2=tk.Entry(self.fr2,bg='yellow')
        self.omat2.bind('<Return>',self.refresh2_s)
        self.omat2.grid(row=0,column=1)
        self.b1=tk.Button(self.fr2,text='Refresh',command=self.refresh2)
        self.b1.grid(row=0,column=2)
        
        self.matr2=tk.Frame(self.fr2)
        self.matr2.grid(row=1,column=0)
        self.fr22=tk.Frame(self.fr2)
        self.b2=tk.Button(self.fr22,command=self.inst_iden2,text='Insert identity')
        self.b2.grid(row=0,column=0)
        self.b2=tk.Button(self.fr22,command=self.print2,text='Print')
        self.b2.grid(row=1,column=0)
        self.b2=tk.Button(self.fr22,command=self.clear2,text='Clear')
        self.b2.grid(row=2,column=0)
        
        tk.Label(self.fr22,text='          ').grid(row=0,column=1,rowspan=7)
        self.la2=tk.Label(self.fr22,text='CHECKINGS',bg='grey')
        self.la2.grid(row=0,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i2_2,text='Identity')
        self.b2.grid(row=1,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i2_2,text='Involutry')
        self.b2.grid(row=2,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i3_2,text='Idempotent')
        self.b2.grid(row=3,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i4_2,text='Orthagonal')
        self.b2.grid(row=4,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i5_2,text='Singular')
        self.b2.grid(row=5,column=2,ipadx=5)
        self.b2=tk.Button(self.fr22,command=self.i6_2,text='Determinant')
        self.b2.grid(row=6,column=2,ipadx=5)
        
        tk.Label(self.fr22,text='         ').grid(row=0,column=3,rowspan=7)
        tk.Label(self.fr22,bg='grey',text=' Get ').grid(row=0,column=4)
        self.b2=tk.Button(self.fr22,command=self.inv_2,text='Inverse')
        self.b2.grid(row=1,column=4)
        self.b2=tk.Button(self.fr22,command=self.adj_2,text='Adjoint')
        self.b2.grid(row=2,column=4)
        self.b2=tk.Button(self.fr22,command=self.trns_2,text='Transpose')
        self.b2.grid(row=3,column=4)
        
        self.fr22.grid(row=1,column=1)
        self.matr22=tk.Frame(self.fr2)
        self.la5=tk.Label(self.matr22)
        self.la5.grid()
        self.matr22.grid(row=2,column=0)
        
        self.fr222=tk.Frame(self.fr2)
        tk.Label(self.fr222,text='Default:').grid(row=0,column=0)
        tk.Label(self.fr222,text='Scalar:').grid(row=1,column=0)
        self.e_def2=tk.Entry(self.fr222)
        self.e_def2.bind('<Return>',self._def2)
        self.e_def2.grid(row=0,column=1)
        self.e_scf2=tk.Entry(self.fr222)
        self.e_scf2.bind('<Return>',self._scf2)
        self.e_scf2.grid(row=1,column=1)
        self.fr222.grid(row=3,column=0)
        
        
        self.fr2.grid(row=8,column=1)
        
        
        
        
        
        self.frans=tk.Frame(self.master)
        """Third Matrix and its fellow"""
       
            
        self.ca=tk.Canvas(self.frans,bg="Light Blue",height=80)
        self.ca.create_arc(10,10,50,50,start=45,extent=260,fill="Red",outline="yellow",width=2)
        self.ca.create_text(170,30,text="  Matrix Master 2.0 ",font=("Helvetica",20))
        self.ca.grid(row=0,column=0,columnspan=6,sticky=tk.EW)
        self.la1=tk.Label(self.frans,text="Hello",bg="Yellow",width=10)
        self.la1.grid(row=1,column=0,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.frans,text="Hello",bg="Orange",fg="White",width=10)
        self.la1.grid(row=1,column=5,sticky=tk.NS,rowspan=15)
        self.la1=tk.Label(self.frans,text="Welcome to Martix Master 2.0",bg="Red",height=7)
        self.la1.grid(row=1,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.frans,text="All rights reserved",bg="Black",fg='white')
        self.la1.grid(row=15,column=1,columnspan=4,sticky=tk.EW)
        self.la1=tk.Label(self.frans,bg='light blue',text="ANSWER WINDOW")
        self.la1.grid(row=2,column=1,columnspan=3,sticky=tk.EW)
        tk.Label(self.frans).grid(row=3,column=1)
    
        
            
        self.matr_a=tk.Frame(self.frans)
        self.matr_a.grid(row=4,column=1)
       
        
        self.fr2=tk.Frame(self.frans)
        self.b1=tk.Button(self.fr2,text='Insert at 1',command=self.at_1)
        self.b1.grid(row=0,column=0)
        self.b1=tk.Button(self.fr2,text='Insert at 2',command=self.at_2)
        self.b1.grid(row=1,column=0)
        self.b1=tk.Button(self.fr2,text='Print',command=self.print_a)
        self.b1.grid(row=2,column=0)
        
        self.fr2.grid(row=4,column=2)
      
            
        
        self.frans.grid(row=5,column=10,rowspan=5)
        
        
        """Main master stuff"""
        self.b2=tk.Button(self.master, width=15,text='Exit', command=self.dest_all,bg='red')
        self.b2.grid(row=13,column=1)
        self.master.overrideredirect(True)
        self.master._offsetx = 0
        self.master._offsety = 0
        
        self.master.bind('<Button-1>',self.clickwin)
        self.master.bind('<B1-Motion>',self.dragwin)
        
        
        
    """FIRST matrix's FUNCTIONS """
    def get_order1(self):
        data=omat1.get()
        
        c=''
        for i in data.split():
            c+=i
        r1=c.split('x')[0]
        c1=c.split('x')[1]
    
        if len(c)>=3:
            return(int(r1),int(c1))
        else:
            print("Invalid Order")
        
    
    def refresh1(self):
        ro,co=self.get_order1()
        print(ro,co)
        print(type(ro))
        for widget in self.matr1.winfo_children():
            widget.destroy()
        self.instmatof1(self.matr1,ro,co)
        self.rows_1=ro
        self.colu_1=co
        
    
    def refresh1_s(self,event):
        ro,co=self.get_order1()
        print(ro,co)
        print(type(ro))
        for widget in self.matr1.winfo_children():
            widget.destroy()
        self.instmatof1(self.matr1,ro,co)
        self.rows_1=ro
        self.colu_1=co
        
    def instmatof1(self,widget,r,c):
        rows=0
        for i in range(1,int(r)+1):
            for j in range(1,int(c)+1):
                #print(ro,j)
                inst='me_{}_{}'.format(i,j)
                
                self.identify(inst,tk.Entry(widget,width=5))
                eval(inst).name=inst
                eval(inst).bind('<Shift-Left>',self.left)
                eval(inst).bind('<Shift-Right>',self.right)
                eval(inst).bind('<Shift-Up>',self.up)
                eval(inst).bind('<Shift-Down>',self.down)
                eval(inst).grid(row=rows,column=j)
                # yASS YAAS YAAAS 
            rows+=1
            
    def clear1(self):
        ro=self.rows_1
        co=self.colu_1
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                inst='me_{}_{}'.format(i,j)
                eval(inst).delete(0,tk.END)
                
    def inst_matr1(self,M):
        ro,co=matrix.order(M)[0],matrix.order(M)[1]
        omat1.delete(0,tk.END)
        omat1.insert(tk.END,'{}x{}'.format(ro,co))
        self.refresh1()
        #if (ro==matrix.order(M)[0]) and (co==matrix.order(M)[1]):
        for i in range(1,int(ro)+1):
              for j in range(1,int(co)+1):
                    val=M[i-1][j-1]
                    inst='me_{}_{}'.format(i,j)
                    eval(inst).insert(tk.END,val)
                    
    
    def print1(self):
        L=self.get_matr1()
        self.inst_matr_a(L)
        
    def get_matr1(self):
        ro,co=self.get_order1()
        M=matrix.emp(int(ro),int(co))
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                res=(eval('me_{}_{}'.format(i,j))).get()
                if res=='':
                    try:
                        print(self.default1)
                        res=self.default1 
                    except:
                        print('not called')
                        res=0#Later we will change it to self.def_val
                M[i-1][j-1]=eval(str(res))
            #matrix.show(M)
        try:
            print(self.scalar1)
            return(matrix.mulsca(self.scalar1,M))
        except:
            return(matrix.mulsca(1,M))
    def inst_iden1(self):
        if self.rows_1 == self.colu_1:
            M=matrix.gen_identity(self.rows_1)
            self.clear1()
            self.inst_matr1(M)
            
    def i1_1(self):
        M=self.get_matr1()
        if matrix.is_identity(M):
            self.la4.configure(bg='green',text="is identity")
        else:
            self.la4.configure(bg='red',text="is not identity")
            
    def i2_1(self):
        M=self.get_matr1()
        if matrix.is_involutry(M):
            self.la4.configure(bg='green',text="is involutry")
        else:
            self.la4.configure(bg='red',text="is not involutry")
            
    def i3_1(self):
        M=self.get_matr1()
        if matrix.is_idempotent(M):
            self.la4.configure(bg='green',text="is idempotent")
        else:
            self.la4.configure(bg='red',text="is not idempotent")
    def i4_1(self):
        M=self.get_matr1()
        if matrix.is_orthagonal(M):
            self.la4.configure(bg='green',text="is orthagonal")
        else:
            self.la4.configure(bg='red',text="is not orthgonal")
    
    def i5_1(self):
        M=self.get_matr1()
        if matrix.det(M)!=0:
            self.la4.configure(bg='green',text="is singular")
        else:
            self.la4.configure(bg='red',text="is not singular")
            
    def i6_1(self):
        M=self.get_matr1()
        self.la4.configure(bg='green',text="Det={}".format(str(matrix.det(M))))
    
    def inv_1(self):
        L=self.get_matr1()
        if matrix.det(L)==0:
            self.la4.configure(bg='red',text="Inverse doesn't exists")
        else:
            self.la4.configure(bg='ivory2',text='')
            self.inst_matr_a(matrix.inverse(L))
        
    def adj_1(self):
        L=matrix.adj(self.get_matr1())
        self.inst_matr_a(L)
    
    def trns_1(self):
        L=matrix.transpose(self.get_matr1())
        self.inst_matr_a(L)
        
    def _def1(self,event):
        a=self.e_def1.get()
        if a=='':
            self.default1=0
        else:
            self.default1=eval(a)
        
    def _scf1(self,event):
        a=self.e_scf1.get()
        if a=='':
            self.scalar1=1
        else:
            self.scalar1=eval(a)
        
    """SECOND matrix's FUNCTIONS"""
    def get_order2(self):
        data=self.omat2.get()
        
        c=''
        for i in data.split():
            c+=i
        r1=c.split('x')[0]
        c1=c.split('x')[1]
    
        if len(c)>=3:
            return(int(r1),int(c1))
        else:
            print("Invalid Order")
        
   # @staticmethod
    def refresh2(self):
        ro,co=self.get_order2()
        print(ro,co)
        print(type(ro))
        for widget in self.matr2.winfo_children():
            widget.destroy()
        self.instmatof2(self.matr2,ro,co)
        self.rows_2=ro
        self.colu_2=co
    
    def refresh2_s(self,event):
        ro,co=self.get_order2()
        print(ro,co)
        print(type(ro))
        for widget in self.matr2.winfo_children():
            widget.destroy()
        self.instmatof2(self.matr2,ro,co)
        self.rows_2=ro
        self.colu_2=co
        
    def instmatof2(self,widget,r,c):
        rows=0
        for i in range(1,int(r)+1):
            for j in range(1,int(c)+1):
                #print(ro,j)
                inst='mee_{}_{}'.format(i,j)
                self.identify(inst,tk.Entry(widget,width=5))
                eval(inst).grid(row=rows,column=j)
                eval(inst).name=inst
                eval(inst).bind('<Shift-Left>',self.left)
                eval(inst).bind('<Shift-Right>',self.right)
                eval(inst).bind('<Shift-Up>',self.up)
                eval(inst).bind('<Shift-Down>',self.down)
                eval(inst).grid(row=rows,column=j)
                # yASS YAAS YAAAS 
            rows+=1
            
    def clear2(self):
        ro=self.rows_2
        co=self.colu_2
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                inst='mee_{}_{}'.format(i,j)
                eval(inst).delete(0,tk.END)
                
    def inst_matr2(self,M):
        ro,co=matrix.order(M)[0],matrix.order(M)[1]
        self.omat2.delete(0,tk.END)
        self.omat2.insert(tk.END,'{}x{}'.format(ro,co))
        self.refresh2()
        #if (ro==matrix.order(M)[0]) and (co==matrix.order(M)[1]):
        for i in range(1,int(ro)+1):
              for j in range(1,int(co)+1):
                    val=M[i-1][j-1]
                    inst='mee_{}_{}'.format(i,j)
                    eval(inst).insert(tk.END,val)
       
    def print2(self):
        L=self.get_matr2()
        self.inst_matr_a(L)
        
    def get_matr2(self):
        ro,co=self.get_order2()
        M=matrix.emp(int(ro),int(co))
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                res=(eval('mee_{}_{}'.format(i,j))).get()
                if res=='':
                    try:
                        print(self.default2)
                        res=self.default2
                    except:
                        print('not called')
                        res=0
                M[i-1][j-1]=eval(str(res))
            #matrix.show(M)
        try:
            print(self.scalar2)
            return(matrix.mulsca(self.scalar2,M))
        except:
            return(matrix.mulsca(1,M))
        
    def inst_iden2(self):
        if self.rows_2 == self.colu_2:
            M=matrix.gen_identity(self.rows_2)
            self.clear2()
            self.inst_matr2(M)
            
            
    def _def2(self,event):
        a=self.e_def2.get()
        if a=='':
            self.default2=0
        else:
            self.default2=eval(a)
        
    def _scf2(self,event):
        a=self.e_scf2.get()
        self.scalar2=eval(a)
        
    def i1_2(self):
        M=self.get_matr2()
        if matrix.is_identity(M):
            self.la5.configure(bg='green',text="is identity")
        else:
            self.la5.configure(bg='red',text="is not identity")
            
    def i2_2(self):
        M=self.get_matr2()
        if matrix.is_involutry(M):
            self.la5.configure(bg='green',text="is involutry")
        else:
            self.la5.configure(bg='red',text="is not involutry")
            
    def i3_2(self):
        M=self.get_matr2()
        if matrix.is_idempotent(M):
            self.la5.configure(bg='green',text="is idempotent")
        else:
            self.la5.configure(bg='red',text="is not idempotent")
    def i4_2(self):
        M=self.get_matr2()
        if matrix.is_orthagonal(M):
            self.la5.configure(bg='green',text="is orthagonal")
        else:
            self.la5.configure(bg='red',text="is not orthgonal")
    
    def i5_2(self):
        M=self.get_matr2()
        if matrix.det(M)!=0:
            self.la5.configure(bg='green',text="is singular")
        else:
            self.la5.configure(bg='red',text="is not singular")
            
    def i6_2(self):
        M=self.get_matr2()
        self.la5.configure(bg='green',text="Det = {}".format(str(matrix.det(M))))
    
    def inv_2(self):
        L=self.get_matr2()
        if matrix.det(L)==0:
            self.la5.configure(bg='red',text="Inverse doesn't exists")
        else:
            self.la5.configure(bg='ivory2',text='')
            self.inst_matr_a(matrix.inverse(L))
        
    def adj_2(self):
        L=matrix.adj(self.get_matr2())
        self.inst_matr_a(L)
    
    def trns_2(self):
        L=matrix.transpose(self.get_matr2())
        self.inst_matr_a(L)
    
    
    
    """ANSWER MATRIX FUNCTIONS"""
    def set_order_a(self,ro,co):
        self.rows_a=ro
        self.colu_a=co
        
    def get_order_a(self):
      
            return(int(self.rows_a),int(self.colu_a))

        
    
    def refresh_a(self):
        ro,co=self.get_order_a()
        print(ro,co)
        print(type(ro))
        for widget in self.matr_a.winfo_children():
            widget.destroy()
        self.instmatof_a(self.matr_a,ro,co)
        
        
    
        
    def instmatof_a(self,widget,r,c):
        rows=0
        for i in range(1,int(r)+1):
            for j in range(1,int(c)+1):
                #print(ro,j)
                inst='means_{}_{}'.format(i,j)
                
                self.identify(inst,tk.Entry(widget,width=5))
                eval(inst).name=inst
                eval(inst).bind('<Shift-Left>',self.left)
                eval(inst).bind('<Shift-Right>',self.right)
                eval(inst).bind('<Shift-Up>',self.up)
                eval(inst).bind('<Shift-Down>',self.down)
                eval(inst).grid(row=rows,column=j)
                # yASS YAAS YAAAS 
            rows+=1
            
    def clear_a(self):
        ro=self.rows_a
        co=self.colu_a
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                inst='means_{}_{}'.format(i,j)
                eval(inst).delete(0)
                
    def inst_matr_a(self,M):
        ro,co=matrix.order(M)[0],matrix.order(M)[1]
        
        self.set_order_a(ro,co)
        self.refresh_a()
        #if (ro==matrix.order(M)[0]) and (co==matrix.order(M)[1]):
        for i in range(1,int(ro)+1):
              for j in range(1,int(co)+1):
                    val=M[i-1][j-1]
                    inst='means_{}_{}'.format(i,j)
                    eval(inst).insert(tk.END,val)
                    
    
    def print_a(self):
        L=self.get_matr_a()
        print(L)
        
    def get_matr_a(self):
        ro,co=self.get_order_a()
        M=matrix.emp(int(ro),int(co))
        for i in range(1,int(ro)+1):
            for j in range(1,int(co)+1):
                res=(eval('means_{}_{}'.format(i,j))).get()
                if res=='':
                    print(self.default1)
                    res=self.default1   #Later we will change it to self.def_val
                M[i-1][j-1]=eval(str(res))
            #matrix.show(M)
        return(M)
    
    
    def at_1(self):
        L=self.get_matr_a()
        print(L)
        self.inst_matr1(L)
    
    def at_2(self):
        L=self.get_matr_a()
        print(L)
        self.inst_matr2(L)
    """COMMON FUNCTIONS FROM HERE"""
        
    def dest_all(self):
        try:
            
            self.ans.destroy()
            self.master.destroy()
        except:
         
            self.master.destroy()
            
    def main_mul(self):
        print('multiplication called')
        print("first's order ( {}x{} )".format(self.rows_1,self.colu_1))
        print("second's order ( {}x{} )".format(self.rows_2,self.colu_2))
        if self.colu_1==self.rows_2:
            self.laam.configure(bg='ivory2',text='')
            L=self.get_matr1()
            M=self.get_matr2()
            AN=matrix.mul(L,M)
            self.inst_matr_a(AN)
        else:
            self.laam.configure(bg='red',text='Invalid Order\nfor Mul')
            
    def main_add(self):
        print('addition called')  
        print("first's order ( {}x{} )".format(self.rows_1,self.colu_1))
        print("second's order ( {}x{} )".format(self.rows_2,self.colu_2))
        if (self.rows_1==self.rows_2)  and (self.colu_1==self.colu_2):
            print('Done')
            self.laaa.configure(bg='ivory2',text='')
            L=self.get_matr1()
            M=self.get_matr2()
            AN=matrix.add(L,M)
            self.inst_matr_a(AN)
        else:
            self.laaa.configure(bg='red',text='Invalid Order\nfor ADD')
            
    def main_sub(self):
        print('subtraction called')
        print('addition called')  
        print("first's order ( {}x{} )".format(self.rows_1,self.colu_1))
        print("second's order ( {}x{} )".format(self.rows_2,self.colu_2))
        if (self.rows_1==self.rows_2)  and (self.colu_1==self.colu_2):
            print('Done')
            self.laas.configure(bg='ivory2',text='')
            L=self.get_matr1()
            M=self.get_matr2()
            AN=matrix.sub(L,M)
            self.inst_matr_a(AN)
        else:
            self.laas.configure(bg='red',text='Invalid Order\nfor ADD')
        
    def identify(self,var,val):
            globals()[var]=val    
    
    def dragwin(self,event):
        x = self.master.winfo_pointerx() - self.master._offsetx
        y = self.master.winfo_pointery() - self.master._offsety
        self.master.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self.master._offsetx = event.x
        self.master._offsety = event.y
        
    def dtls_(self):
        root1 = tk.Tk()
        app=dtls(root1)
        root1.mainloop()    
        
    def instr_(self):
        
        root1 = tk.Tk()
        app=instr(root1)
        root1.mainloop()
        
    def intc_(self):
        L=self.get_matr1()
        M=self.get_matr2()
        self.inst_matr1(M)
        self.inst_matr2(L)
        
        
    """LEFT RIGHT UP DOWN shift functions"""
        
    def left_shift(self,string):
        a=string
        b=a.split('_')
        c=b.pop(0)
        return("{}_{}_{}".format(c,b[0],int(b[1])-1))
        
    def right_shift(self,string):
        a=string
        b=a.split('_')
        c=b.pop(0)
        return("{}_{}_{}".format(c,b[0],int(b[1])+1))
        
    def up_shift(self,string):
        a=string
        b=a.split('_')
        c=b.pop(0)
        return("{}_{}_{}".format(c,int(b[0])-1,int(b[1])))
        
    def down_shift(self,string):
        a=string
        b=a.split('_')
        c=b.pop(0)
        return("{}_{}_{}".format(c,int(b[0])+1,int(b[1])))
        
    #@staticmethod 
    def left(self,event):
        print('left clicked')
        a=self.left_shift(self.master.focus_get().name)
        print('shift focus to',a)
        print(type(a))
        print(type(eval(a)))
        
        eval(a).focus_set()
        
        
    def right(self,event):
        print('right clicked')
        a=self.right_shift(self.master.focus_get().name)
        print('shift focus to',a)
        print(type(a))
        print(type(eval(a)))
        
        eval(a).focus_set()
        
    def up(self,event):
        print('up clicked')
        a=self.up_shift(self.master.focus_get().name)
        print('shift focus to',a)
        print(type(a))
        print(type(eval(a)))
        
        eval(a).focus_set()
        
    def down(self,event):
        print('down clicked')
        a=self.down_shift(self.master.focus_get().name)
        print('shift focus to',a)
        print(type(a))
        print(type(eval(a)))
        
        eval(a).focus_set()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
t=tk.Tk()
r=Home(t)
t.mainloop()