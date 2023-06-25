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