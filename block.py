import datetime as dt
import hashlib

class Block(object):
    """
    index, 블록 생성시간, 데이터, 이전 hash value 등을 이용해 새로운 hash를 가지는 블록을 생성
    """
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        sha = hashlib.sha256()
        new_str_bin = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        # 이전 block의 hash를 가져와서 다시 hash를 만든다.
        # 즉, 새롭게 hash 값을 만들 때 이전 블록의 hash 값을 참조해서 만들기 때문에 이를 활용해 무결성이 확보된다.
        sha.update(new_str_bin.encode())
        
        return sha.hexdigest()
        
    # 링크드 리스트 처럼 시작이 되는 헤드노드가 필요한데
    # 블록체인에서도 마찬가지로 창세기 블록, genesis_block을 만들어 줘야 한다.
    # 그 다음으로 새롭게 block을 만들어 주는 함수를 선언하고, 해당 함수는 기존의 블록체인에서 마지막 노드에 자동으로 이어 붙인다.
    # 자동으로 이어 붙이는 말은, 기존 블록체인의 마지막 노드의 hash 값을 참고해서 본인의 hash 값을 만든다는 것이다.
    
def create_genesis_block():
    return Block(0,dt.datetime.now(),data="genesis block", previous_hash="0")

def next_block(last_block):
    ## 지난번에 생성된 last_block에 이어붙일 새로운 블록을 만들어서 리턴
    return Block(index = last_block.index+1, timestamp = dt.datetime.now(), data = "Hey, I am block {}".format(last_block.index+1),previous_hash = last_block.hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[-1]

num_of_block_to_add = 10
for i in range(num_of_block_to_add):
    ## 이전 블록에 이어(이전 hash 값을 이용해 새로운 hash 값을 생성) 새로운 블록을 생성
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = blockchain[-1]
    print("Block {} has been added to blockchain".format(previous_block.index))
    print("hash value: {}".format(previous_block.hash))