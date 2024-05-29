import sqlite3
import json
import csv
from sqlite3 import Error
from dbcreate import *
from tabulate import tabulate

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query, output=False):
    cursor = connection.cursor()
    try:
        #print("Query: " + query)
        cursor.execute(query)
        connection.commit()
        if print:
            rows = cursor.fetchall()
            return rows
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def add_bool_docs(docs):
    create_docs = "INSERT INTO " + document_table_keys + " VALUES "
    for doc in docs:
        doc_string = "("+'"' + str(doc["id"]) + '"' + ','
        del doc["id"]
        for k, v in doc.items():
            doc_string += '"' + str(v) + '"' + ','
        doc_string = doc_string[0:-1] + "),"
        create_docs += doc_string
    create_docs = create_docs[0:-1] + ";"
    return create_docs

def getSelectQueries():
    queryfiles = os.listdir("./queries")
    queries = []
    for qf in queryfiles:
        f = open("./queries/"+qf, "r")
        query = [qf]
        for line in f:
            line = line.strip().split(" ")
            query.append((line[0], line[1]))
        queries.append(query)
        f.close()
    return queries

def runSelectQuery(q):
    select = "SELECT * FROM documents WHERE "
    for i in range(len(q[1:])):
        condition = q[i+1]
        if i != 0:
            select += "AND "
        if condition[1] == "-":
            select += "("+condition[0]+'="0" OR '+condition[0]+'="-") '
        elif condition[1] == "p":
            select += condition[0]+'="'+condition[1].lower()+'" '
        elif condition[1] == "+":
            select += "("+condition[0]+'="+" OR '+condition[0]+' LIKE "[{%") '
    return select

def prettyOutput(filename, header, output):
    f = open(filename, "w")
    counts = []
    for j in range(len(header)):
        count = 0
        column_values = [value[j] for value in output]
        for val in column_values:
            if val == "+" or "[" in str(val):
                count += 1
        counts.append(count)
    output.append(counts)
    f.write(tabulate(output, headers=header, tablefmt="'grid'"))
    f.close()

def prettyOutputProperties(filenamebase, header, table):
    #Print the table without injuries
    # f = open(filenamebase+"-doc.txt", "w")
    docOutput = []
    for i in range(len(table)):
        row = []
        for j in range(len(table[i])):
            if "[" in str(table[i][j]):
                row.append("+")
            else:
                row.append(table[i][j])
        docOutput.append(row)
    # f.write(tabulate(docOutput, headers=header, tablefmt="'grid'"))
    # f.close()
    with open(filenamebase+'-doc.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        csvOutput = docOutput
        csvOutput.insert(0,header)
        mywriter.writerows(csvOutput)

    #Print the table with just doc ids and injuries
    # f2 = open(filenamebase+"-injury.txt", "w")
    injuryOutput = []
    for i in range(len(table)):
        for j in range(len(table[i])):
            if "[" in str(table[i][j]):
                injuries = json.loads(table[i][j].replace("\'", "\""))
                for injury in injuries:
                    row = [table[i][0]]
                    for k, v in injury.items():
                        row.append(str(k) + ": "+str(v))
                    injuryOutput.append(row)
    # f2.write(tabulate(injuryOutput, tablefmt="'grid'"))
    # f2.close()
    with open(filenamebase+'-injury.csv', 'w', newline='') as file:
        mywriter = csv.writer(file, delimiter=',')
        csvOutput = injuryOutput
        csvOutput.insert(0,["id"])
        mywriter.writerows(csvOutput)
FooterYale University
