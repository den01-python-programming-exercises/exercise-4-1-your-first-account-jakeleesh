def main():
    #write your code below this line
    jakes_account = Account("Jake's account", 100)
    jakes_account.deposit(20)
    print(jakes_account.balance_end())

# Don't edit below this line - this setup is required for testing
if __name__ == '__main__':
    from account import Account
    main()
else:
    from src.account import Account
