# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:31:31 2023

@author: super
"""

import heapq

def prim(graph):
    # Selección de un vértice arbitrario como origen
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])
    # Inicialización del heap de aristas a considerar
    edges = [
        (weight, start_vertex, to)
        for to, weight in graph[start_vertex].items()
    ]
    heapq.heapify(edges)

    # Construcción del árbol de expansión mínima
    mst = []
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, weight_next in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (weight_next, to, to_next))

    return mst

# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}
mst = prim(graph)
print(mst)
