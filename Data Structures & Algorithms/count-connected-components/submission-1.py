class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adjaceny list
        # use dfs to iterate thru graph
        # increment counter for every new dfs from node

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Sort each adjacency list
        for neighbors in adj:
            neighbors.sort()
        
        visited = set()
        count = 0 

        # do dfs and iterate thru nodes 

        # 0 1 2 3 4 5 
        # 0 : 1 
        # 1 : 0, 2
        # 2 : 1, 3
        # 3 : 2
        # 4 : 5
        # 5 : 4 

        
        def dfs(node): 
            for neighbor in adj[node]: # what does this mean ? what is neighbor is it like all the values stored in the key in hashmap
                if neighbor not in visited: # yeah if we havent traversed the neighbor
                    visited.add(neighbor) # mark as visited
                    # 1 is visited 
                    # 2 is visited 
                    # 3 is visited 

                    # new cycle 
                    # exit 

                    # 4 is visited 
                    # 5 is visited 
                    dfs(neighbor) # ok now u can try and look for the paths in this node
        
        # fuction to use dfs ? 
        for node in range(n):
            if node not in visited:
                # jump to 4 
                visited.add(node) # mark as visited ok  # add 0
                dfs(node) # why call this --> to jump start the process ? but it keeps iterating in dfs too or maybe for when it ends ? 
                # first component 0 1 2 3
                # second component 4 5
                count += 1 

            # currently confused about how these are used bruh like u just pass 1 back into the dfs and make it start all over again from there instead of restarting 
        
        return count


                
            




        

