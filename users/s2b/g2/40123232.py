result = []
with open("./../../../2016_cd_2a_2.txt", 'r') as f:
    content = f.readlines()
    #print(content)
    #print(len(content))
    # 逐 element 處理
    for i in range(len(content)):
        for line in content[i].splitlines():
            #print(content[i].splitlines())
            result.append(list(line.split(",")))
            
            g.es(result)
            