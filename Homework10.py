import datetime
import sys
import time
import zipfile

def progress_porcent():
    for i in range(101):
        time.sleep(0.1)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()

def fname():
    print("this is the name of the script",(sys.argv[0]))
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))

def zipFunction():
    file_name = "filename.zip"
    zip_file = zipfile.ZipFile(file_name,"w")
    zip_file.write("example1.txt")
    zip_file.write("picture1.jpg")
    zip_file.close()

def birth():
    today = datetime.date.today()
    bday = datetime.date(2020, 7, 12)
    till_bday = bday - today    
    print(today)
    print(till_bday)



# progress_porcent()
# fname()
# zipFunction()
birth()
