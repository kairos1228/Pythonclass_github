
def get_fixed_price(price):
    fixed_price = price*(1/(1-discount_rate*0.01))
    return fixed_price

discount_rate = int(input("할인율은? "))
a_discounted_price = int(input("A 상품의 할인된 가격은? "))
b_discounted_price = int(input("B 상품의 할인된 가격은? "))

a_fixed_price = get_fixed_price(a_discounted_price)
b_fixed_price = get_fixed_price(b_discounted_price)

print('A 상품의 정가는 {} 원' .format(a_fixed_price))
print('B 상품의 정가는 {} 원' .format(b_fixed_price))