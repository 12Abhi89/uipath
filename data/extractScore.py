itr = 1
flag = 1
while flag:
    with open("D:/RS01/uipath/RNS-RS01/data/outputScore.txt", "r") as f:
        outputText = f.read().strip()
        if len(outputText) <=0:
            continue
        for i in list(outputText.split("\n")):
            if str(itr)+":" in i:
                print(i.split("\t")[2])
                itr += 1
            elif "Finished" in i:
                flag = 0

