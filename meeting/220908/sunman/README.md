---
marp: true
---

# 코딩 인터뷰 완전 분석


## 🌻 6장 big-O

---

# 🌻 시간 복잡도

## 종류
1. big-O (빅오)
   - 시간의 상한 / 배열의 모든 값을 출력하는 알고리즘은 O(N)
2. big-Θ (빅쎄타)
   - 시간의 하한
3. big-Ω (빅오메가)
   - 정확한 시간 / 'O(x)'와 'Θ(x)'가 같은 경우 -> 'Ω(x)'

---

# 🌻 시간 복잡도 

## 퀵 정렬이란?
- '축'이 되는 원소 하나를 무작위로 뽑은 뒤
- 이보다 작은 원소들은 앞에 큰 원소들은 뒤에 놓이도록 위치를 바꿈
- 그 결과 부분 정렬이 완성되고
- 그 뒤 왼쪽과 오른쪽 부분을 재귀적으로 정렬

---

# 🌻 시간 복잡도

## 최선/최악/평균의 경우
- 최선의 경우
  - 모든 원소가 동일한 경우 / 단순히 배열을 한차례 순회하고 끝날 것
  - O(N) 🔥 그래도 확인은 해야돼서 O(N^2) 아닌가?
- 최악의 경우
  - 배역이 역순으로 정렬되어 있고 첫번째 원소를 항상 축으로 잡는다면
  - O(N^2)
- 평균적인 경우
  - O(NlogN)

---

# 🌻 공간 복잡도

## 개념
- 크기가 n인 배열을 만들고자 한다면 O(n)
- 크기가 n X n 인 2차원 배열을 만들고자 한다면 O(n^2)

---

# 🌻 공간 복잡도

## 예시
- 재귀 호출에서 사용하는 스택 공간도 공간 복잡도 계산에 포함
- 아래는 O(n)
- ```js
  const sum = (n) => {
    if (n <= 0){
      return 0
    }
    return n + sum(n-1)
  }
  ```

---

# 🌻 공간 복잡도

## 상수항 무시
- ❌ O(2N)
- ✅ O(N)

---

# 🌻 공간 복잡도

## 지배적이지 않은 항 무시
- ❌ O(N^2 + N)
- ✅ O(N^2)

---

# 🌻 공간 복잡도

## log N 수행 시간
- 이진 탐색을 상상해보자
- N개의 원소가 있을 때 우리가 다루는 리스트의 크기는
- N, N/2, N/2/2, N/2/2/2, ..., 1
- 위의 과정이 K번 이루어졌기 때문에 이를 식으로 쓰면,
- 2^K = N 됨
- 그래서 두 개씩 쪼개 가는 탐색 방법은 logN 번 수행됨

---

# 🌻 공간 복잡도

## O(logN) 과 O(K^N)의 차이
- log는 밑을 무시해도 되지만
- exponent에서는 밑을 무시하면 안된다
- 이유는 나중에 나온다.

---

# 🌻 쉬어가는 개발 용어 설명

## ArrayList (동적 가변크기 배열)
- 배열의 역할을 함과 동시에 크기가 자유롭게 조절되는 자료구조
- 원소 삽입 시 필요에 따라 크기가 두 배 더 큰 배열을 만든 뒤,
- 이전 배열의 모든 원소를 새 배열로 복사

---

# 🌻 예제 1

- 아래 코드의 시간 복잡도는?
```js
const foo = (numbers: number[]) => {
    const sum = 0
    const product = 1

    for (i = 0; i < numbers.length; i ++){
        sum += numbers[i]
    }
    for (i = 0; i < numbers.length; i ++){
        product *= numbers[i]
    }

    console.log(sum, ",", product)
}
```

---

# 🌻 정답

- O(N)

---

# 🌻 예제 2

- 아래 코드의 시간 복잡도는?
```js
const printPairs = (numbers: number[]) => {
    for (i = 0; i < numbers.length; i++){
        for (j = 0; j < numbers.length; j++){
            console.log(i, j)
        }
    }
}
```

---

# 🌻 정답

- O(N^2)

---

# 🌻 예제 3

- 아래 코드의 시간 복잡도는?
```js
const printPairs = (numbers: number[]) => {
    for (i = 0; i < numbers.length; i++){
        for (j = i + 1; j < numbers.length; j++){
            console.log(i, j)
        }
    }
}
```

---

# 🌻 정답

- O(N^2)

---


# 🌻 예제 4

- 아래 코드의 시간 복잡도는?
```js
const printPairs = (numbers1: number[], numbers2: number[]) => {
    for (i = 0; i < numbers1.length; i++){
        for (j = i + 1; j < numbers2.length; j++){
            console.log(i, j)
        }
    }
}
```

