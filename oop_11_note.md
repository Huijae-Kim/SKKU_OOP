# 11주차 강의 내용 
&copy; document created by heejae6021@naver.com
 ## GUI
### 설치
- https://www.lfd.uci.edu/~gohlke/pythonlibs/
- 윈도우에서 쉽게 패키지를 깔 수 있도록 캘리포니아 주립대에서 배포하는 사이트
- packages 깔아준다 : NumPy(수학관련), SciPy(수학관련), PyQt4(GUI관련),  Scikit-image(이미지프로세싱관련), Scikit-learn(머신러닝관련), Matplotlib(일반적인 plot관련), PyOpenGL(accelerate까지 깔아준다, graphic관련), PyQtGraph(실시간 plot관련)
- window command창 연다.
```bash
cd Downloads
python -m pip install numpy~ #<tab>으로 자동완성
python -m pip install pyqt4~
 
# 나머지도 다 이렇게 한 다음 마지막으로 다음을 적어 실행해준다.
python -m pip install pyqtgraph 
```
### PyQt
```bash
C:\Python27\Lib\site-packages\PyQt4\designer 실행 
```
1. 오른쪽에 property는 mainwindow나 클릭하는 위젯의 속성들과 그에 대한 값이 적혀있다. 
2. 위젯은 mainwindow에 올리는 하나하나의 component를 의미한다.
3. PushButton
	- objectName은 이 위젯의 이름을 의미. 유일한 이름을 가져야 한다. 중복되면 안된다.
	- enabled 체크하지 않으면 그 버튼을 쓸 수 없게 한다. > false나 true로 셋팅을 하게 된다.
	- geometry는 그 위젯의 크기를 의미한다. [(좌측상단의 좌표), 좌표기준 width x height]
	- sizeIncrement는 윈도우가 커짐에 따라 얼만큼씩 커지는가에 대한 것이다. 
	- font는 그 안에 text의 글꼴을 바꿔줄 수 있다.
	- 글을 쓸 때는 가변폭(~ ,굴림), 코드를 쓸 때는 고정폭(~ 체, 굴림체) 
	- shortcut은 단축키를 사용할 수 있게 해준다.
4. `mainui.ui`로 저장한 다음에 command 창에서 다음을 적어준다.
```bash
C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py mainui.ui -o mainui.py # 안되면 아래
C:\Python27\python.exe C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py mainui.ui -o mainui.py 
# pyuic.py는 ui가 xml코드로 되어있는 것을 py코드로 바꿔준다.
C:\Python27\python.exe C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py mainui.ui -x -o mainui.py
# -x 넣어주면 main function도 들어가기 때문에 이렇게 써주고 python file 작동시키면 화면 나온다.
python mainui.py #로 실행
```
5. `class Ui.MainWindow(object)` 수정
```python
def setupUi(self, MainWindow):
	...
	self.pushButton.clicked.connect(self.myfunc)
 
def myfunc(self): 
    self.lineEdit.setText("You clicked")
    # pushButton이라는 object를 누르면 lineEdit이라는 object에 text를 적어준다.
```
6. 만약에 버튼을 클릭했을 때 다른 모든 버튼에도 영향을 주게 해서 enabled를 false로 바꿔주고 싶다면 각 object들을 한 list에 넣어서 한꺼번에 실행해줄 수 있다.
7. widget의 크기에 따라 잘 변동하게 해주고 싶다. > `layout`을 쓴다.
	- 오른쪽 widget box에 맨 위에 `layouts`이 있다. 
	- main window에서 오른쪽 버튼 누르고 layout에 들어가면 한꺼번에 자동으로 layout을 정리해주는 것도 있다.
	- form layout을 사용하면 상위 배치?가 된다.
	- grid layout을 사용하면 중간 배치?가 된다.