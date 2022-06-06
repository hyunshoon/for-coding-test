N = int(input())
inp_li = list(map(int, input().split(' ')))

order_dict = {}
for i in range(len(inp_li)):
    order_dict[i] = inp_li[i]

order_li = sorted(order_dict.items(), key= lambda x: x[1])

pre = order_li[0][1]
cnt = 0
for i in range(len(order_li)):
    if order_li[i][1] == pre: # 이전 숫자가 현재 숫자와 같으면 동일 숫자 부여
        order_li[i] = [order_li[i][0],cnt]
    else:
        cnt+=1
        pre = order_li[i][1]
        order_li[i] = [order_li[i][0],cnt]

order_print = sorted(order_li, key = lambda x:x[0])
result = ''
for order in order_print:
    result+=str(order[1])+' '
print(result)