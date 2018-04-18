# 7주차 강의 내용 (완)

&copy; document created by heejae6021@naver.com

## Error 관련

### `try:`, `except:`

- 통제가 불가능한 에러가 발생할 위험이 있을 때 try, except 구문을 써야한다.

- 속도가 느려질 가능성이 있으니 꼭 필요한 경우에 써야 한다.

- (예) 파일을 불러올 때, 통신을 이용해 메시지를 보낼 때 등등의 상황에... 만약에 그런 상황이 발생한다면 ~~해라.

```python
try:
  data.append(int(el))
except:
  print "data is not number"

# 각각 exception 상황을 나눠서 해줄 수 있다.
except IOException:
  print "IOException Error"
except ValueException:
  print "ValueException Error"
```

### `raise Exception`
- 일부러 Exception을 불러일으키는 것.
```python
if len(a) is not len(b):
  raise Exception # if len(a) is not len(b) Exception 발생.
```

## `input( )`

```python
# 2.7 ver
raw_input() # 무조건 string
input() # python이 int인지, str인지 등등 판단해서 캐스팅한다.

#3.0 ver
input() # 2.7 ver의 raw_input()과 동일
```

## IO, Input file
### open / close the file
- 같은 directiory에 있으면 그냥 파일명만 쓰면 된다. (상대경로)
- 파일 open 모드
	1. read : 읽기만 가능
	2. write : 쓰기 가능(새파일을 만들어서 쓴다)
	3. append : 기존 파일에 추가/수정이 가능

```python
# open the file
fp = open("data.csv") # file pointer(flie location)
fp = open("data.csv", "r")
fp = open("data.csv", "w")
fp = open("data.csv", "a")
```
- 파일에서 읽어오는 형태는 늘 string 형태로 저장된다.
- csv file 마지막에도 늘 enter로 줄바꿈 되어있는 것을 권장.
- `close( )` 명시적으로 써주는 것이 좋다.
```python
# close the opened file
fp.close()
```
### readline(s)
- 불러온 파일을 읽어오는 method이다.
- `readline( )`을 할 때마다 커서가 다음 줄로 움직인다고 생각하면 편하다.
```python
line1 = fp.readline() # 첫번째 줄 읽고 다음 줄 앞에 커서가 옮겨 간 상태
line2 = fp.readline() # 두번째 줄 읽고 다음 줄 앞에 커서가 옮겨 간 상태

# 만약 모든 줄을 다 읽어버리고 싶으면
lines = fp.readlines() # 단 커서는 파일 가장 앞에 있어야 한다.
print type(lines) # check data type
```

## OOP

- Object Oriented Programming
- Object : thing, 객체 (무형, 유형 모두 포함)
- Class : object를 설명하는 blue print(설계도), 포괄적인 개념
- Class에 의해서 만들어진 피조물이 바로 Object가 된다.
- Class를 현실화하면 객체(Instance)가 된다.
- 우리는 앞으로 class를 선언해서 그걸로 개체를 만들어서 프로그램을 짤 것이다.

### object와 instance의 차이
- object는 객체, instance는 class에 의해 만들어진 객체.
- 즉 instance는 class와의 관계 설명할 때 쓰인다.
```python
class Minion:
  pass
bob = Minion()
# bob은 object이다.
# bob은 Minion이라는 class에 instance이다.
```

### class
- attribute[속성] : 명사; object가 가지고 있는 특징
- method: 동사; 할 수 있는 일, function과 비슷
- (예) '차'라는 class : attribute(색상, 승차인원, 마력), method(굴러간다, 문이 열린다)

### class의 특징

1. 캡슐화, 은닉화 
	- 차에 관련된 모든 속성은 다 드러나야 한다. 그리고 외부에서 쉽게 바꿀 수 없어야 한다. 
	- 혹시 attribute를 알아내거나 지정하고자 할 때 set-get method(SetColor( ), GetColor( ))라는 것을 이용한다. 
	- attribute를 set-get method를 통하지 않고서는 알 수 없다.
	- 하지만! 파이썬은 약화된 객체지향을 지향하기 때문에 set-get method를 통하지 않고서도 attribute에 접근할 수 있다.

3. 상속
	- class 간의 부모/자식 관계가 성립한다.
	- child는 parent의 attribute, method를 모두 갖는다.
	- parent는 하나만 갖는 것을 지향한다. 동시/다중상속도 가능하긴 하지만 attribute나 method가 겹칠 수 있기 때문에 지양한다.

4. 다형성
	- 다양한 형태를 인정한다.
	- method 오버라이드 
		- parent가 가지고 있는 method를 다시 정의해서 사용하는 것. "재정의"
		- car라는 parent class에 color라는 속성, run( )이라는 method가 있다.
		- child class에 동일하기 run( )이라는 method가 있는데 조금 다르다.
		- 이러한 경우 method를 재정의했다고 하며 오버라이드라고 한다.

	- 오버로딩 
		- 같은 이름을 가지고 있는 함수이지만 인자 수를 다르게 줄 수 있다. 알아서 동작하는게 달라지는 것.
		- range 함수를 생각해라.

### class 쓰는 법

- class명은 대문자로 적어준다. 괄호 안에는 parent class가 들어간다.
- 파이썬의 class 안의 method에서는 관례적으로 첫번째 argument에는 self를 적어준다. 호출 시 호출한 객체도 전달되어야 하기 때문이다.
```python
class Car():
  def __init__(self): # method는 처음에 self가 들어가야 한다. argument가 없는 상태.
  self.color="black" # __init__(self)는 호출할 때 무조건 실행되는 함수.

# 만약 만들 때 color를 지정하고 싶을 때,
class Car():
  # 생성자
  def __init__(self,color): # 여기서 color는 argument
  self.color = color # attribute를 정하고 싶으면 self를 앞에 써라.
    # 앞의 color는 attribute, 뒤에 color는 argument.

  # 소멸자, 꼭 안써줘도 된다.
  def __del__(self):
    pass

  # 일반 method들도 쓸 수 있다.
  def run(self):
    pass
```
- class 호출할 때는 instance를 정해준다.
```python	
# instance mycar로 Car class 호출
mycar = Car()
# Car 안에 method 호출
mycar.run() 
mycar.color # 파이썬은 약화된 객체지향을 지향하기 때문에, attribute에 쉽게 접근할 수 있게 만들어졌다.
```
### private / protected / public 변수
| base 클래스 속성 | 클래스 내에서의 접근 | 객체에서 접근 | 상속받은 파생 클래스 내에서 접근 | 상속받은 객체에서 접근 |
|-----|-------|------|-------|-------|
|private| 가능 | 불가능| 불가능 | 불가능 |
|protected| 가능 | 불가능 | 가능 | 불가능 |
|public| 가능 | 가능 | 가능 | 가능 |
- private `__` : 나 아니면 안돼. 나만 쓸 수 있어. set-get을 통해서만 접근할 수 있다.
- protected `_` : 상속관계가 아닌 관계는 접근할 수 없어.
