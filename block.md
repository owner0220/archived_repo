# Class Block
- block은 하나의 정보단위를 말한다.
- 보통 DB에서는 하나 하나 transaction이라고 생각해 거의 real-time으로 적용되지만
블록체인은 데이터들이 쌓이고 그 데이터들이 한번에 블록으로 만들어 진다.

### 구현
1. index, timestamp, data, previous_hash를 모두 합쳐 string으로 만들고 이 스트링을 bytes로 encoding해서 hash 값을 찾는다.
2. 1에서 만들어진 hash 값이 해당 블록의 hash 값이 된다.(주소)
    - 여기서 정의된 data가 해당 블록의 핵심 정보가 된다.(serialization만 되면 된다.)
    ※ Serialization이란 개체를 저장하거나 메모리, 데이터베이스 또는 파일로 전송하기 위해 개체를 바이트 스트림으로 변환하는 프로세스
3. 블록들은 경우에 따라 달라질 수 있지만, 기본적으로 생성번호, 생성인덱스, 데이터, 이전 해쉬값 네가지를 이용해 hash 값을 찾아주는 클래스를 구현하면 된다.

```
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
        
```

4. 
- 링크드 리스트 처럼 시작이 되는 헤드노드가 필요한데
- 블록체인에서도 마찬가지로 창세기 블록, genesis_block을 만들어 줘야 한다.
- 그 다음으로 새롭게 block을 만들어 주는 함수를 선언하고, 해당 함수는 기존의 블록체인에서 마지막 노드에 자동으로 이어 붙인다.
- 자동으로 이어 붙이는 말은, 기존 블록체인의 마지막 노드의 hash 값을 참고해서 본인의 hash 값을 만든다는 것이다.


```
def create_genesis_block():
    return Block(0,dt.datetime.now(),data="genesis block", previous_hash="0")

def next_block(last_block):
    ## 지난번에 생성된 last_block에 이어붙일 새로운 블록을 만들어서 리턴
    return Block(index = last_block.index+1, timestamp = dt.datetime.now(), data = "Hey, I am block {}".format(last_block.index+1),previous_hash = last_block.hash)
```

---
5. 데이터를 list of transaction 으로 고려해서 업그레이드해보자
