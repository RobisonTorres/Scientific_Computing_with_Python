print('Scientific Computing with Python - FreeCodeCamp')
print('Project: Arithmetic Arranger')

def arithmetic_arranger(problems, show=False):

    # Given a math problem horizontally, this function arranges it vertically and gives the result if asked.
    x = 0
    fl = ''
    sl = ''
    tl = ''
    lr = ''

    if len(problems) > 5:
        # First rule.
        return 'Error: Too many problems.'

    while len(problems) > x:

        each = problems[x].split()
        f_number = each[0]
        s_number = each[2]
        operator = each[1]

        if len(f_number) < 5 and len(s_number) < 5:
            if f_number.isnumeric() and s_number.isnumeric():
                if operator == '+':
                    result = str(int(f_number) + int(s_number))
                elif operator == '-':
                    result = str(int(f_number) - int(s_number))
                # Second rule.
                else:
                    return "Error: Operator must be '+' or '-'."
            else:
                # Third rule.
                return "Error: Numbers must only contain digits."
        else:
            # Fourth rule.
            return 'Error: Numbers cannot be more than four digits.'

        # Space between equations arrangement.
        space = max(len(f_number), len(s_number)) + 2

        fl += ' ' * (space - len(f_number)) + f_number + ' ' * 4
        sl += operator + ' ' * (space - len(s_number) - 1) + s_number + ' ' * 4
        tl += space * '-' + ' ' * 4
        lr += ' ' * (space - len(result)) + result + ' ' * 4
        x += 1

    # It shows the result if the second argument equals to true.
    if show:
        arranged_problems = fl.rstrip() + '\n' + sl.rstrip() + '\n' + tl.rstrip() \
                            + '\n' + lr.rstrip()
    else:
        arranged_problems = fl.rstrip() + '\n' + sl.rstrip() + '\n' + tl.rstrip()

    return arranged_problems
