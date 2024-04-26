for i in range (2, 10, 4):
    if 2 <= i <= 5:
        for j in range (1, 10):
            print(f'{i} x {j} = {i*j:2d}', end = '    ')
            print(f'{i+1} x {j} = {(i+1)*j:2d}', end = '    ')
            print(f'{i+2} x {j} = {(i+2)*j:2d}', end = '    ')
            print(f'{i+3} x {j} = {(i+3)*j:2d}')

    
    if 5 <= i <= 9:
        print()
        for j in range (1, 10):
            print(f'{i} x {j} = {i*j:2d}', end = '    ')
            print(f'{i+1} x {j} = {(i+1)*j:2d}', end = '    ')
            print(f'{i+2} x {j} = {(i+2)*j:2d}', end = '    ')
            print(f'{i+3} x {j} = {(i+3)*j:2d}')