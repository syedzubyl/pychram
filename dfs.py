# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:53:02 2023

@author: Vimala Priya
"""
def recursdfs(graph, s,path = []):  
    
       if s not in path:  
           path.append(s) 
           if s not in graph:  
               return path
           for neighbour in graph[s]:  
               path = recursdfs(graph, neighbour, path)
       return path 
   
graph = {"A":["B","C","D"],  
   "B":["E"],  
   "C":["G","F"],  
   "D":["H"],  
   "E":["I"],  
   "F":["J"],  
   "G":["K"]}  
dfs = recursdfs(graph, "A")  
print("\n")
print("Depth First Search Traversal")
print("----------------------------")
print(dfs)




