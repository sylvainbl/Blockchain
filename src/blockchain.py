import hashlib
import json
from time import time

# this class contain the blockchain and the method necessary to make it work


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    # Create the first block of the blockchain
    self.new_block(previous_hash=1, proof=100)

    # create a new block and add it to the chain
    def new_block(self):
        pass

    # add a new transaction
    def new_transaction(self):
        pass

    # create a SHA-256 hash of a block
    # params:
    # a block like created by new_block [dict]
    # return:
    # the hash [str]

    @staticmethod
    def hash(block):
        # this instruction permit to order the dict in case it isn't ordered
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # return the last block in the blockchain

    @property
    def last_block(self):
        return self.chain[-1]

    # create a new transaction that will be in the next mined block
    # params:
    # sender: name/address of the sender [str]
    # recipient: name/address of the recipient [str]
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

    # Create a new block in the blockchain
    # params:
    # proof: the proof given by the proof of work algorithm [int]
    # previous_hash: the hash of the previous block (if there was one) [str]
    # return: new block [dict]

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
