from brownie import accounts, ERC20CRV, VotingEscrow

def test_deploy():
    account = accounts[0]
    token_name = 'Ocean token'
    token_symbol = 'OCEAN'
    token_decimals = 18
    version = '1.2'

    erc20 = ERC20CRV.deploy(token_name, token_symbol, token_decimals, {'from': account})

    voting_escrow = VotingEscrow.deploy(
        erc20, token_name, token_symbol, version, {'from': account})

    assert voting_escrow.name() == token_name
    assert voting_escrow.symbol() == token_symbol
    assert voting_escrow.version() == version
