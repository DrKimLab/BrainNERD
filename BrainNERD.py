import copy
import metrics
import random
from constants import *
from db import *
from dbcreate import *
TERM_MAP = {}



### transpose.py holds all of the functions need to model and then validate term tagging
### Dr. Kim lab, Yale
###
### Contributors: Angelo Olcese, Sarah Chacko


# readTerms goes through terms file to create defaultvalue for TERM_MAP
def readTerms():
    f = open(TERM_FILE, "r")
    for line in f:
        TERM_MAP[line.strip()] = "0"



# readExpected iterates through validation csv file
# This function returns a list of maps, each map representing one document
# This map holds the validation values for each term in that document
#
# filename - path to validation file
def readExpected(filename):
    f = open(filename, "r")
    expectedDocMaps = []
    terms = []
    counter = 0
    for line in f:
        expectedMap = {}
        # First line of validation file has the column headers, which are the terms
        if counter == 0:
            terms = line.strip().split(",")
            counter += 1
        else:
        # Each line will hold the validation value for each term for that document
            line = line.strip().split(",")
            for i in range(0, len(line)):
                expectedMap[terms[i]] = line[i]
            expectedDocMaps.append(expectedMap)
    return expectedDocMaps


# readLongSentences will go through each report's long data and add each sentence to a list
# Each sentence is a list of all of the (word, label) pairs present in the sentence
#
# filename - path to long data file
def readLongSentences(filename):
    f = open(filename, "r")
    sentences = []
    temp = []
    counter = 0
    for line in f:
        line = line.strip()
        # First line is not needed
        if counter == 0:
            counter += 1
            continue
        terms = line.split()
        label = terms[1]
        #  If the label is ENDLINE then we end that sentence and start a new one
        if label == END_LINE:
            sentences.append(temp)
            temp = []
        # Otherwise we add the pair to the temp array representing this sentence
        else:
            temp.append([" ".join(terms[2:]),label])
    return sentences


# evalPresentTerms is the function that defines our model for evaluating a sentence
# Input is all of the sentences in a document
# Output will be map representing what tag should be given to each term in the document
# Input:
# sentences - List of sentences, where each sentence is a list of (text, label) pairs
# Output:
# reportTermVals    -
def evalPresentTerms(sentences):
    reportTermVals = copy.deepcopy(TERM_MAP)
    reportTermProps = copy.deepcopy(TERM_MAP)
    #Go through each sentence
    for s in sentences:
        negation_present = False
        uncertainty_present = False
        smallVessel_present = False
        skip_sentence = False
        # Iterate through each text, label pair
        if skip_sentence:
            continue
        else:
            for textLabel in s:
                text = textLabel[0]
                label = textLabel[1]
                # If label is negation, we note that there has been a negation
                if label == NEGATION:
                    negation_present = True
                # If label is uncertainty, we note that there has been uncertainty
                elif label == UNCERTAINTY:
                    uncertainty_present = True
                elif label == SMALLVESSEL:
                    smallVessel_present = True

                # For now, all surgical tags count as Surgical-All
                if label[0:8] == "Surgical":
                    label = "Surgical-All"
                # If label is one of the important terms
                if label in reportTermVals:
                    if label == "Stroke" and smallVessel_present:
                        continue
                    # If negation is present previously in the sentence, we add the term as pertinent negative
                    if negation_present:
                        #We prefer positive tags so only change the tag if term is not mentioned yet
                        if reportTermVals[label] == "0":
                            reportTermVals[label] = "-"
                            reportTermProps[label] = "-"
                    # If negation isn't present, but uncertainty is we will add the term as possible
                    elif uncertainty_present:
                        #We prefer positive tags so only change the tag if it is not already pertinent positive
                        if reportTermVals[label] != "+":
                            reportTermVals[label] = "p"
                            reportTermProps[label] = "p"
                    #Term is mentioned without negation or uncertainty so add it as pertinent positive
                    else:
                        reportTermVals[label] = "+"
                        if  isinstance(reportTermProps[label], str):
                            reportTermProps[label] = []
                        #category, props = extractProperties(label, s)
                        reportTermProps[label].append(extractProperties(text, label, s))


    # This will look like {term1: "+", term2: "p", term3: "+", term4: "-",...}
    return reportTermVals, reportTermProps

#Function which takes in a (term, label) pair as well as the sentence it is in,
# then extracts the properties which apply to that term
# Input:
# termLabel    - The term, label pair that is taken in from the long data
# sentence     - The full long data for the sentence
# Output:
# props        - The properties in the sentence which are modeled to belong to the termLabel
def extractProperties(term, label, sentence):
    props = {"Injury": term}
    for textLabel in sentence:
        text = textLabel[0]
        label = textLabel[1]
        if label in PROP_LIST:
            category = "Unknown"
            # Check if label is one that only needs text value
            if label in JUST_TEXT:
                #For the JUST_TEXT values, the label is the category
                if label in props:
                    props[label].append(text)
                else:
                    props[label] = [text]
            #Check if the label is on that needs just the label
            elif label in JUST_LABEL:
                #Decide which category the label belongs to
                if label in MAGNITUDE:
                    category = "Magnitude"
                elif label in DURATION:
                    category = "Duration"

                #Add the label to the dictionary under the category
                if label in props:
                    props[category].append(label)
                else:
                    props[category] = [label]
            # Check if label belongs to one that needs two layer table
            elif label in DOUBLE_LAYER:
                #Decide which category the label belongs to
                if label in COMPARTMENTS:
                    category = "Compartment"
                elif label in PARENCH:
                    category = "Parench"
                if category in props:
                    if label in props[category]:
                        props[category][label].append(text)
                    else:
                        props[category][label] = [text]
                else:
                    props[category] = {label: [text]}
    return props

