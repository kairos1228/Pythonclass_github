
def buy(lst):
    print('[구입]')
    item = input('상품명? ')
    if item == '' : return False
    amount = int(input('수량은? '))
    lst[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.\n')

def show(lst):
    print('\n>>> 장바구니 보기:', lst)

def find(lst):
    print('\n[검색]')
    product = input('장바구니에서 확인하고자 하는 상품은? ')
    if product in lst :
        print(f'{product}은(는) {lst[product]}개 담겨 있습니다.')
    else :
        print(f'장바구니에 {product}은(는) 없습니다.')


#주 프로그램 부
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)