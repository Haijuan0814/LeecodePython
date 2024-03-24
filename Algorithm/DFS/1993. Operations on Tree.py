class LockingTree:

    def __init__(self, parent: List[int]):
        # intial the locked  list and lockedUser list
        self.locked = defaultdict(list)
        self.parent = parent
        # intial the graph : node with its direct subs
        g = defaultdict(list)
        for i in range(len(parent)):
            node = parent[i]
            if node != -1:
                g[node].append(i)
        self.graph = g
        
    # Locks the given node for the given user and prevents other users from locking the same node
    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = user
            return True
        return False
        
    # Unlocks the given node for the given user
    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        del self.locked[num]
        return True
        

    # The node is unlocked,
    # It has at least one locked descendant (by any user), and
    # It does not have any locked ancestors.

    def upgrade(self, num: int, user: int) -> bool:

        def check_ancestors(num):
            if num == -1:
                return False
            elif num in self.locked:
                return True
            else:
                return check_ancestors(self.parent[num])

        def check_descendants(num , user):
            for node in self.graph[num]:
                if node in self.locked:
                    return True
                if check_descendants(node , user):
                    return True
            return False

        def unlock_descendants(num):
            for node in self.graph[num]:
                if node in self.locked:
                    del self.locked[node]
                unlock_descendants(node)

        if num in self.locked:
            return False
        # 有祖先被锁了
        elif check_ancestors(self.parent[num]):
            if num == 0:
                print(11) 

            return False
        # 没有子孙被该用户锁    
        elif not check_descendants(num , user):
            return False
        
        # unlock the descendants
        unlock_descendants(num)
        # lock the current node
        self.locked[num] = user
        return True
        
    




# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)