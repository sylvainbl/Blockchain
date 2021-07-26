

# this class contain the blockchain and the method necessary to make it work
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # create a new block and add it to the chain
    def new_block(self):
        pass

    # add a new transaction
    def new_transaction(self):
        pass

    # hash a block
    @staticmethod
    def hash(block):
        pass

    # return the last block in the blockchain
    @property
    def last_block(self):
        pass

    # create a new transaction that will be in the next mined block
    # params:
    # sender : name/address of the sender [str]
    # recipient : name/address of the recipient [str]
    # amount: nb of coins in the transaction [int]
    # return:
    # index in the chain of the new block that will contain the transaction [int]
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
