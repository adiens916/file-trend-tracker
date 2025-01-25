# File Trend Tracker
![](/assets/demo.png)

## 기능
- 특정 폴더 내 파일 수정한 날짜 기준으로 개수 & 크기 세기  
: 이를 통해 해당 폴더와 관련된 활동 추이를 대략적으로 가늠할 수 있음.
- 그래프 표현
- CSV 저장

## 설치
```
# 필요한 패키지들 설치
pip install pandas matplotlib setuptools
# 개발 모드로 설치 (현재 프로젝트 개발할 때만)
pip install -e .
```

## 주의
- Python 3.13인 경우, matplotlib이 가상 환경에서 오류 남.  
=> Python 3.12를 기반으로 가상 환경 만들기 / 가상 환경 안 쓰기

  > There is a bug in python 3.13.0 on windows when it runs in a venv  
  [출처 1](https://discuss.python.org/t/this-probably-means-that-tcl-wasnt-installed-properly-tried-all-the-solutions-that-i-found-in-the-internet-just-tryna-do-my-homework-please-help/68692/6)

  > The latest Python 3.13.0 does not work with PyCharm for the TCL file. Go back one version on Python Interpreter and the PyCharm will work properly with the TCL file.  
  [출처 2](https://www.reddit.com/r/pycharm/comments/1gsj3jj/comment/lxjjqju/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)
