#import logging
#import logstash
#from logstash_formatter import LogstashFormatter
from db import db

def parse(filename):
    comment = ";"
    partition = "Partition"
    lines = []
    partitions = {}
    clean = []
    with open(filename, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        if comment in line:
            if partition in line:
                meaning = line.split()
                if "Max" not in meaning[1]:
                    partitions[int(meaning[2])] = meaning[3]
                    
        else:
            clean.append(line)
    
    return clean, partitions

def logstash_input(clean, partitions):
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger()
    # formatter = LogstashFormatter()
    # handler = logstash.LogstashHandler("logstash", 5959)
    # handler.setFormatter(formatter)
    status = {"1":"Complete", "0":"Failed", "5":"Cancelled"}
  #  logger.addHandler(handler)
    values = {0:"Job Number", 1:"Submit Time", 2:"Wait Time",
              3:"Run Time (seconds)", 4:"Number of Allocated Processes", 
              5:"Average CPU Time Used", 6:"Used Memory (Kb)", 7:"Requested Number of Processors",
              8:"Requested Time (seconds)", 9:"Requested Memory (Kb)", 10:"Status", 11:"User ID", 12:"Group ID",
              13:"Executable (Application) Number", 14:"Queue Number", 15:"Partition", 16:"Preceding Job Number",
              17:"Think Time from Preceding Job"
    }
    position=0
    for line in clean:
        position+=1
        elements = line.split()
        logged = {}
        for i in range(len(elements)):
            if i == 15:
                logged[values[i]] = partitions[int(elements[i])]
            if i == 10:
                logged[values[i]] = status[elements[i]]
            else:
                logged[values[i]] = int(elements[i])
        
        db.create(index='mei-2017', doc_type='log', id=position, body=logged)
        #logger.info(str(position), extra=logged)

if __name__ == "__main__":
    
    clean, partitions = parse("example.swf")
    logstash_input(clean, partitions)
