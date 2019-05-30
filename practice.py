import datetime as dt
import hashlib

class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)

        sha.update(new_str_bin.encode())
        return sha.hexdigest()


def create_genesis_block():
    return Block(0,dt.datetime.now(),data="genesis block", previous_hash='0')

def next_block(last_block):
    return Block(index = last_block.index+1, timestamp=dt.datetime.now(), data="hey i am block"+last_block.index+1,previous_hash=last_block.hash)








blockchain = [create_genesis_block()]
previous_block = blockchain[-1]

num_of_block_to_add = 10

for i in range(num_of_block_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
