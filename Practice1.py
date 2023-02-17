# Вводится строка с номером телефона. Ожидается формат ввода: +7(xxx)xxx-xx-xx где userInp - это цифра.
# Размер введенных символов считается верным (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя). Необходимо проверить, что введенная строка соответствует этому формату. Вывести ДА, если соответствует и НЕТ - в противном случае.
# Sample Input: +7(123)456-78-99
# Sample Output: ДА

userInp = list(input())
form = '+7(xxx)xxx-xx-xx'
res = ''

if len(userInp) == len(form):
    for i, v in enumerate(userInp):
        if form[i] != 'userInp' and form[i] != v:
            break
        elif form[i] == 'userInp':
            res += v
    if res.isdigit() and len(res) == 10:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('НЕТ')
