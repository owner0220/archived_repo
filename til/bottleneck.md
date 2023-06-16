disk I/O가 overflow 될때
bottlenect 현상이 발생


CPU가 프로세스 계산을 해야 하는데 diskI/O에서 처리가 안되니까 실제 계산을 안되고 wait가 발생하는 현상이 생길 수 있다.
