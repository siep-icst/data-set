v_num=1005

prev_v_path="email-Eu-core-department-labels.txt"
prev_e_path="email-Eu-core.txt"
prev_v_file=open(prev_v_path,'r')
prev_e_file=open(prev_e_path,'r')
data_name="email_eu"
new_data_path=data_name+"_new.igraph"
new_data_file=open(new_data_path,'w')

# v2nei_list=[]

# for i in range(v_num):
#     tmp_neighbors=set()
#     v2nei_list.append(tmp_neighbors)

# # construct neighbor sets of all vertices
# while True:
#     raw_tmp_line=e_file.readline()
#     tmp_line=raw_tmp_line.strip().split()
#     tmp_len=len(tmp_line)
#     if(tmp_len<1):
#         break
#     vid0=int(tmp_line[0])
#     vid1=int(tmp_line[1])
#     v2nei_list[vid0].add(vid1)
#     v2nei_list[vid1].add(vid0)

# e_file.close()

# roots of graphs
root_list=[]
v2root_list=[]
edges=[]

# each graph has only one node
for i in range(v_num):
    v2root_list.append(i)

def find_root(_vid):
    if (v2root_list[_vid]==_vid):
        return _vid
    else:
        v2root_list[_vid]=find_root(v2root_list[_vid])
    return v2root_list[_vid]

while True:
    raw_e_line=prev_e_file.readline()
    tmp_e=raw_e_line.strip().split()
    tmp_len=len(tmp_e)
    if(tmp_len<1):
        break
    vid0=int(tmp_e[0])
    vid1=int(tmp_e[1])
    tmp_edge=[]
    tmp_edge.append(vid0)
    tmp_edge.append(vid1)
    edges.append(tmp_edge)

    root0=find_root(vid0)
    root1=find_root(vid1)
    if(root0==root1):
        pass
    elif(root0<root1):
        v2root_list[root1]=root0
        # v2root_list[vid1]=root0
    else:
        v2root_list[root0]=root1
        # v2root_list[vid0]=root1
prev_e_file.close()

graph_cnt=0
for i in range(v_num):
    if(v2root_list[i]==i):
        graph_cnt+=1


for vid in range(v_num):
    v2root_list[vid]=find_root(v2root_list[vid])

print("graph cnt: "+str(graph_cnt))

# root to nodes
tree_dict={}
for vid in range(v_num):
    v_root=v2root_list[vid]
    if(v_root in tree_dict):
        tree_dict[v_root].append(vid)
    else:
        tree_dict[v_root]=[vid]

print(tree_dict)

# read labels of vertex
v2label_list=[]
for i in range(v_num):
    v2label_list.append(-1)
while True:
    raw_v_line=prev_v_file.readline()
    tmp_v_line=raw_v_line.strip().split()
    line_len=len(tmp_v_line)
    if(line_len<1):
        break
    tmp_v=int(tmp_v_line[0])
    tmp_label=int(tmp_v_line[1])
    v2label_list[tmp_v]=tmp_label
prev_v_file.close()

graph_id=0
for x in tree_dict.keys():
    new_data_file.write("t # "+str(graph_id)+"\n")
    new_data_file.write("0 0 0 0\n")
    # vertices in this tree
    graph_v_list=tree_dict[x]
    for vid in graph_v_list:
        vlabel=v2label_list[vid]
        new_data_file.write("v "+str(vid)+" "+str(vlabel)+"\n")
    for edge in edges:
        left_v=edge[0]
        right_v=edge[1]
        if left_v in graph_v_list:
            # this edge is in this graph
            new_data_file.write("e "+str(left_v)+" "+str(right_v)+"\n")

    graph_id+=1
new_data_file.write("t # -1\n")
new_data_file.close()
    


