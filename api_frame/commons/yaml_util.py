#读取yaml数据
import yaml

#读取yaml文件里的数据，须安装并引入yaml插件
def read_yaml(yaml_path):
     with open(yaml_path,encoding="utf-8",mode="r") as f:
         value = yaml.load(f,yaml.FullLoader)
         return value

#写入yaml数据,mode=会把原数据清空，a为追加数据
def write_yaml(yaml_path,data):
    with open(yaml_path,encoding="utf-8",mode="a") as f:
        data = {"name1":"马上教育","name2":"英雄联盟"}
        yaml.dump(data,stream=f,allow_unicode=True)

#清空yaml数据
def clear_yaml(yaml_path):
    with open(yaml_path,encoding="utf-8",mode="w") as f:
        f.truncate()


#程序入口
if __name__ == "__main__":
    data_value = read_yaml("../testcases/pruduct_manager/test.yaml")
    # write_yaml("../testcases/pruduct_manager/test.yaml", "data")
    # clear_yaml("../testcases/pruduct_manager/test.yaml")
    # print(str(date_value["data1"])+ "类型为：" +str(type(date_value["data1"])))
    # print("值为：" + str(data_value["data1"]) +"的类型为"+ str(type(data_value["data1"])))
    # print(data_value["data4"])
    # print(data_value["data7"])
    print(data_value)