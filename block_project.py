#블록체인의 구조?
#최초의 블록부터 시작해서 바로 앞의 블록에 대한 링크를 가지고 있는 형태
#이러한 형태를 여러 노드들이 같은 정보, 장부를 갖는지 확인을 한다.


# 블록체인의 특징
# 1. 블록의 구조
# - Tracsaction
# - 전블록 hash
# - Time
# 2. 합의 과정
# - 분산화된 환경에서 자료 동기화

# 여기에는
# 블록 구조들
# Transaction 형태
# chain과 연결법들이 있을 것이다.

# 먼저 블록은 JSON 형태로 저장
# index : 몇 번째 블록인지
# Timestamp : 언제 블록이 생성되었는지
# Transaction : 거래 목록
# Proof : 마이닝의 결과
# Prev_hash : 블록의 무결성을 검증

import hashlib
import json
from time import time
from urllib.parse import urlparse
import requests

####### block generation & its principle

class Blockchain(object):
	# initialize the blockchain info
	def __init__(self):
		self.chain = []
		self.current_transaction = []
		self.nodes = set()
		# genesis block
		self.new_block(previous_hash=1, proof=100)

	def new_block(self,proof,previous_hash=None):
		block = {
			'index': len(self.chain)+1,
			'timestamp': time(), # timestamp from 1970
			'transactions': self.current_transaction,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1])
		}
		self.current_transaction = []
		self.chain.append(block)
		return block

	def new_transaction(self,sender,recipient,amount):
		self.current_transaction.append(
			{
				'sender' : sender,
				'recipient' : recipient,
				'amount' : amount				
				
			}
		)
		return self.last_block['index'] + 1

	def register_node(self, address):
		parsed_url = urlparse(address)
		self.nodes.add(parsed_url.netloc) # netloc attribute! network lockation
	
	def valid_chain(self,chain):
		last_block = chain[0]
		current_index = 1
		
		while current_index < len(chain):
			block = chain[current_index]
			print('%s' % last_block)
			print('%s' % block)
			print("\n---------\n")
			# check that the hash of the block is correct
			if block['previous_hash'] != self.hash(last_block):
				return False
			last_block = block
			current_index += 1
		return True

	def resolve_conflicts(self):
		neighbours = self.nodes
		new_chain = None

		max_length = len(self.chain) # Our chain length
		for node in neighbours:
			tmp_url = 'http://' + str(node) + '/chain'
			response = requests.get(tmp_url)
			if response.status_code == 200:
				length = response.json()['length']
				chain = response.json()['chain']

				if length > max_length and self.valid_chain(chain):
					max_length = length

			if new_chain:
				self.chain = new_chain
				return True

			return False

	# directly access from class, share! not individual instance use it
	@staticmethod
	def hash(block):
		block_string = json.dumps(block, sort_keys=True).encode()
	
		return hashlib.sha256(block_string).hexdigest()

	@property
	def last_block(self):
		return self.chain[-1]

	def pow(self, last_proof):
		proof = 0
		while self.valid_proof(last_proof, proof) is False:
			proof += 1

		return proof

	@staticmethod
	def valid_proof(last_proof, proof):
		guess = str(last_proof + proof).encode()
		guess_hash = hashlib.sha256(guess).hexdigest()
		return guess_hash[:4] == "0000" # nonce