# evaluateDocumentSuccess will compare our model evaluation to the expected validation values
# Input:
# modelTermVals    - The term, value pair that is the result of our model tagging for a document
# expectedTermVals - The term, value pair that is the expected value for each term as read in the validation file
# Output:
# correct - is map of terms to boolean of whether their value was correctly predicted by the model
def evaluateDocumentSuccess(modelTermVals, expectedTermVals):
    correct = copy.deepcopy(TERM_MAP)
    for key, value in modelTermVals.items():
        if expectedTermVals[key] == value:
            correct[key] = (True, value)
        else:
            correct[key] = (False, expectedTermVals[key], value)
    return correct


# evaluateDocumentSuccessThreeGroups will compare our model evaluation to the expected validation values while making
# "0" equivalent to "-"
# Input:
# modelTermVals    - The term, value pair that is the result of our model tagging for a document
# expectedTermVals - The term, value pair that is the expected value for each term as read in the validation file
# Output:
# correct - is map of terms to tuples of (boolean of correct guess, expected value, predicted value)
def evaluateDocumentSuccessThreeGroups(modelTermVals, expectedTermVals):
    correct = copy.deepcopy(TERM_MAP)
    for key in correct:
        if expectedTermVals[key] == modelTermVals[key]:
            correct[key] = (True, modelTermVals[key])
        elif (expectedTermVals[key] == "-" or expectedTermVals[key] == "0") and (modelTermVals[key] == "-" or modelTermVals[key] == "0"):
            correct[key] = (True, "-")
        else:
            correct[key] = (False, expectedTermVals[key], modelTermVals[key])
    return correct

# evaluateTotalSuccess iterates through a single document success map in order to evaluate
# how our model is performing
def evaluateTotalSuccess(correctTerms, successNums):
    documentFullyCorrect = True
    for term, vals in correctTerms.items():
        if vals[0] == True:
            successNums[term] += 1
        else:
            documentFullyCorrect = False

    if documentFullyCorrect:
        successNums["documents"] += 1

    return successNums


def instantiateSuccessNums():
    ratios = {"documents": 0}
    for key in TERM_MAP:
        ratios[key] = 0
    return ratios

def writeReport(successNums):
    hits = 0
    numTerms = 0
    print("-------------")
    print("Number of documents is "+str(NUM_DOCS))
    print("\nTerm percentages:")
    for term, numCorrect in successNums.items():
        if term == "documents":
            continue
        hits += numCorrect
        numTerms += 1
        print(term + ": "+str(float(numCorrect)/NUM_DOCS * 100)+"% ("+str(numCorrect)+" correct)")
    print("\nTotal terms correct: "+str(float(hits)/(NUM_DOCS*numTerms) * 100)+"% ("+str(hits)+" out of "+str((NUM_DOCS*numTerms))+" correct)")
    print("-------------")
    print("Documents that were 100% correctly modeled: "+str(successNums["documents"]))

def printFailures(modelTermVals, expected, correctTerms, doc_num):
    incorrectTerms = []
    for term, correct in correctTerms.items():
        if not correct[0]:
            incorrectTerms.append((term, modelTermVals[term], expected[term]))
    if len(incorrectTerms) != 0:
        print("Document ID: " + str(doc_num))
        print(incorrectTerms)

# aggregateConfusionMatrix will take the success evaluation of a document and aggregate the info into the confusion matrix
# Input:
# matrix    - The matrix which will hold the aggregate confusion matrix info
# correctTerms - is map of terms to tuples of (boolean of correct guess, expected value, predicted value) output of document evaluation
# Output:
# matrix    - The updated confusion matrix with previous values + the values from inputted document evaluation.
def aggregateConfusionMatrix(matrix, correctTerms):
    pos = 0
    possible = 1
    neg = 2
    for term, vals in correctTerms.items():
        index1 = "0"
        index2 = "0"
        if vals[0]:
            if vals[1] == "p":
                index1 = possible
                index2 = possible
            elif vals[1] == "+":
                index1 = pos
                index2 = pos
            elif vals[1] == "-" or vals[1] == "0":
                index1 = neg
                index2 = neg
        else:
            if vals[1] == "p":
                index2 = possible
            elif vals[1] == "+":
                index2 = pos
            elif vals[1] == "-" or vals[1] == "0":
                index2 = neg
            if vals[2] == "p":
                index1 = possible
            elif vals[2] == "+":
                index1 = pos
            elif vals[2] == "-" or vals[2] == "0":
                index1 = neg
        matrix[index1][index2] += 1
    return matrix

