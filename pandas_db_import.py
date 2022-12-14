import pymysql  # 데이터 베이스별 선택
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:@localhost:3306/lect')  # 데이터 베이스별 연결 문자열은 sqlalchemy에서 확인

sql = 'select * from table_name'

df = pd.read_sql(sql, engine, index_col='index_col')
