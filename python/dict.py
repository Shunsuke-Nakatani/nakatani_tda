import copy
import os
import pandas as pd
import json

os.chdir("/Users/sinco/OneDrive/デスクトップ/python")

#sampleの読み込み
df =pd.read_csv('sample.csv')

fr =df["from_address"]
to =df["to_address"]

#FIWAREにimportするデータの形作り
entities=[]
dat ={}

for i,acc in enumerate(fr):
    dat["id"]="urn:ngsi-ld:Store:%d" %i    #idつける

    dat["type"]="Store"    #typeつける

    dat["name"]=acc    #nameつける

    coordinates=[i,0]      #locationつける
    value={"type":"Point","coordinates":coordinates}
    dat["location"]={"type":"geo:json","value":value}

    entities.append(copy.deepcopy(dat))

print(entities)

entities_json=json.dumps(entities,indent=4)
print(entities_json)

