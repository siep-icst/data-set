data_name="nasa"
edges_path=data_name+"_edges.txt"
edges_file=open(edges_path,'r')

# # whether vid is constituent int
# v_set=set()
# max_vid=0

v2nei={}

while True:
    raw_edge_line=edges_file.readline()
    tmp_edge=raw_edge_line.strip().split()
    list_len=len(tmp_edge)
    if(list_len<1):
        break
    v_left=int(tmp_edge[0])
    v_right=int(tmp_edge[1])
    if(v_left in v2nei):
        v2nei[v_left].add(v_right)
    else:
        v2nei[v_left]=set()
        v2nei[v_left].add(v_right)
    if(v_right in v2nei):
        v2nei[v_right].add(v_left)
    else:
        v2nei[v_right]=set()
        v2nei[v_right].add(v_left)
edges_file.close()

max_deg=0
for vid in v2nei.keys():
    tmp_deg=len(v2nei[vid])
    if (tmp_deg>max_deg):
        max_deg=tmp_deg

print("max degree of "+data_name+" : "+str(max_deg))