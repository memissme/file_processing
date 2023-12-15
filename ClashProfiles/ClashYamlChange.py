# -------------------------------------------
# 版本号：0.1bate
# 创建日期：2023-06-08
# 作者：memissme
# 使用方法：
#   1. 需要有myRlues.yml作为基础文件；
#   2. 私人添加的网址在webside.csv
#   3. 输出文件为outRules.yml
#   4. 在clash中重新添加。
#
#--------------------------------------------

# import ruamel.yaml as yaml
import yaml,csv,os

# 先读取list信息，保存有效信息为字典
# inputPath = "list.yml"
# 读取节点更新文件
with open(inputPath, 'r',encoding='utf8') as dicData: 
    listConfig = yaml.safe_load(dicData)

listConfigInfo = {}
i = 1
for info in listConfig['files']:
    listConfigInfo[str(i)] = {"time":info['time'],"name":info['name']}
    print("现有以下节点：")
    print("序号：",i,"——>\t",info['name'])
    i += 1

user_input = 0
while(user_input==0):
    user_input = input('请输入序号：')
    if int(user_input) > 0 and int(user_input) <= len(listConfigInfo) + 1:
        user_choice = int(user_input)
        print("您选择的序号是：", user_choice , "节点文件是", listConfigInfo[user_input]['name'])
        newfile = listConfigInfo[user_input]['time']
    else :
        print('您输入的不是有效的序号！')

# 设置路径，读取yaml文件
inputPath = "profiles\\"
# 读取节点更新文件
with open(inputPath + newfile, 'r',encoding='utf8') as dicData: 
    newConfig = yaml.safe_load(dicData)
    # config = yaml.load(stream,Loader=yaml)

# 读取正在使用文件
newfile = "myRlues.yml"
with open(inputPath  + newfile, 'r',encoding='utf8') as dicData: 
    oldConfig = yaml.safe_load(dicData)

websideData = []
websideDataPath = "webside.csv"
with open(inputPath + websideDataPath, 'r') as f:
    reader = csv.reader(f)
    # 跳过首行（如果有）
    # next(reader)
    # 将数据保存到列表中
    for row in reader:
        rowString = "DOMAIN-SUFFIX," + row[0] + ",me 私人添加"
        websideData.append(rowString)

print(oldConfig['rules'])
websideData.append('GEOIP,CN,🇨🇳 国内网站')
websideData.append('MATCH,🐟 漏网之鱼')
oldConfig['rules'].extend(websideData)

# 读更新的取节点信息
proxiesList = newConfig['proxies']
# print(proxiesList)
# print(oldConfig['proxies'])
proxiesNameList = []
# 将节点名称保存到List
for i in proxiesList:
    proxiesNameList.append(i['name'])

currentProxies = proxiesNameList

# 更新节点信息
oldConfig['proxies'] = proxiesList

# 遍历数据并更改
for i in oldConfig['proxy-groups'][1:6]:
    i['proxies'] = currentProxies

outputPath = "outRules.yml"

# with open(outputPath, 'w',encoding='utf8') as dicData: 
#     yaml.dump(oldConfig,dicData,allow_unicode=True)

# folder_path = os.getcwd()
# print('输出文件保存在:',folder_path,"文件名为：",outputPath)
