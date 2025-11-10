def solve(n):
        res=[]
        board=[]
        c=set()
        pos=set()
        neg=set()
        def trial(i):
            if len(board)==n:
                res.append(board.copy())
                return
            for j in range(n):
                if j not in c and i+j not in pos and i-j not in neg:
                    s="."*j+"Q"+"."*(n-j-1)
                    board.append(s)
                    c.add(j)
                    pos.add(i+j)
                    neg.add(i-j)
                    trial(i+1)
                    c.remove(j)
                    pos.remove(i+j)
                    neg.remove(i-j)
                    board.remove(s)
            return
        trial(0)
        return res
n = int(input("Enter the number of queens: "))
solutions = solve(n)
for i in solutions:
    for j in i:
        print(j)
    print()