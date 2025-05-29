# Problem link = 

def pascalTriangle(numRows):
    if numRows == 1:
        return[[1]]
    else:
        result = []
        result.append([1])
        for i in range(1, numRows):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(result[i - 1][j - 1] + result[i - 1][j])
            temp.append(1)
            result.append(temp)
        return result
    
numRows = 5
print(pascalTriangle(numRows))