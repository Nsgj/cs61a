def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw2(balance,password):
    def withdraw(amount,putin):
        nonlocal balance
        nonlocal password
        if len(save) >= 3:
            return "Your account is locked. Attempts: " + str(save)
        
        if putin == password:
            if amount > balance:
                return "Insufficient funds"
            balance = balance - amount
            return balance
        else:
            save.append(putin)
            return 'Incorrect password'
    save = []
    return withdraw