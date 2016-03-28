result = []
with open("./../../../2b_files/task0/2016_cd_2b_3.txt", 'r') as f:
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

# 第 i 組學號數列 為 spring_2a[i-1], i 從 1 到 11 共有 11 組
# 若要先照排依組序排座位, 且空字串由下一組可用學號補上
# 以排為先, 然後列, 共有 9 排 8 列可以排座位

seat_by_column = []
for row in range(7):
    for column in range(11):
        # 因為各分組數列的長度並不相同, 但是最長的有 8 位組員, 因此若無法取得的資料 (因為索引超值), 就補上空字串
        try:
            seat_by_column.append(spring_2b[column][row])
        except:
            seat_by_column.append("")

g.es("去除空白字串前的座位數列:", seat_by_column)

# 然後利用 filter(None, seat_by_column) 去除空白字串, 就可以得到以 column 為主的座位排序

seat_by_column = list(filter(None, seat_by_column))
# 以排為主的座位數列
#g.es("以排為主的座位數列:", seat_by_column)

# 然後每 8 個取為 1 排, 即可得到以排為主的座位序列

N = 8
column_list = [seat_by_column[n:n+N] for n in range(0, len(seat_by_column), N)]
# 列出每 8 個組員一排的數列
#g.es("每 8 個組員一排的數列:", column_list)
# 根據 column_list, 建立一個 dictionary, 其中學號為 index, 座位號為對應值
seat_dict = {}
for column in range(len(column_list)):
    for i in range(8):
        try:
            seat_dict.update({column_list[column][i]: (column, i)})
        except:
            seat_dict.update({"": ""})
# 根據學號, 排序 dictionary 的方法
import operator
seat_dict_sort = sorted(seat_dict.items(), key = operator.itemgetter(0), reverse = False)

# 依照學號順序, 列出座位表
for i in range(len(seat_dict_sort)):
    g.es(seat_dict_sort[i])

# dont know why .reverse() did not work, 只有 [::-1] 可以 reverse list elements
#g.es(column_list[::-1])

# 因為經由 zip 逐一重新 transpose 的列資料, 必須配合最大 (也就是總共有 7 列) 列數補上空白字串 (也就是空位)
# 所以不能使用 zip, 而必須導入 zip_longest 模組方法

from itertools import zip_longest

# zip list of lists, 特別注意下列 column_list 前方的 *

'''
The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple: 

https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
'''

spring_2b_final_seat = list(zip_longest(*column_list[::-1], fillvalue=""))
# 列出最後的座位
#g.es(spring_2b_final_seat)

# 最後轉成 html table 標註格式

g.es("<table>")
for row in range(len(spring_2b_final_seat)):
    g.es("<tr>")
    # 因為每一 row 有 9 個位子
    for i in range(9):
        g.es("<td>", spring_2b_final_seat[row][i], "</td>")
    g.es("</tr>")
g.es("</table>")


