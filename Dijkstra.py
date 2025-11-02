startLat, startLon = 40.790622, 29.393939
endLat, endLon     = 40.769982, 29.426983

mapRadiusMeters = 4000      
skip = 5                     
dpi_preview = 150
dpi_video = 150               
fps = 20
wave_color = "#00e5e5"
wave_main_alpha = 0.9
path_color = "#00ffff"
node_color = "#009999"
bg_color = "#2B2A2A"
road_color = "#3a3a3a"
road_thickness = 0.4
preview_frame_index = 8     

out_preview = "gebzepreview.png"
out_video   = "gebzewave.mp4"

graph = ox.graph_from_point((startLat, startLon), dist=mapRadiusMeters, network_type='drive')
startNode = ox.distance.nearest_nodes(graph, startLon, startLat)
endNode   = ox.distance.nearest_nodes(graph, endLon, endLat)

visitedEdges = []
visitedNodes = set()
pq = [(0, startNode, None)]
while pq:
    cost, current, parent = heapq.heappop(pq)
    if current in visitedNodes:
        continue
    visitedNodes.add(current)
    if parent is not None:
        visitedEdges.append((parent, current))
    if current == endNode:
        break
    for neighbor, edata in graph[current].items():
        length = edata[0]['length'] if 0 in edata else edata['length']
        heapq.heappush(pq, (cost + length, neighbor, current))

shortestPath = nx.shortest_path(graph, startNode, endNode, weight='length')
pathEdges = list(zip(shortestPath[:-1], shortestPath[1:]))
