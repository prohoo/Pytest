import time
import os
if __name__ == "__main__":

    time1 = str(int(time.time()))
    filesname = "report_" + time1
    os.mkdir("./reports/" + filesname)