"""
Author: Samantha Harper

Date: 01/31/2025

Summary: Proam will sort an array of 0s. 1s, and 2s in accedning order.
Class Solution is used with method sort012. 
Method - sort012 will take the input array and sort them in ascending order regardling of position. 

"""
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        pos_0 = 0
        pos_1 = 0
        pos_2 = 0

        for num in arr:
            if num == 0:
                pos_0 += 1
            elif num == 1:
                pos_1 += 1
            else:
                pos_2 += 1

        num_start = 0

        for i in range(pos_0):
            arr[num_start] = 0
            num_start += 1

        for i in range(pos_1):
            arr[num_start] = 1
            num_start += 1

        for i in range(pos_2):
            arr[num_start] = 2
            num_start += 1

def main():
    order = Solution()
    arr = [0, 1, 2, 0, 1, 2]
    order.sort012(arr)


    for x in arr:
        print(x, end= " ")

if __name__ == "__main__":
    main()
        

