print('[구입]')
shopping_bag = {}

while True:
    item = input('상품명? ')
    if item == '' : break
    amount = int(input('수량은? '))
    shopping_bag[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')

print('\n>>> 장바구니 보기:', shopping_bag)