class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        queue.append(('0000', 0))
        deadends = set(deadends)
        visited = set('0000')

        while queue:
            #steps += 1
            cur_code , cur_step = queue.popleft()

            if cur_code in deadends:
                continue
            if cur_code == target:
                return cur_step

            for i in range(4):
                for move in [-1 , 1]:
                    new_code = cur_code[:i] + str((int(cur_code[i]) + move) % 10) + cur_code[i+1:]
                    
                    if new_code not in visited:
                        visited.add(new_code)
                        queue.append((new_code , cur_step+1))

        return -1     
               

    


        