start = 1

matrix = {}
matrix[0,0] = 1
last = 1
target = 361527
height = 0
width = 0

# while int(last) < int(target):
#     # print(matrix[0,0])
#     # print(width)
#     # print(height)
#     if width > height:
#         height += 1
#     if width == height:
#         width += 1
#     for i in range(0,int(width)):
#         for j in range(0,int(height)):
#             if i > 1 and j > 1:
#                 matrix[i,j] = matrix[i-1,j] + matrix[i,j-1] + matrix[i-1,j-1]
#             elif i > 1:
#                 matrix[i,j] = matrix[i-1,j]
#                 print(matrix[i,j])
#             elif j > 1:
#                 matrix[i,j] = matrix[i,j-1]
#             # print(matrix)

def right (height,width):
    for i in range(0,int(width)):
        matrix[i,height] = matrix[i-1,height] + matrix[i,height-1] + matrix[i-1,height-1]
        print(matrix[i,height])
    height += 1
    up(height,width)
def up (height,width):
    for i in range(int(height),0,-1):
       matrix[width,i] =  matrix[width,i+1] + matrix[width-1,i] + matrix[width-1,i+1]
    width +=1    
    left(height,width)
def left (height,width):
    for i in range(int(width),0,-1):
        matrix[i,height] = matrix[i+1,height] + matrix[i,height+1], matrix[i+1,height+1]
    heigth += 1
    down(height,width)
def down (height,width):
    for i in range(0,int(height)):
        matrix[width,i] = matrix[width,i-1] + matrix[width+1,i] + matrix[width+1,i-1]
    width +=1
    right(height,width)

right(height,width)