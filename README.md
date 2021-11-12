# 코드 모음

## 나중에 필요할 것 같은 코드들 편하게 쓸 수 있도록 모아둔 레포지토리!

### 1. 이미지 크롤링

[Codes](https://github.com/ji-in/jiin-collection/blob/main/crawler.py)

이 코드는 `ChromeDriver`를 사용하여 크롤링을 한다. 그래서 `ChromeDriver`를 다운받아야 한다. 

자신의 크롬과 버전이 동일한 `ChromeDriver`를 설치하고, 드라이버와 같은 경로에서 크롤링 코드를 실행하면 된다.

그리고 셀레니움 라이브러리가 필요한데, `pip install selenium`으로 다운받으면 된다. 

`ChromeDriver`을 다운로드 하는 방법은 구글링하면 나오지롱~

크롤링을 다 끝내고 이미지가 모아졌으면, 이미지들을 한번 더 확인해야 한다. 내가 원치 않는 이미지들이 있을 수 있기 때문에다. 그 이미지들을 수동으로 하나하나 삭제해준다.

### 2. 얼굴만 크롭하기

[Codes with dlib]()

dlib 과 openCV 를 사용했다.

OpenCV 의 Haar Cascades 를 사용하여 얼굴을 크롭할 수도 있다. (haar cascades를 사용하는 코드는 시간 날 때 올리겠음!) 어떤게 결과가 더 좋은지는 비교는 안해봤다. dlib 사용해도 충분히 잘 크롭된다.

