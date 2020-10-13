# expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
# st_open = []
# st_close = []
#
# for i in range(len(expression)):
#     if expression[i] == "(":
#         st_open.append(i)
#     elif expression[i] == ")":
#         ch = st_open.pop()
#         print(expression[ch:i+1])
#


def get_sub_expressions(expression):
    st = []
    result = []
    for index in range(len(expression)):
        if expression[index] == "(":
            st.append(index)
        elif expression[index] == ")":
            start_ch = st.pop()
            result.append(expression[start_ch:index + 1])

    return result


#print(get_sub_expressions(input()))
[print(x) for x in get_sub_expressions(input())]


