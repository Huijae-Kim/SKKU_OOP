# 7주차 강의 내용 (완)

&copy; document created by heejae6021@naver.com

## Error 관련

### `try:`, `except:`

- 통제가 불가능한 에러가 발생할 위험이 있을 때 try, except 구문을 써야한다.
- 속도가 느려질 가능성이 있으니 꼭  필요한 경우에 써야 한다.
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

- 같은 directiory에 있으면 그냥 파일명만 쓰면 된다. (상대경로)
- 파일 open 모드
	1. read : 읽기만 가능
	2. write : 쓰기 가능(새파일을 만들어서 쓴다)
	3. append : 기존 파일에 추가/수정이 가능

```python
fp = open("data.csv")
fp = open("data.csv", "r")
```
- 파일에서 읽어오는 형태는 늘  string 형태로 저장된다.
- csv file 마지막에도 늘 enter로 줄바꿈 되어있는 것을 권장.
- -close() 명시적으로 써주는 것이 좋당.

## OOP
- Object Oriented Programming
- Object = thing, 객체 (무형, 유형 모두 포함)
- Class : object를 설명하는 blue print(설계도), 포괄적인 개념
- Class를 현실화하면 개체(Instance)가 된다.
- 우리는 앞으로 class를 선언해서 그걸로 개체를 만들어서 프로그램을 짤 것이다.

### class
- 명사 : attribute[속성] (object가 가지고 있는 특징)
- 동사 : method (할 수 있는 일, function과 비슷)
- (예) '차'라는 class : 속성(색상, 승차인원, 마력), 매쏘드(굴러간다, 문이 열린다)

### class의 특징
1. 캡슐화, 은닉화 : 차에 관련된 모든 속성은 다 드러나야 한다. 그리고 외부에서 쉽게 바꿀 수 없어야 한다. 혹시 attribute를 알아내거나 지정하고자 할 때 set-get method(SetColor( ), GetColor( ))라는 것을 이용한다.  attribute를 set-get method를 통하지 않고서는 알 수 없다.
2. 상속
	- class 간의 부모/자식 관계가 성립한다.
	- child는 parent의 attribute, method를 모두 갖는다.
	- parent는 하나만 갖는 것을 지향한다. 동시/다중상속도 가능하긴 하지만 attribute나 method가 겹칠 수 있기 때문에 지양한다.

3.  다형성
	- 다양한 형태를 인정한다.
	- method 오버라이드 : parent가 가지고 있는 method를 다시 정의해서 사용하는 것. "재정의"
		- car라는 parent class에 color라는 속성, run( )이라는 method가 있다.
		- child class에 동일하기 run( )이라는 method가 있는데 조금 다르다.
		- 이러한 경우 method를 재정의했다고 하며 오버라이드라고 한다.
	- 오버로딩 : 같은 이름을 가지고 있는 함수이지만 인자 수를 다르게 줄 수 있다. 알아서 동작하는게 달라지는 것.
		- range 함수를 생각해라.
### class 쓰는 법

```python
# class명은 대문자로 적어준다. 괄호 안에는 parent class가 들어간다.
class Car():
	def __init__(self): # method는 처음에 self가 들어가야 한다. argument가 없는 상태.
	self.color="black" # 무조건 실행되는 함수.
# 만약 만들 때 color를 지정하고 싶을 때,
class Car():
	# 생성자
	def __init__(self,color): # 여기서 color는 argument
		self.color = color # attribute를 정하고 싶으면 self를 앞에 써라.
		# 앞의 color는 attribute, 뒤에 color는 argument.
	# 소멸자, 꼭 안써줘도 된다.
	def __del__(self):
		pass # 소멸자 이 것을 써줘야 끝이나는 것..(??)
	# 일반 method들도 쓸 수 있다.
	def run(self):
# self를 쓰면 전역적으로 쓴다.

mycar = Car() # instance명을 mycar라고 하자.
mycar.run() # 이렇게 method를 호출할 수 있다.
mycar.color # 파이썬은 약화된 객체지향을 지향하기 때문에, attribute에 쉽게 접근할 수 있게 만들어졌다.
# __ : private : 나 아니면 안돼. 나만 쓸 수 있어. set-get을 통해서 접근할 수 있다.
# _ : protected : 상속관계가 아닌 관계는 접근할 수 없어.
# instance.method 나오면 class인 것이다.
# 앞으로 oop로 코드를 짜야 한다.
```

 
