class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = 0
        k = len(height) - 1
        l = len(height) - 1
        volume = 0
        while i<len(height)-1:
            if height[i] == 0:
                i+=1
                continue

            j=i+1
            intermed_tot = 0
            

            while height[j]<height[i]:
                j+=1
                if j == len(height):
                    j-=1
                    break
                intermed_tot+=height[j-1]
                

            if height[j]>=height[i]:
                volume += height[i]*(j-i-1)-intermed_tot
                

          
            i=j
        
        while k >0:

            if height[k] == 0:
                k-=1
                continue

            l=k-1
            intermed_tot = 0

            while height[l]<=height[k]:
                if l == -1:
                    l+=1
                    break
                intermed_tot+=height[l]
                l-=1
            
            if height[l]>height[k]:
                volume += height[k]*(k-l-1)-intermed_tot
            k=l
            
        return volume

