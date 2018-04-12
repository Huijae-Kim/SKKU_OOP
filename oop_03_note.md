# 3주차 강의 내용 (완)
&copy; document created by heejae6021@naver.com

## 변수
Variable : 
변수; 램의 일정 부분 공간의 이름; 데이터가 저장되어있는 공간

## 데이터형태
### 숫자
- 숫자 역시 문자열 형태라고 볼 수 있다.
- 정수형, 실수형, 복소수형, decimal(부동소수점의 부정확성을 완벽하게 보완한 형태)
- 복소수를 기본 포맷으로 가지고 있음 > Python만의 특징
- 실수형이 정수형보다 더 큰 data type; 그래서 정수형을 사용했을 때 더 속도가 빠르다.
- 정수형(Integer) : 1 , 2 , 3
- 부동(떠다닌다) 소수점 숫자형(Float) : 소수점이 왔다갔다 할 수 있는 것(=유동소수점); 1.0 , 2.3
- . 들어가면 무조건 실수!
- 복소수형 : i를 j로 쓴다; 2+3j
- 암묵적 캐스팅
```python
a = 3.1 # float
b = 2 # integer
c = a+b  # 5.1(float)
```
> Python은 작은 data type을 큰 data type으로 변환한 후 연산.
- 명시적 캐스팅
```python
a = 3.1
b = 2
c = int(a)+b # 5(integer)
d = a - int(a) # 소수부분, 캐스팅의 또다른 기능
```
> 기본적으로 프로그래밍은 data type이 같아야지만 연산이 가능했다.
### 문자열(string)
- “ ” 안에 들어가면 문자열
```python
a = “ab” # string
b = “12” # string
c = a+b # “ab12”(string)
d = a*3 # “ababab”(string)
```  
- 문자+숫자는 불가능!
```python
a = “ab”
b = 12
c = a+b # error
d = a+str(b) # “ab12”(string)
```
- 문자열의 길이
```python
a = “ab”
len(a) # 2
```
- 순서(index)는 1부터가 아닌! 0부터 시작이다
```python
a = “ab”
a[0] # “a”
b = “skku”
b[1] # “k”
b[3] # “u”
b[len(b)-1] # “u”
b[-1] # “u”
b[-4] # “s”
``` 
- 숫자는 index 불가능! 문자열로 변환 후 사용 가능!
```python
b = 12
b[0] # error
len(str(b)) # 2
```
- Slicing
```python
# a[start:stop:step]
f = “hello, world”
f[0:5] # “hello”, 0부터 5번째(즉, index 4)까지 가져와라.
f[:5] # “hello”, 앞에 0 생략 가능
f[-3:] # “rld”, 뒤에서 3번째부터 끝까지 가져와라.
f[:] # “hello, world”, f와 동일, but 깊은 copy 
f[::-1] # “dlrow ,olleh”, 반대로
```
- .find()
```python
f = “hello, world”
f.find(“,”) # 5, f라는 문자열에서 ‘,’를 찾아서 첫 index를 알려줘
f.rfind(“,”) # 5, 오른쪽에서부터 찾아줘
```
> 문자열에서만 가능하다.
- .split() 
```python
f = “hello, world”
f.split(“,”) # [‘hello’, ‘ world’], 여기서 ‘,’를 구분자라고 한다.
```
> 구분자를 기준으로 나눠준다.
- .strip() / .rstrip() / .lstrip() 
```python
g = “ My name is heejae kim.”
g.strip() # “My name is heejae kim.”
```
> 의미없는 공백을 잘라내준다(trim). 즉 앞뒤 공백을 지워준다. 
- null : 공간은 있는데, 공간은 할당되어있는데 어떠한 값도 들어가 있지 않은 것. = None
- escape characters
```markdown
\ # 뒤에 오는 것 특이한 거야! 라고 알려주는 signal
\n # 줄바꿈, 길이 1이다
\b # backspace
\” # 특수하게 해석하지마
\\ # 다음에 오는 backslash를 escape character로 해석하지마. 특이한 거 아냐.
```
- 따옴표 3개, 3개 ‘’’ ‘’’
```python
‘’’
따옴표 안에 manual을 이처럼 길게 작성할 수 있다.
줄바꿈을 해도 문제가 없다.
’’’
```
> 문단을 주석처리 할 수 있다.
- .format()
```python
name = heejae
age = 26
print ‘{0} is {1} years old’.format(name, age) # ‘heejae is 26 years old’, (0,1)은 index를 의미
```
- 문자의 길이는 최대 79자..!!
