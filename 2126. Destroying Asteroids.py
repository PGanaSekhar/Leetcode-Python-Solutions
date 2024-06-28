class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        i=0
        b=0
        while i<len(asteroids):
            if asteroids[i]<=mass:
                mass+=asteroids[i]
                asteroids.pop(i)
            else:
                i+=1
        return mass>=sum(asteroids)
