from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_URL"

def get_latest_block():
    """
    Connects to the Ethereum blockchain using an Infura HTTP endpoint and retrieves the latest block number.
    We have a couple of checks and try/catch blocks as connections to blockchain nodes can fail from time to time.
    """

    # Connect to Ethereum using the Infura URL
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Ensure connection is established
    if not web3.is_connected():
        print("Failed to connect to Ethereum")
        return None

    # Get the latest block number
    # Wrap in try/except to catch any errors as sometimes API calls do fail/timeout
    try:
        latest_block = web3.eth.block_number
        print(f"The latest block on the Ethereum blockchain is: {latest_block}")
        return
    except Exception as e:
        print(f"Error getting the latest block number: {e}")
        return None
    
    
if __name__ == "__main__":
    get_latest_block()
