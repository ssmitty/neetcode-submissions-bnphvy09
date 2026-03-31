class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        newarray=list(zip(position,speed))
        newarray.sort(reverse=True)
        time1=(target- newarray[0][0])/newarray[0][1]
        stack=[time1]
        print(f"inital time {time1}")
        for i in range(1,len(newarray)):
            print("here")
            time=(target-newarray[i][0])/newarray[i][1]
            print(time)
            if time> stack[-1]:
                
                print(newarray[i])
                stack.append(time)
        return len(stack)
