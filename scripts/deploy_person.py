from brownie import Person, accounts

def main():
    acct = accounts.load('deployment')
    Person.deploy(21, {'from': acct, 'uri': 'https://rinkeby.infura.io/v3/undefined'})