# This is for studing APIs and practical usecase of data structure
## APIs?
* API stands for Application Programming Interface which helps communicating other products and services.
![apis](https://user-images.githubusercontent.com/65937735/132780065-80a39fd9-90b1-46cb-b057-228b0895fbd7.png)

It's like calling a function from different application. Once one of the parties sends request to retrieve a data then other one returns response.
## Related data structure
- [x] Linked list
- [ ] Hash table
- [ ] Binary search
- [ ] Stack
- [ ] Queue

### Array
연속하는 공간에 같은 속성의 요소들을 저장. array를 만들기 전에 크기를 할당해줘야 한다.
#### 크기가 n인 array가 있다고 할 때
* Accessing time: O(1) 요소들이 연속적인 공간에 저장되어 있어서 가능하다는데 솔직히 무슨 말인지 모르겠다.
* Search time: 선형 - O(n), 이진 - O(log n)
* Insertion time: O(n). array의 시작부분에 요소를 넣어야 하는 경우 나머지 요소들을 뒤로 한 칸씩 밀어야 한다.
* Deletion time: O(n). array의 시작부분의 요소를 지워야 하는 경우 나머지 요소들을 뒤로 한 칸씩 당겨야 한다.
#### Practical usage
추가적인 변수를 만들 필요가 없고 단순히 array를 조회하는 것만드으로 요소에 접근해야 할 때.

### Linked list
서로 나눠진 공간에 요소를 선형적으로 저장한다. 요소들을 node라고 부르고 각 node는 일반적으로 item을 저장하고 다음 node를 가리키는 2가지 속성을 가진다. 크게 3가지 Linked list가 있다.
1. SIngly Linked List
To be updated
2. Doubly Linked List
To be updated
3. Circular LInked List
To be updated
#### 크기가 n인 Linked list가 있다고 할 때
* Accessing time: O(n)
* Search time: O(n)
* Insertion time: O(1). 삽입할 요소의 위치를 알 때
* Deletion time: O(1). 지울 요소의 전 요소의 인덱스를 알 때

https://www.geeksforgeeks.org/overview-of-data-structures-set-1-linear-data-structures/
