from web3 import Web3, HTTPProvider

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_URL"  # Replace with your Infura URL

def get_erc20_token_balance(token_contract_address, wallet_address):
    """
    Connects to the Ethereum blockchain using an Infura HTTP endpoint and retrieves the ERC-20 token balance
    for a user's wallet.
    
    Parameters:
    token_contract_address (str): The address of the ERC-20 token contract.
    wallet_address (str): The address of the user's wallet.
    """

    # Connect to Ethereum using the Infura URL
    web3 = Web3(HTTPProvider(infura_url))

    # Ensure connection is established
    if not web3.is_connected():
        print("Failed to connect to Ethereum")
        return None

    # ERC-20 token contract ABI necessary for the balanceOf, decimals and symbols functions
    with open('data/erc20abi.json') as abi_file:
        erc20_abi = abi_file.read()

    # Create contract instance
    contract = web3.eth.contract(address=token_contract_address, abi=erc20_abi)

    # Wrap in try/except to catch any errors as sometimes API calls do fail/timeout
    # Get token balance, divide it by the decimals for the token balance
    # Get the token symbol E.g. USDT for the token that people recognize instead of the contract address
    try:
        raw_bal = contract.functions.balanceOf(wallet_address).call()
        decimal = contract.functions.decimals().call()
        balance = raw_bal / (10 ** decimal)
        tsymbol = contract.functions.symbol().call()
        print(f"Token ${tsymbol} Balance for {wallet_address}: {balance}")
    except Exception as e:
        print(f"Error getting token balance: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace with the actual token contract address (Currently USDT) and wallet address (Currently random wallet)
    # We use to_checksum_address and turn the address to lowercase 
    token_contract_address  = Web3.to_checksum_address("0xdAC17F958D2ee523a2206206994597C13D831ec7".lower())
    wallet_address          = Web3.to_checksum_address("0xbd32d105f2fa9a8ce9c4e5c3ab6ff59ec1ed0d2f".lower())
    get_erc20_token_balance(token_contract_address, wallet_address)
