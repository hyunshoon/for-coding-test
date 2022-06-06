# int -> str 후 각 자리수에서 체크
N = int(input())
n_li = [0] *10
for n in range(1,N+1):
  number = str(n)
  for s in number:
    if s == '0':
      n_li[0] += 1
    elif s == '1':
      n_li[1] += 1
    elif s == '2':
      n_li[2] += 1
    elif s == '3':
      n_li[3] += 1
    elif s == '4':
      n_li[4] += 1
    elif s == '5':
      n_li[5] += 1
    elif s == '6':
      n_li[6] += 1
    elif s == '7':
      n_li[7] += 1
    elif s == '8':
      n_li[8] += 1
    elif s == '9':
      n_li[9] += 1


result = ''
for n in n_li:
    result += str(n) + ' '
print(result)
