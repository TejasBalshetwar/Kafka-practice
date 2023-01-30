# from ksql import KSQLAPI
# ksql = KSQLAPI('http://localhost:8088')

# print(ksql.ksql("SHOW TOPICS;"))
# print("\n")
# print(ksql.ksql("SHOW STREAMS;"))

# # Value example {"timestamp": "12:10:12", "level": "CRITICAL", "message": "PROJECT CRASHED"}
# # ksql.ksql("CREATE STREAM my_stream (timestamp VARCHAR, level VARCHAR, message VARCHAR) WITH (KAFKA_TOPIC='first', VALUE_FORMAT='JSON');")

# print(ksql.ksql("PRINT FIRST FROM BEGINNING;"))


# CREATE STREAM CRITICAL_LOG AS SELECT * FROM LOG WHERE LEVEL = 'critical'; new stream from existing stream

from ksql import KSQLAPI
import json

def str_to_json(str):
    return json.loads(str)

ksql_client = KSQLAPI(url='http://localhost:8088')
# query = "SELECT * FROM CRITICAL_LOG;"
# try:
#     rows = ksql_client.query(query)
#     for row in rows:
#         if "finalMessage" not in row and "header" not in row :
#             print(row)
# except Exception as e:
#     pass
