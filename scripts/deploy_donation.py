from brownie import Donation, accounts

def main():
    acct = accounts.load('deployment')
    Donation.deploy({'from': acct, 'uri': 'https://rinkeby.infura.io/v3/undefined'})