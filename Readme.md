# 오토앱리무버
> **귀찮아**

안드로이드 재설치 후 자동으로 깔리는 기본앱들 하나씩 지우기 귀찮아서 만든 자동화 프로그램

# 필수 설치 소프트웨어
- Python 3

# 어떻게 사용할까?
1. [여기](https://developer.android.com/studio/releases/platform-tools?hl=ko)를 눌러 접속합니다.
2. 자신이 쓰는 운영체제에 맞게 **SDK 플랫폼**을 다운로드 합니다.
3. 압축을 풀어 최상단 폴더 이름이 **platform-tools**인 상태로 프로젝트 폴더 최상단으로 이동시킵니다.
4. 앱 패키지 이름을 확인하기 위해 구글플레이에서 **App Inspctor** 설치하고 실행합니다.
5. 지울 앱을 선택하고, **Package name** 밑에 있는 문자열을 **Database.txt**에 입력합니다.
6. 2개 이상 지울 경우에는 한줄 띄우기(\n)로 구분하여 입력합니다.

~~~ database
com.android.vending
com.google.android.projection.gearhead
...
~~~