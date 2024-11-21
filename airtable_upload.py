from pyairtable import Api
import pandas as pd
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# Airtable 설정
access_token = os.getenv("ACCESS_TOKEN")  # .env에서 Access Token 가져오기
base_id = os.getenv("BASE_ID")  # .env에서 Base ID 가져오기
table_id = os.getenv("TABLE_ID")  # .env에서 Table ID 가져오기

# Airtable 테이블 연결
api = Api(access_token)
table = api.table(base_id, table_id)
# print(table.all())

# CSV 데이터 로드
df = pd.read_csv("tools_data_cleaned.csv")

# 데이터 Airtable로 업로드
for _, row in df.iterrows():
    record = {
        "Name": row["Name"],
        "Link": row["Link"],
        "Description": row["Description"],
    }
    table.create(record)

print("Airtable로 데이터 업로드 완료.")
