import csv
def problem3_7(csvfile,flower):
    with open(csvfile,"r") as asd:
        reader = csv.reader(asd)
        for item in reader:
            if item[0] == flower:
                print(item[1])

problem3_7("flowers.csv","alyssum")