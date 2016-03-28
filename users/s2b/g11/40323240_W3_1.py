result = []
with open("./../../../2b_files/task0/g11.txt", 'r') as f:
    content = f.readlines()
    for i in range(len(content)):
        for line in content[i].splitlines():
            result.append(list(line.split(",")))
group_sorted = []
for i in range(len(result)):
    group_list = sorted(list(filter(None, result[i])))
    group_sorted.append(group_list)
final_result = sorted(group_sorted)
g.es("分組結果:", final_result)
spring_2b =  final_result