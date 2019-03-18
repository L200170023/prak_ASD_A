##NAMA : ILHAM ATHUR B.W
##NIM : L200170023
##KELAS : A

##NO.1
d = [[3,4],[5,6]]
e = [[1,2],[7,8]]
f = [[13,4,"x","y"],[13,33,3]]
g = [[3,4],[1,4],[2,5]]
h = [[1,2,3],[6,7,8]]
i = [[1,2,3],[4,5,6],[7,8,9]]

def cekCek(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
           z+=1
    if(z == len(n)):
        print("matrik tsb konsisten")
    else:
        print("matrik tsb tidak konsisten")
cekCek(d)
cekCek(e)
cekCek(f)

def cekInt(n):
    x = 0
    y = 0
    for i in n:
        for j in i:
            y+=1
            if (str(j).isdigit()==False):
                print("tidak semua isi matriks adalah angka")
                break
            else:
                x+=1
    if(x==y):
        print("semua isi matriks adalah angka")
cekInt(d)
cekInt(e)
cekInt(f)

def ordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    print("punya ordo "+str(x)+"x"+str(y))
ordo(d)
ordo(e)
ordo(f)
ordo(g)

def jml(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")
jml(d,e)
jml(d,f)
   
     
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("dapat dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("belum memenuhi syarat")
zz = [[1,2,3],[1,2,3]]
zx = [[1],[2],[3]]
kali(zz,zx)
kali(d,e)
kali(d,g)
kali(d,zx)


def detHitung(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    else:
        return "tidak bisa dihitung determinan, bukan matrix bujursangkar"
    return total
z = [[3,1],[2,5]]
x = [[1,2,1],[3,3,1],[2,1,2]]
v = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
r = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]
print(detHitung(z))
print(detHitung(x))
print(detHitung(v))
print(detHitung(r))
print(detHitung(g))
print(detHitung(h))

##NO.2
def ciptNol(n,m=None):
    if(m==None):
        m=n
    print("menciptakan matrix 0 dengan ordo "+str(n)+"x"+str(m))
    print([[0 for j in range(m)] for i in range(n)])

ciptNol(5,6)
ciptNol(4)

def ciptIden(n):
    print("menciptakan matrix identitas dengan ordo"+str(n)+"x"+str(n))
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])
ciptIden(6)
ciptIden(3)

##NO.3
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList: 
    def __init__(self): 
        self.head = None
    def pushAw(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
    def pushAk(self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return self.head
    def insert(self,data,pos):
        node = Node(data)
        if not self.head:
            self.head = node
        elif pos==0:
            node.next = self.head
            self.head = node
        else:
            prev = None
            current = self.head
            current_pos = 0
            while(current_pos < pos) and current.next:
                prev = current
                current = current.next
                current_pos +=1
            prev.next = node
            node.next = current
        return self.head
    def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
        if temp is None: 
            return 
        if temp.next is None: 
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def search(self, x): 
        current = self.head 
        while current != None: 
            if current.data == x: 
                return "True"
            current = current.next
        return "False"
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next   
    
llist = LinkedList() 
llist.pushAw(31)
llist.pushAw(32)
llist.pushAw(22)
llist.pushAw(24)
llist.pushAw(2)
llist.pushAw(29)
llist.pushAk(9)
llist.deleteNode(0)
llist.insert(1,6)
print(llist.search(31))
print(llist.search(39))
llist.display()

##NO.4
class DNode(object):
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
def cetakkedepan(mulai):
    current=soal
    while(current.prev!=None):
        print(current)
        current=current.next
def cetakkebelakang(mulai):
    current=soal
    while(current.prev!=None):
        print(current)
        current=current.prev
def tambahdepan(soal,penambah):
    current=soal
    while(current.prev!=None):
        current=current.prev
    current.prev=penambah
def tambahbelakang(soal,penambah):
    current=soal
    while(current.prev!=None):
        current=current.next
    current.next=penambah

a=Matrix(2,2)
a[0]=[5,1]
a[1]=[-3,3]
g=Matrix(4,4)
g[0]=[4,5,2,8]
g[1]=[6,4,2,5]
g[2]=[9,3,2,3]
g[3]=[1,2,2,1]
b=Matrix(2,2)
b[0]=[1,3]
b[1]=[2,9]
c=a+b
d=a*b
e=Matrix.identity(4)
f=Matrix.identity(3)
print(f.det())
print(b.det())
print(g.det())
print(c)
print(d)
print(e)
a=Node(10,Node(20,Node(30,Node(40,Node(50)))))
a.tambah(5)


a.kunjungi()
