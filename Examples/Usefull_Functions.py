#This function will filter the reports by date
def Filter_Date(s, first, last):
    d1 = s.rfind("Date")
    e1 = s.rfind("Date") + 25
    
    start = s.rfind(first) + len(first)
    end = s.rfind(last, start)
    Lowerstar = s.rfind(first) + len(first)
    Lowerend = s.rfind(last, start)
    date = s[d1:e1]
    text = s[start:end].strip(":")
    return nlp(date + text)
  
  
#This function will filter the reports by findings  
def Filter_Findings(s):
    s = s.lower()
    first = "findings"
    last = "impression"
    d1 = s.rfind("date")
    e1 = s.rfind("date") + 25 
    start = s.rfind(first) + len(first)
    end = s.rfind(last, start)
    date = s[d1:e1]
    findings = s[start:end].strip(":")
    return nlp(date+findings)


  
# Color of the NER Categories and how to change them in Displacy  
displacy_colors = { "ATROPHY":"#eef5fb", "GRAY-WHITE": "#deebf7", "LAM_NECROSIS":"#cee1f3",
                   "DENSITY-HIGH":"#bed8ef", "DENSITY-ISO":"#afceec", "DENSITY-HIGH":"#9fc5e8",
                   "DENSITY-MIXED":"#8fbbe4", "DENSITY-UNDIFF":"#7fb2e0","CLOT":"#6fa8dc",
                   "CONTUSION": "#609ed8" , 
                   "HEMORRHAGE": "#eb0087" ,
                   "STROKE": "#f91010" , 
                   "VASCULAR": "#3182cc", "MALFORMATION": "#2e78bc","FLUID COLLECTION": "#2a6eac",
                   "Edema": "#26649c", "HERNIATION": "#225a8d", "MASS EFFECT": "#1e4f7d" ,
                   "MIDLINESHIFT": "#b1b1ff", "LESION": "#173b5d", "HYDROCEPHALUS": "#1d4d70" , 
                   "PNEUMOCEPHALUS": "#184e75", "SURGICAL-AFTER": "#124f7b" , 
                   "SURGICAL-CLIP": "#0d5080" ,
                   "SURGICAL-DRAIN":"#075086" , "SURGICAL-ENDOVASCULAR" : "#02518b" , 
                   "SURGICAL-HOLE":"#054ba2" , "SURGICAL-MONITOR": "#0b4c9c",
                   "SURGICAL-PLACEMENT": "#124d95" ,
                   "SURGICAL-REMOVAL": "#184d8f", "FRACTURE":"#c713ff" , 
                   "MAG-NORMAL": "#e5f5e0", "MAG-RESOLVED": "#d9f0d1" ,
                   "MAG-BETTER": "#c0e7b4" , "MAG-WORSE": "#a7dd96", 
                   "MAG-SAME": "#8ed478", "MAG-LARGE" : "#81cf69",
                   "MAG-SMALL" : "#00e8eb", "SIZE": "#00eb78" ,
                   "MAG-MODIFIER":"#5dbf3e" , "MAG-OTHER": "#55b139",
                   "COMPART-EXTERNAL": "#fee6ce", 
                   "SINUS": "#fdd2a8", "COMPART-EXTAX": "#fcbf81",
                   "VENTRICLE" : "#fcab5b", "DIRECTION": "#ff6500",
                   "COMPART-INTAX" : "#fa8e21", "PARENCH-DEEP": "#fa840e",
                   "PARENCH-BRAINSTEM" : "#ef7a05", "PARENCH-CEREBELLAR": "#dc7004",
                   "PARENCH-CORTICAL": "#c96704", "REGION": "#b65d04",
                   "TERRITORY":"#8f4903", "COMPART-OTHER": "#693502", 
                   "SMALLVESSEL": "#fd9c9c",
                   "DATE": "#ffff00", "TIME": "#d5ff00",
                   "DUR-NEW": "#fbd45d", "DUR-OLD":"#fac523", "DUR-UNDIFF": "#ebb300",
                   "ENDL": "#f6f6f6", "NEGATION":"#808080","UNCERTAINTY": "#d8d8d8"
                  } 
                   
Options= {"ents": ["ATROPHY", "GRAY-WHITE", "LAM_NECROSIS",
                   "DENSITY-HIGH", "DENSITY-ISO", "DENSITY-HIGH",
                   "DENSITY-MIXED", "DENSITY-UNDIFF","CLOT",
                   "CONTUSION", "HEMORRHAGE", "STROKE" ,
                   "VASCULAR", "MALFORMATION","FLUID COLLECTION",
                   "Edema", "HERNIATION", "MASS EFFECT",
                   "MIDLINESHIFT", "LESION", "HYDROCEPHALUS", 
                   "PNEUMOCEPHALUS", "SURGICAL-AFTER", 
                   "SURGICAL-CLIP",
                   "SURGICAL-DRAIN", "SURGICAL-ENDOVASCULAR" , 
                   "SURGICAL-HOLE", "SURGICAL-MONITOR",
                   "SURGICAL-PLACEMENT" ,
                   "SURGICAL-REMOVAL", "FRACTURE" , 
                   "MAG-NORMAL", "MAG-RESOLVED",
                   "MAG-BETTER", "MAG-WORSE", 
                   "MAG-SAME","MAG-LARGE",
                   "MAG-SMALL", "SIZE" ,
                   "MAG-MODIFIER", "MAG-OTHER",
                   "COMPART-EXTERNAL", 
                   "SINUS", "COMPART-EXTAX",
                   "VENTRICLE" , "DIRECTION",
                   "COMPART-INTAX" , "PARENCH-DEEP",
                   "PARENCH-BRAINSTEM" , "PARENCH-CEREBELLAR",
                   "PARENCH-CORTICAL", "REGION",
                   "TERRITORY", "COMPART-OTHER", 
                   "SMALLVESSEL",
                   "DATE", "TIME",
                   "DUR-NEW", "DUR-OLD", "DUR-UNDIFF",
                   "ENDL", "NEGATION", "UNCERTAINTY"], "colors": displacy_colors}
