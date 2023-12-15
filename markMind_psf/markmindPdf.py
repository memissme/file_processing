"""
 __version__       --- beta 0.1.0
 author            --- memissme
 data              --- 2023.08.09
 function          --- 帮助Obsidian中markMind插件新建PDF关联文件，
                       如果文件不存在则新建一个“源文件名.md”，
                       文件内容如下（例）：
                       annotate-target: references/1998discovery-and-development-of-somatostatin-agonists.pdf
                       annotate-type: pdf
notice             --- 默认PDF文件放在在obsidian本地库根目录下的 references文件夹中，如另有需求可以自行更改
                       在目标文件夹中运行终端，
                       用py命令运行脚本，脚本本文件需放在与PDF同目录下运行
"""


import os

# print(os.getcwd()) # 获取当前工作目录路径
print(os.path.abspath('.')) # 获取当前工作目录路径
folder_path = os.getcwd()  # 获取当前工作目录路径
pdf_files = []

for file in os.listdir(folder_path):
    if file.endswith('.pdf'):
        pdf_files.append(file)

nl = "\n"
folderPathList = folder_path.split('\\')
offset = 0
for i in folderPathList:
    if i == 'references':
        offset = 1
    if offset:
        filePath = i + '/'
print('新增的文件名如下：\n')
for i in pdf_files:
    file_name = i.replace(".pdf", ".md")
    if not os.path.exists(file_name):   #如果文件已存在则跳过
        content = "---" + nl + nl + "annotate-target: " +filePath+ i + nl + "annotate-type: pdf" + nl + "---" + nl
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
            print(file_name,'\n')