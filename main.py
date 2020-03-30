def TransStrIntoInt(s : str):
    a = s.split('.')
    num = 0
    for i in range(4):
        num = num * (1 << 8) + int(a[i])
    return num

def display(num : int):
    digit = [0] * 4
    
    for i in range(3, -1, -1):
        digit[i] = num % 256
        num //= 256

    return '.'.join(map(str, digit))
def SplitNetwork(ip: int, subMark : int, n : int):
    
    # last bit we have to borrow
    lastBit = 0

    for i in range(32):
        if not ((1 << i) & subMark):
            lastBit += 1
        else:
            break
    
    lastBit += 1
    
    # first bit we have to borrow
    # we borrow bits from beginBit to lastBit inorder to create new net address
    beginBit = lastBit - 1

    while (1 << (lastBit - beginBit)) < n:
        beginBit -= 1

    ans = []
    
    if beginBit < 0:
        return ans
    
    for i in range(n):
        cur = ip
        for j in range(beginBit, lastBit):
            if (1 << (j - beginBit)) & i:
                cur |= (1 << j)
        ans.append(cur)
        cur += (1 << beginBit) - 1
        ans.append(cur)
    
    return ans
        
s = input()
t = input()
n = int(input())

# convert ip address and submark into interger
ip = TransStrIntoInt(s)
subMark = TransStrIntoInt(t)

# split net into n subnet
ans = SplitNetwork(ip, subMark, n)

if not len(ans):
    print("Impossible")
else:
    for i in range(n):
        print('Subnet {0}:'.format(i))
        print('\tNetaddress: {0}'.format(display(ans[2 * i])))
        print('\tBoradcast address: {0}'.format(display(ans[2 * i + 1])))
        print('\tSubMark of subnet: {0}'.format(display((1 << 32) - 1 - ans[2 * i + 1] + ans[2 * i])))
        print('\tMax host can connect: {0}'.format(ans[2 * i + 1] - ans[2 * i] - 2))
