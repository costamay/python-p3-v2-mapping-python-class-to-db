# stack =>LIFO/FILO

# push
# pop
# empty/full
# peek
# search(target)
# size

# def reverse_string(string):
#     stack = []
#     for char in string:
#         stack.append(char)
        
#     reversed = ""
#     while stack:
#         reversed += stack.pop()
#     print(reversed)
# reverse_string("world")
# # dlrow

# abcd<<<fgh<i =>afgi

# a<cd<fg => cfg

def back_space(string):
    stack = []
    
    for char in string:
        if char == "<":
            if len(stack) != 0:
                stack.pop()
            
        else:
            stack.append(char)
    
    result = ""
    while stack:
        result = stack.pop() + result
        
    print(result)
back_space("abcd<<<fgh<i")

# a, b, c, d, f, g, h, i
# a, b, c, d
# a, b, c
# a, b
# a, f, g, h
# a, f, g, i
