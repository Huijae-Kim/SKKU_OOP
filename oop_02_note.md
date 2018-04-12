# 2주차 강의 내용 (완)
&copy; document created by heejae6021@naver.com

## windows command 사용하기

1. Change directory
```bash
$ cd <directory>
# autocomplete by ‘tab’
$ cd .. # move the upper directory
$ cd ..\..\ # move to upper to upper directory
$ d: # move to D drive
```
2. Check directories under the current directory
```bash
$ dir
# <DIR>. : directory itself
# <DIR>.. : upper directory(상위폴더)
```
3. Help. Tell me how to use the code
```bash
$ <code> /?
```
4. Make directory
```bash
$ md <directory>
# recommand to make directory named English
```
5. Remove directory
```bash
$ rd <directory>
# remove only blank directory
```
6. Make file
```bash
$ copy con <file_name>
$ copy con a.txt
```
> After you write down the text in the file, `ctrl`+`z` > `enter`  to make the file completely.  
7. Check the content of the file
```bash
$ type <file_name>
```
8. Delete the file 
```bash
$ del <file_name>
```
9. Copy the file to the directory
```bash
$ copy <file_name> <directory>
# directory can be written in absolute path. 
# if you want to use relative path, it should be a subfolder in the directory of the file.
``` 
10. Absolute path vs Relative path
```bash
$ cd C:\User\PC\Desktop # absolute path
$ cd .. # relative path
```
11. Run python script
```bash
$ copy con myfirst.py # make script
	print “hello, world” # write script
	ctrl+z > enter
$ python myfirst.py # run python script
```
## Pycharm 주석

1. todo
```python
# todo
```
> 터미널 왼쪽 아래 클릭하면 todo 확인 가능
2. fixme
```python
# fixme
```
> 같은 방식으로 fixme도 todo와 같이 확인 가능
3. 한글 주석
```python
-*- coding: utf-8 -*-
```
> 맨 위에 적어주면 한글 주석 가능
