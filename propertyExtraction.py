from BrainNERD import *
from constants import *
import json

NUM_DOCS = 1

def readPropValidation():
    f = open(PROP_VALIDATION)
    counter = 0
    expectedDocMaps = []
    terms = []
    for line in f:
        expectedMap = {}
        if counter == 0:
            terms = line.strip().split("/")
            counter += 1
        else:
        # Each line will hold the validation properties for each term for that document
            line = line.strip().split("/")
            for i in range(0, 2):#len(line)):
                if line[i] == "-" or line[i]  == "0" or line [i] == "p":
                    continue
                else:
                    expectedMap[terms[i]] = json.loads(line[i])
            expectedDocMaps.append(expectedMap)
            counter += 1
        if counter == 2:
            return

def readDocNums():
    f = open(DOC_NUM_FILE)
    docs = []
    for line in f:
        docnum = line.strip()
        docs.append(docnum)

    return docs

def modelWithPropertyExtraction():
    readTerms()
    modeledDocs = []
    for i in range(START_NUM,START_NUM+DOC_COUNT):
        sentences = readLongSentences(LONG_DIR+"/long_"+str(i)+".csv")
        modelTermVals, modelTermProps = evalPresentTerms(sentences)
        modelTermProps["id"] = i
        modeledDocs.append(modelTermProps)

    conn = create_connection("./properties.sql")
    execute_query(conn, create_bool_docs_table)
    execute_query(conn, add_bool_docs(modeledDocs))

    # get column headers
    header_table = execute_query(conn, "PRAGMA table_info('documents')", True)
    headers = [h[1] for h in header_table]

    #Run the select queries in the "/queries folder"
    #Output into /queries-output folder
    for q in getSelectQueries():
        filename = "./queries-output-properties/" + q[0].split(".")[0]
        prettyOutputProperties(filename, headers, execute_query(conn, runSelectQuery(q), True))


if __name__ == "__main__":
    modelWithPropertyExtraction()
FooterYale University
