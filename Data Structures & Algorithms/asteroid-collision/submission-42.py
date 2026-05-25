class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        temp = []
        for i in asteroids:
            alive = True
            while alive and temp and i < 0 < temp[-1]:
                if abs(i) == temp[-1]:      # cùng size → cả hai nổ
                    temp.pop()
                    alive = False
                elif abs(i) < temp[-1]:     # i thua → i nổ
                    alive = False
                else:                       # i thắng → pop stack, tiếp tục
                    temp.pop()
            if alive:
                temp.append(i)
        return temp