print('Scientific Computing with Python - FreeCodeCamp')
print('Project: Budget App')

class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.total_withdraw = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        txt = {'amount': amount, 'description': description}
        self.ledger.append(txt)

    def check_funds(self, amount):
        return self.balance >= amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.total_withdraw += amount
            txt = {'amount': amount * -1, 'description': description}
            self.ledger.append(txt)
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            txt = {'amount': amount * -1, 'description': f'Transfer to {category.category}'}
            self.ledger.append(txt)
            category.balance += amount
            txt = {'amount': amount, 'description': f'Transfer from {self.category}'}
            category.ledger.append(txt)
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        txt = self.category.center(30, '*')
        budget_list = []
        n = len(self.ledger)
        x = 0
        while n > x:
            new_list = [item for item in self.ledger[x].values()][::-1]
            space = (30 - len(str(new_list[0])[0:23]) - len(f'{new_list[1]:.2f}'[:7])) * ' '
            budget_list.append(new_list[0][0:23] + space + f'{new_list[1]:.2f}'[:7])
            x += 1
        return txt + '\n' + '\n'.join(budget_list) + '\n' + f'Total: {self.balance:.2f}'


def create_spend_chart(arr):

    # This function creates a chart based on the total withdraw of each category.
    percentage = []
    chart_body = []
    chart_bottom = []

    # Total amount of all withdraw.
    total = sum([value.total_withdraw for value in arr])

    # Percentage of each category.
    for i in range(0, len(arr)):
        percentage.append([abs(round(((value.total_withdraw / total) * 100), 0))
                           for value in arr][i])

    # Chart Body.
    for n in range(100, -10, -10):
        x = 0
        line = f"{str(n) + '|':>4}"
        while len(arr) > x:
            if percentage[x] < n:
                line += '   '
            else:
                line += ' o '
            x += 1
        chart_body.append(line + ' ')
        x -= x

    array = [str(name.category) for name in arr]
    new_length = [word + ((len(max(array, key=len)) - len(word)) * ' ')
                  if word != str(max(array, key=len)) else word for word in array]

    # Chart Bottom.
    for n in range(0, len(max(array, key=len))):
        x = 0
        line = '     '
        while len(arr) > x:
            line += new_length[x][n] + '  '
            x += 1
        chart_bottom.append(line)
        x -= x

    return 'Percentage spent by category' + '\n' + '\n'.join(chart_body) \
           + '\n' + 4 * ' ' + (len(arr) * 3 + 1) * '-' + '\n' + '\n'.join(chart_bottom)
