import yaml
def yml_data_with_file(file_name):
    with open("./data/"+file_name+".yml", 'r',encoding='UTF-8') as f:
        return yaml.load(f)
#         print(type(data))  # 打印data类型
#         print(data)  # 打印data返回值
# if __name__ == '__main__':
#     yml_data_with_file()
def data_with_key(key):
    #return yml_data_with_file("login_data")[key]
    data = yml_data_with_file("login_data")[key]
    eles = data.values()
    data_list = list()
    for case_data in eles:
        data_list.append(case_data)
    return data_list
# def data(key):
#     da=yml_data_with_file("login_data")[key]
#     return da
# ele=data("test_login")
# print(ele)