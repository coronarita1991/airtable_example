# Airtable 데이터 업로드 스크립트

이 프로젝트는 CSV 파일 데이터를 Airtable에 자동으로 업로드하는 Python 스크립트를 제공합니다.

# 기능
	•	.env 파일을 사용하여 민감한 정보를 안전하게 관리
	•	CSV 데이터를 읽어 Airtable 테이블에 업로드
	•	Airtable API와 Python pyairtable 라이브러리를 사용

# 프로젝트 구조
```
project/
│
├── tools_data_cleaned.csv  # 업로드할 CSV 데이터
├── airtable_upload.py      # Airtable 업로드 스크립트
├── .env                    # 환경 변수 파일 (개인정보 저장)
└── README.md               # 프로젝트 설명 파일
```

# 필수 조건
```
•	Python 3.8 이상
•	Airtable Personal Access Token (PAT)
•	설치된 Python 패키지:
•	pyairtable
•	pandas
•	python-dotenv
```

# 설치 및 설정

##	1.	Python 패키지 설치

`pip install pyairtable pandas python-dotenv`


##	2.	.env 파일 생성
프로젝트 루트 디렉토리에 .env 파일을 생성하고 아래 내용을 추가:

ACCESS_TOKEN=your_personal_access_token
BASE_ID=your_base_id
TABLE_ID=your_table_id

	•	ACCESS_TOKEN: Airtable Personal Access Token (https://airtable.com/account 에서 생성)
	•	BASE_ID: Airtable Base ID (https://airtable.com/api 에서 확인)
	•	TABLE_ID: Airtable 테이블 ID (테이블 설정에서 확인)

##	3.	CSV 데이터 준비
	•	업로드할 데이터를 tools_data_cleaned.csv 파일에 저장합니다.
	•	파일에는 Name, Link, Description 열이 포함되어야 합니다.

# 사용 방법

##	1.	스크립트 실행

`python airtable_upload.py`


##	2.	결과 확인
	•	실행 후 데이터가 Airtable 테이블에 성공적으로 업로드됩니다.
	•	오류가 발생하면 콘솔에 오류 메시지가 출력됩니다.

# 유의 사항

	•	.env 파일에 민감한 정보가 포함되어 있으므로 Git에 추가하지 않도록 .gitignore에 포함하세요.
	•	Airtable의 API 요청 속도 제한에 주의하세요. (기본적으로 초당 5개의 요청 제한)

# 참고 자료
- Airtable API: https://airtable.com/api
- PyAirtable 라이브러리 문서: https://pyairtable.readthedocs.io