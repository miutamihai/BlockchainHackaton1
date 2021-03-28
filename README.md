# BlockchainHackaton1

You should first install [Brownie](https://eth-brownie.readthedocs.io/en/stable/).

## Setup
1. Get your private key from metamask
2. Run `brownie accounts add`, with your private key and `deployment` as the name
3. Run `export WEB3_INFURA_PROJECT_ID=0342134c26fe4cd8b42d4ef719756ddf`
4. Cd to your cloned repository
5. Run `brownie compile`
6. Run `brownie deploy --network rinkeby`
7. Go to [etherscan](https://rinkeby.etherscan.io/verifyContract) to verify your contract (make sure to use the latest compiler version)
8. Run `brownie console --network rinkeby`
9. Run `instance = Contract.from_explorer('CONTRACT_DEPLOYMENT_ADDRESS')`

## Running
Available functions: 
* `instance.getBalance()` -> gets the balance of the contract
* `instance.getServiceOwner()` -> gets the owner of the contract
* `instance.fund({ 'from': 'YOUR_ADDRESS', 'value': VALUE_TO_FUND })` -> funds the contract with the inputted value
* `instance.withdraw(VALUE_TO_WITHDRAW, { 'from': 'YOUR_ADDRESS' })` -> withdraws desired amount from the contract balance

## Events
The contract has the following events associated with it:
* `Funded` -> triggered when the `fund` function is called
* `Withdrawn` -> triggered when the `withdraw` function is called
