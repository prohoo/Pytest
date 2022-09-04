import datetime
import time

import pytest
import os
if __name__ == "__main__":
    pytest.main()

    time1 = str(int(time.time()))
    filesname = "./reports/report_" + time1

    #在./reports这个目录下创建filesname文件，此时文件内容是空的
    os.mkdir(filesname)
    time.sleep(3)

    #把./temps里的数据生成allure数据到filesname这个文件里面去
    os.system("allure generate ./temps -o "+filesname+" --clean")