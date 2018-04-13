# 6주차 강의 내용 (완)
&copy; document created by heejae6021@naver.com

## Bubble Sort

- 오름차순 정리
- 4 3 2 1 7
- 이중 loop 돌린다.
- [try1] 0-1, 1-2, 2-3, 3-4 비교하면서 swap > 4번째 index에 가장 큰 수가 가게 된다.
- [try2] 0-1, 1-2, 2-3 비교하면서 swap
- [try3] 0-1, 1-2 비교하면서 swap
- [try4] 0-1 비교하면서 swap
- 총 length-1의 loop를 돌면 된다.
```python
def bubble_sort(data):
  mydata = data[:]
  for i in range(len(mydata)-1):
    for j in range(len(mydata)-i-1):
      if mydata[j] > mydata[j+1]:
        mydata[j],mydata[j+1]=mydata[j+1],mydata[j]
  return mydata
```
```python
def bubble_sort(data):
  mydata = [:]
  for i in range(len(data)-1):
    for j in range(i+1, len(data)):
      if data[i]>data[j]:
        data[i],data[j]=data[j],data[i]
  return data
```

## Quick Sort

- 대부분 프로그램 언어들의 내장 정렬 함수는 이 방법을 사용해서 만들어졌다.
- bubble sort보다 빠르다.
- 임의의 pivot을 정한다. 알고리즘 상에서는 가운데, 프로그램 상에서는 첫번째를 pivot으로 잡는다.
- 오름차순 정렬
![Image of Quick Sort](https://github.com/heejae6021/OOP/blob/master/images/quicksort.jpg =400x405)
- quick sort 함수를 만들기 위해서는 재귀함수를 배워야 한다. 다음 시간에~
