from constants import TERM_FILE
import os

create_bool_docs_table = "CREATE TABLE IF NOT EXISTS documents (id INTEGER PRIMARY KEY,"
document_table_keys = "documents (id,"
f = open(TERM_FILE)
for line in f:
    line = line.replace("-", "_")
    create_bool_docs_table +=line.strip() + " string,"
    document_table_keys += line.strip()+ ","
create_bool_docs_table = create_bool_docs_table[:-1] + ");"
document_table_keys = document_table_keys[:-1] + ")"
