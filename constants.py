TERM_FILE ="./terms"
LONG_DIR = "./Long_data_manuscript/test"
VALIDATION_DIR = "./validation"
START_NUM = 101
DOC_COUNT = 171

PROP_VALIDATION = "./prop_extract_validation/validation.csv"
DOC_NUM_FILE = "./correctDocs.txt"

END_LINE = "Endl"
NEGATION = "Negation"
UNCERTAINTY = "Uncertainty"
SMALLVESSEL = "SmallVessel"
SINUS = "Sinus"
EYE = "Eye"

#Simple just label
DURATION = {"Dur-New", "Dur-Old", "Dur-Undiff"}
MAGNITUDE = {"Mag-Same", "Mag-Modifer", "Mag-Better", "Mag-Large", "Mag-Worse", "Mag-Normal", "Mag-Other", "Mag-Small", "Mag-Resolved" }
JUST_LABEL = DURATION | MAGNITUDE

#double layer table
COMPARTMENTS = {"Compart-IntAx", "Compart-ExtAx", "Compart-External", "Compart-Other"}
PARENCH = {"Parench-Brainstem", "Parench-Cerebellar", "Parench-Cortical", "Parench-Deep"}
DOUBLE_LAYER = COMPARTMENTS | PARENCH

#just text for below 5
JUST_TEXT = {"Direction", "Region", "Territory", "Size", "Ventricle"}

PROP_LIST = JUST_TEXT | DOUBLE_LAYER | JUST_LABEL
