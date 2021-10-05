# You are given three integers  and  representing the dimensions of a cuboid along with an integer . 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arr = []
    arr = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    # print(arr)
    filtered_arr = [el for el in arr if sum(el) != n]
    print(filtered_arr)