---

# 🌻 정답

- O(ab)

---


# 🌻 예제 5

- 아래 코드의 시간 복잡도는?
```js
const printPairs = (numbers1: number[], numbers2: number[]) => {
    for (i = 0; i < numbers1.length; i++){
        for (j = i + 1; j < numbers2.length; j++){
            for (k = 0; k < 10000; k++){
                console.log(i, j)
            }
        }
    }
}
```

---

# 🌻 정답

- O(ab)

---

# 🌻 예제 6

- 아래 코드의 시간 복잡도는?
```js
const reverse = (numbers: number[]) => {
    for (i = 0; i < numbers.length / 2; i++){
        other = number.length - i - 1
        temp = numbers[i]
        array[i] = array[other]
        array[other] = temp
    }
}
```

---

# 🌻 정답

- O(N)

---

# 🌻 예제 7

- 다음 중 O(N)과 같은 것은?
   - P < N/2 일 때, O(N+P)
   - O(2N)
   - O(N + logN)
   - O(N + M)

---

# 🌻 정답

- ✅ P < N/2 일 때, O(N+P)
- ✅ O(2N)
- ✅ O(N + logN)
- ❌ O(N + M) <= N과 M의 관계를 모름으로 그대로 써야함

---

# 🌻 예제 8 (이해 안돼서 Skip 😅)

- 아래 상황의 시간 복잡도를 구하라
   - 여러 개의 문자열로 구성된 배열이 주어졌을 때,
   - 각각의 문자열을 먼저 정렬하고
   - 그 다음에 전체 문자열을 사전순으로 다시 정렬하는 알고리즘

- 정답
  - O(N^2logN)이라고 오해하기 쉽지만,
  - O(a*s(loga+logs))가 맞다.

---

# 🌻 예제 9

- 균형 이진 탐색 트리의 아래 상황에서 시간 복잡도를 구하라
```js
const sum = (node) => {
    if (node == null){
        return 0;
    }
    return sum(node.left) + node.value + sum(node.right)
}
```

---

# 🌻 정답

- O(N)

---

# 🌻 예제 10

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const isPrime = (n: int) => {
    for(i = 2; i * i <= n; i++){
        if (n % i === 0){
            return false
        }
    }
    return true
}
```

---

# 🌻 정답

- O(N^0.5)

---

# 🌻 예제 11

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const factorial = (n: int) => {
    if (n < 0){
        return -1;
    } else if (n === 0){
        return 1;
    } else {
        return n * factorial(n-1)
    }
}
```

---

# 🌻 정답

- O(N)

---

# 🌻 예제 12 (이해 안돼서 Skip 😅)

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const permutation = (word: string, prefix: string) => {
    if(word.length === 0){
        console.log(prefix)
    } else {
        for(i = 0; i < word.length; i++){
            const rem = word.slice(0,i) + word.slice(i+1)
            permutation(rem, prefix + word[i])
        }
    }
}
```

---

# 🌻 정답

- O(N^2*N!)

---

# 🌻 예제 13

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const fib = (n: int) => {
    if(n <= 0) return 0;
    else if (n == 1) return 1;
    return fib(n-1) + fib(n-2);
}
```

---

# 🌻 정답

- O(2^N)
- 정확히는 O(1.6^N) (이해 안돼서 Skip 😅)

---

# 🌻 예제 14

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const allFib = (n: int) => {
    for (i = 0; i < n; i ++){
        console.log(i, ":", fib(i))
    }
}

const fib = (n: int) => {
    if(n <= 0) return 0;
    else if (n == 1) return 1;
    return fib(n-1) + fib(n-2);
}
```

---

# 🌻 정답

- O(2^N)

---

# 🌻 예제 15

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const allFib = (n: int) => {
    for (i = 0; i < n; i ++){
        console.log(i, ":", fib(i))
    }
}

const fib = (n: int, memo: int[]) => {
    if(n <= 0) return 0;
    else if (n == 1) return 1;
    else if (memo[n] > 0) return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n]
}
```

---

# 🌻 정답

- O(N)

---

# 🌻 예제 16

- 다음 함수의 시간 복잡도는 어떻게 되는가?
```js
const powersOf2 = (n: int) => {
    if (n < 1){
        return 0
    } else if (n == 1){
        return 1
    } else {
        const prev = powersOf2(n/2) // 여기서 n/2는 몫만 구한다는 뜻
        const curr = prev * 2
        return curr
    }
}
```

---

# 🌻 정답

- O(logN)