# -------------------------------------------
# 版本号：0.1bate
# 创建日期：2023-11-15
# 作者：memissme
# 使用方法：
#   1. 更新webProxy.csv和webDirect.csv文件
#   2. 生成新的pac.txt文件
#   3. 注意，如果读取的myPAC.js文件中
#       'DIRECT': {
#        // 'example1.com': true,
#        // Add more direct access rules here...
#       },
#       如果原本有Domains，注意最后一个“,”
#--------------------------------------------



import re
import csv

# 定义文件路径
pathway = "V2RayN_PAC\\"
proxy_file_path = pathway + 'webProxy.csv'
direct_file_path = pathway + 'webDirect.csv'
js_file_path = pathway + 'myPAC.js'

# 读取CSV文件并获取所有域名
with open(direct_file_path, newline='') as directCsvfile:
    reader = csv.reader(directCsvfile)
    directDomains = [row[0] for row in reader if row]


with open(proxy_file_path, newline='') as proxyCsvfile:
    reader = csv.reader(proxyCsvfile)
    proxyDomains = [row[0] for row in reader if row]

# 读取JavaScript文件内容
with open(js_file_path, 'r') as jsfile:
    js_content = jsfile.read()

# 查找'DIRECT'部分并添加新域名
patternDirect = r"('DIRECT': \{)([^}]*)(    \})"
matchDirect = re.search(patternDirect, js_content)
# print(matchDirect.group(3))

if matchDirect:
    direct_part = matchDirect.group(2) + ',\n'.join(["        '{}': true".format(domain) for domain in directDomains])
    new_direct_part = matchDirect.group(1) + direct_part + '\n' + matchDirect.group(3)
    new_js_content = js_content[:matchDirect.start()] + new_direct_part + js_content[matchDirect.end():]
    js_content = new_js_content
# print(js_content)
# print("#########************##########")


patternProxy = r"('PROXY': \{)([^}]*)(    \})"
matchProxy = re.search(patternProxy, js_content)
if matchProxy:
    proxy_part = matchProxy.group(2) + ',\n'.join(["        '{}': true".format(domain) for domain in proxyDomains])
    new_proxy_part = matchProxy.group(1) + proxy_part + '\n' + matchProxy.group(3)
    new_js_content = js_content[:matchProxy.start()] + new_proxy_part + js_content[matchProxy.end():]
    # print(new_js_content)

    # 将修改后的内容写回JavaScript文件
    with open(pathway + 'PAC.txt', 'w') as jsfile:
        jsfile.write(new_js_content)

# print("Domains have been added to the 'DIRECT' section of 'my.js'.")