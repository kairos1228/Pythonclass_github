def rep_char(c, n):
    print(c*n)

def draw_line_string(msg1):
    msg1 = f'Hello {msg1},'
    msg2 = 'Welcome to Seoul.'

    if (len(msg1) > len(msg2)) :
        nstr = int(len(msg1))
    else: nstr = int(len(msg2))
    nstr = nstr + 2

    rep_char('-', nstr)
    print(f' {msg1}\n {msg2}')
    rep_char('-', nstr)

msg1 = input('Input his/her name: ')
draw_line_string(msg1)