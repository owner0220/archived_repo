# 빅오 표기법(Big-O notation)

###  시간복잡도, 공간복잡도

> [Big-O notation] (<https://en.wikipedia.org/wiki/Big_O_notation>)

## Big-O 표기란?

> Big-O notation is a way of converting the overall steps of an algorithm into algebraic terms, then excluding lower order constants and coefficients that don’t have that big an impact on the overall complexity of the problem.

- 개발자들에게는 위의 사전식 정의보다는 아래의 정의가 더 와닿을 겁니다.

  `Regular       Big-O``2             O(1)   --> It's just a constant number``2n + 10       O(n)   --> n has the largest effect``5n^2          O(n^2) --> n^2 has the largest effect`

- 이 예제가 의미하는 것은 다음과 같습니다.

   

  시간복잡도에서 중요한 것은 정해진 표현식에 가장 큰 영향을 미치는 n 의 단위이다

- 대표적인 시간 복잡도들을 간단하게 정의해봅니다.

  1. **O(1) – 상수 시간** : 입력값 n 이 주어졌을 때, 알고리즘이 문제를 해결하는데 오직 한 단계만 거칩니다.
  2. **O(log n) – 로그 시간** : 입력값 n 이 주어졌을 때, 문제를 해결하는데 필요한 단계들이 연산마다 특정 요인에 의해 줄어듭니다.
  3. **O(n) – 직선적 시간** : 문제를 해결하기 위한 단계의 수와 입력값 n이 1:1 관계를 가집니다.
  4. **O(n^2) – 2차 시간** : 문제를 해결하기 위한 단계의 수는 입력값 n의 제곱입니다.
  5. **O(C^n) – 지수 시간** : 문제를 해결하기 위한 단계의 수는 주어진 상수값 C 의 n 제곱입니다.

- 위 정의를 가지고 아래 예제의 시간복잡도를 계산해보겠습니다.

  `var n = 16; -- 입력값 n 이 16일 때``O (1) = 1 step "(awesome!)" -- O(1)는 시간복잡도가 1입니다.``O (log n) = 4 steps  "(awesome!)" -- O(log n)는 시간복잡도가 4입니다. (log 의 밑이 2라고 가정)``O (n) = 16 steps "(pretty good!)" -- O(n)는 시간복잡도가 16``O(n^2) = 256 steps "(uhh..we can work with this?)" -- O(n^2)는 시간복잡도가 256``O(2^n) = 65,536 steps "(...)"`

- 위와 같은 시간복잡도 계산을 코드에 적용해봅니다.

  `// 아래와 같은 데이터 구조 기준으로 시간복잡도를 적용해봅니다.``var` `friends = {``'Mark'` `: ``true``,``'Amy'` `: ``true``,``'Carl'` `: ``false``,``'Ray'` `:  ``true``,``'Laura'` `: ``false``,``}``var` `sortedAges = [22, 24, 27, 29, 31]`

#### O(1) — CONSTANT TIME (상수 시간)

- 값을 검색할 때, 객체에서 키를 알거나 배열에서 인덱스를 알고 있으면 언제나 한 단계만 걸립니다.

  `//If I know the persons name, I only have to take one step to check:``function` `isFriend(name){ ``//similar to knowing the index in an Array``return` `friends[name];``};``isFriend(``'Mark'``) ``// returns True and only took one step``function` `add(num1,num2){ ``// I have two numbers, takes one step to return the value``return` `num1 + num2``}`

#### O(LOG N) — LOGARITHMIC TIME (로그 시간)

- 배열에서 값을 찾을 때, 어느 쪽에서 시작할지를 알고 있으면 검색하는 시간이 두배로 줄어듭니다.

  `//You decrease the amount of work you have to do with each step``function` `thisOld(num, array){``var` `midPoint = Math.floor( array.length /2 );``if``( array[midPoint] === num) ``return` `true``;``if``( array[midPoint]  only look at second half of the array``if``( array[midpoint] > num ) --> only look at first half of the array``//recursively repeat until you arrive at your solution` `}``thisOld(29, sortedAges) ``// returns true``//Notes``//There are a bunch of other checks that should go into this example for it to be truly functional, but not necessary for this explanation.``//This solution works because our Array is sorted``//Recursive solutions are often logarithmic``//We'll get into recursion in another post!`

#### O(2^N) — EXPONENTIAL TIME (지수 시간)

- 지수 시간은 보통 문제를 풀기 위해 모든 조합과 방법을 시도할 때 사용됩니다.

  `//The number of steps it takes to accomplish a task is a constant to the n power``//Thought example``//Trying to find every combination of varters for a password of length n`

## 마무리

> it’s hard to say there is a single “right” or “best” answer to these problems. But it is possible to say there are “better” or “worse” answers to a given problem.

- 문제를 해결하려고 할 때마다 시간복잡도를 분석하는 습관을 들이면 좋은 개발자가 될 수 있습니다.
- 엔지니어에게 있어서, **문제라는 것은 정답이나 최선의 답의 관점에서 접근하는 것보다, 상황에 더 맞는 답인지 아닌지의 관점에서 접근해야 합니다.**
- 마지막으로 한번 더 요약합니다.
  1. **O(1) – 상수 시간** : 알고리즘이 문제를 해결하는데 오직 한 단계만 거칩니다.
  2. **O(log n) – 로그 시간** : 문제를 해결하는데 필요한 단계들이 연산마다 특정 요인에 의해 줄어듭니다.
  3. **O(n) – 직선적 시간** : 문제를 해결하기 위한 단계의 수와 입력값 n이 1:1 관계를 가집니다.
  4. **O(n^2) – 2차 시간** : 문제를 해결하기 위한 단계의 수는 입력값 n의 제곱입니다.
  5. **O(C^n) – 지수 시간** : 문제를 해결하기 위한 단계의 수는 주어진 상수값 C 의 n 제곱입니다. (상당히 큰수가 됩니다)