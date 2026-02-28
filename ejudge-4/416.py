from datetime import datetime

line1 = datetime.strptime(input().strip().replace("UTC", ""), "%Y-%m-%d %X %z") 
sec1 = line1.timestamp()
line2 = datetime.strptime(input().strip().replace("UTC", ""), "%Y-%m-%d %X %z") 
sec2 = line2.timestamp()
print(int(sec2 - sec1))