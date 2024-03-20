def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    circle_width = (3.14 * radius ** 2)
    return circle_width

radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
circle_width = get_circle_area(radius)
print('반지름 {}인 원의 넓이 = 3.14 x {} x {} = {}' .format(radius, radius, radius, circle_width))
