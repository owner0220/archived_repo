> python ver_3.7.2

# Sequence Types 

### 시퀀스 유형 - range

- 사용법 :

  **range** ( stop )

  **range** ( start, stop )

  **range** ( start, stop, step )

- 기능 : 

  - 숫자 리스트를 만들어 준다.

  - 따로 설정이 없다면 start = 0, step = 1로 기본 세팅이 되어 있다.

  - **range 인자로 들어가는 stop 숫자 보다 -1 한 값들만 나온다는 것을 기억하자!**

  - 내부 로직 :

    ```c
    //step > 0 일때
    for (int i = 0; i>=0 and r[i] < stop; i++){
        r[i] = start + step*i;
    }
    
    //setp < 0 일때
    for (int i = 0; i>=0 and r[i] > stop; i++){
        r[i] = start + step*i;
    }
    ```

    

- 리턴값 :

  **range** 클래스

