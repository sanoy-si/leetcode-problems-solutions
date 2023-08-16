if __name__ == '__main__':
    N = int(input())
    lis = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            lis.insert(int(command[1]),int(command[2]))
        elif command[0] == 'print':print(lis)
        elif command[0] == 'remove':lis.remove(int(command[1]))
        elif command[0] == 'append':lis.append(int(command[1]))
        elif command[0] == 'sort':lis.sort()
        elif command[0] == 'pop':lis.pop()
        else:lis.reverse()
        
        
        
