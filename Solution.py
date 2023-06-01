class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price_sorted = sorted(price)
        l = len(price)
        
        mid = l / 2
        if mid % 2 == 0:
            mid = int(mid)
        else:  
            mid = int(mid) + 1
        print("mid: ", mid)

        left = 0
        right = l - 1

        # 从中间开始，每次取一个，直到取完
        while(left < right):
            mid = int((left + right) / 2)
            print("mid: ", mid)

            # mid为区间中点，k为区间长度，计算区间甜蜜度

            