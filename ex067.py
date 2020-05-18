while True:
    print('-x'*30)
    n = int(input('Qer ver a tabuada de qual numero?: '))
    print('-x' * 30)
    if n < 0:
        break
    m = 1
    while m < 11:#for c in range(1 , 11) como alternativa dessa forma dispensando o m = 1 e m += 1
        r = n * m
        print(f'{n} x {m:2.0f} = {r:2.0f}')
        m += 1
print('=+'*30)
print('Acabou')