def evaluateModel(start_num, num_docs):
    readTerms()
    successNums = instantiateSuccessNums()
    expectedDocMaps = readExpected((VALIDATION_DIR+"/validation_final.csv"))
    global NUM_DOCS
    NUM_DOCS = num_docs
    # 3 by 3 matrix where rows from top to bottom are +, p, -, and columns left to right are same
    matrix = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(start_num, start_num + NUM_DOCS):
        #Read in the long sentences
        sentences = readLongSentences(LONG_DIR+"/long_"+str(i)+".csv")
        #Using our model to predict the term booleans
        modelTermVals, _ = evalPresentTerms(sentences)
        # Evaluating our success
        correctTerms = evaluateDocumentSuccessThreeGroups(modelTermVals, expectedDocMaps[i-1])
        successNums = evaluateTotalSuccess(correctTerms, successNums)
        matrix = aggregateConfusionMatrix(matrix, correctTerms)
        #printFailures(modelTermVals, expectedDocMaps[i-1], correctTerms, i)
    metrics.metrics(matrix, True)
    writeReport(successNums)

def runModelToDB(start_num, num_docs):
    readTerms()
    NUM_DOCS = num_docs
    modeledDocs = []
    for i in range(start_num, start_num + NUM_DOCS):
        #Read in the long sentences
        sentences = readLongSentences(LONG_DIR+"/long_"+str(i)+".csv")
        #Using our model to predict the term booleans
        modelTermVals, _ = evalPresentTerms(sentences)
        modelTermVals["id"] = i
        modeledDocs.append(modelTermVals)
    conn = create_connection("./data.sql")
    execute_query(conn, create_bool_docs_table)
    execute_query(conn, add_bool_docs(modeledDocs))

    # get column headers
    header_table = execute_query(conn, "PRAGMA table_info('documents')", True)
    headers = [h[1] for h in header_table]

    #Run the select queries in the "/queries folder"
    #Output into /queries-output folder
    for q in getSelectQueries():
        filename = "./queries-output/" + q[0].split(".")[0]+"-output.txt"
        prettyOutput(filename, headers, execute_query(conn, runSelectQuery(q), True))

def confidenceInterval(start_num, num_docs, sample_num_docs, iterations):
    readTerms()
    expectedDocMaps = readExpected((VALIDATION_DIR+"/validation_final.csv"))
    global NUM_DOCS
    NUM_DOCS = num_docs
    precisionScores = []
    recallScores = []
    f1Scores = []
    for _ in range(0, iterations):
        # 3 by 3 matrix where rows from top to bottom are +, p, -, and columns left to right are same
        matrix = [[0,0,0], [0,0,0], [0,0,0]]
        for j in range(0, sample_num_docs):
            i = random.randrange(start_num, start_num + num_docs)
            #Read in the long sentences
            sentences = readLongSentences(LONG_DIR+"/long_"+str(i)+".csv")
            #Using our model to predict the term booleans
            modelTermVals, _ = evalPresentTerms(sentences)
            # Evaluating our success
            correctTerms = evaluateDocumentSuccessThreeGroups(modelTermVals, expectedDocMaps[i-1])
            matrix = aggregateConfusionMatrix(matrix, correctTerms)
            #printFailures(modelTermVals, expectedDocMaps[i-1], correctTerms, i)
        precision, recall, f1 = metrics.metrics(matrix, False)
        precisionScores.append(precision)
        recallScores.append(recall)
        f1Scores.append(f1)
    precisionScores.sort()
    recallScores.sort()
    f1Scores.sort()
    offset95 = int(iterations * .025)
    precision95 = 0
    recall95 = 0
    f195 = 0
    for i in range(offset95, iterations - offset95):
        precision95 += precisionScores[i] / (iterations - (2*offset95))
        recall95 += recallScores[i] / (iterations - (2*offset95))
        f195 += f1Scores[i] / (iterations - (2*offset95))
    print("Precision95: "+ str(precision95))
    print("Recall95: "+ str(recall95))
    print("F1_95: "+ str(f195))

    offset99 = int(iterations * .005)
    precision99 = 0
    recall99 = 0
    f199 = 0
    for i in range(offset99, iterations - offset99):
        precision99 += precisionScores[i] / (iterations - (2*offset99))
        recall99 += recallScores[i] / (iterations - (2*offset99))
        f199 += f1Scores[i] / (iterations - (2*offset99))
    print("Precision99: "+ str(precision99))
    print("Recall99: "+ str(recall99))
    print("F1_99: "+ str(f199))



if __name__ == "__main__":
    evaluateModel(START_NUM, DOC_COUNT)
    runModelToDB(START_NUM, DOC_COUNT)
    # confidenceInterval(START_NUM, DOC_COUNT, 100, 1000)
FooterYale University
