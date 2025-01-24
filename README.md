# 의료 이미지 라벨링 도구

## 프로젝트 소개
이 도구는 의료 이미지(X-ray 등)에서 골절 부위를 라벨링하기 위한 웹 기반 애플리케이션입니다. YOLO 형식의 데이터셋을 생성하는 데 사용됩니다.

## 주요 기능
- 이미지 업로드 및 관리
- 직관적인 바운딩 박스 그리기
- 골절 유형 분류 (애매한 골절/골절)
- YOLO 형식으로 라벨 데이터 저장
- 기존 라벨 불러오기 및 수정

## 설치 방법

### 필수 요구사항
- Python 3.7 이상
- Flask

### 설치 단계
1. 저장소 클론
~~~bash
git clone [저장소 URL]
cd [프로젝트 폴더]
~~~

2. 가상환경 생성 및 활성화
~~~bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
~~~

3. 필요한 패키지 설치
~~~bash
pip install -r requirements.txt
~~~

## 사용 방법

1. 서버 실행
~~~bash
python app.py
~~~

2. 웹 브라우저에서 접속
- http://localhost:5002 로 접속

3. 이미지 준비
- `static/images` 폴더에 라벨링할 PNG 이미지 파일을 넣어주세요

4. 라벨링 방법
- 이미지 위에서 마우스로 드래그하여 바운딩 박스 생성
- 드롭다운 메뉴에서 골절 유형 선택
- 저장 버튼 클릭하여 라벨 정보 저장

## 디렉토리 구조
~~~
프로젝트/
├── app.py              # 메인 애플리케이션 파일
├── static/
│   ├── images/         # 라벨링할 이미지 저장
│   └── labels/         # YOLO 형식의 라벨 파일 저장
├── templates/
│   └── index.html      # 메인 페이지 템플릿
└── requirements.txt    # 필요한 패키지 목록
~~~

## 라벨 형식
- YOLO 형식으로 저장됨
- 각 줄: `<class> <x_center> <y_center> <width> <height>`
- 클래스: 0 (애매한 골절), 1 (골절)
- 모든 좌표는 정규화됨 (0~1 사이 값)

## 문제 해결
- 이미지가 보이지 않을 경우: `static/images` 폴더에 PNG 파일이 있는지 확인
- 라벨이 저장되지 않을 경우: `static/labels` 폴더의 쓰기 권한 확인
- 서버 오류: 콘솔 로그 확인

## 기여 방법
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 연락처
문제나 제안사항이 있으시면 이슈를 등록해주세요.