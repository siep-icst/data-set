import matplotlib.pyplot as plt
dataset_name="human"
igraph_path="human_2.igraph"

degree_map={}
with open(igraph_path,'r') as edge_file:
    while True:
        tmp_line=edge_file.readline()
        if not tmp_line:
            break
        tmp_edge=tmp_line.strip().split()
        ch=str(tmp_line[0])
        if(ch!="e"):
            continue
        vertex0=int(tmp_edge[1])
        vertex1=int(tmp_edge[2])
        if vertex0 in degree_map:
            degree_map[vertex0]+=1
        else:
            degree_map[vertex0]=1
        if vertex1 in degree_map:
            degree_map[vertex1]+=1
        else:
            degree_map[vertex1]=1

# print(len(degree_map))
# for tmp_pair in degree_map.items():
#     print("vertex id: "+str(tmp_pair[0])+' '+"degree: "+str(tmp_pair[1]))

# vertex_cnt=len(degree_map)
# degree_list=list(degree_map.values())
# degree_list.sort(reverse=True)
# plt.plot(range(vertex_cnt),degree_list)
max_degree=0
degree2cnt={}
for vertex_id in degree_map:
    tmp_degree=degree_map[vertex_id]
    if(tmp_degree>max_degree):
        max_degree=tmp_degree
    if tmp_degree in degree2cnt:
        degree2cnt[tmp_degree]+=1
    else:
        degree2cnt[tmp_degree]=1

deg_list=list(degree2cnt.keys())
deg_list.sort(reverse=True)
cnt_list=[]
for tmp_deg in deg_list:
    cnt_list.append(degree2cnt[tmp_deg])
plt.plot(deg_list,cnt_list,'.')
plt.xlabel("degree")
plt.ylabel("count")
plt.title(dataset_name+" dataset")
plt.savefig("distribution_"+dataset_name+".png")
plt.show()
print("max degree: "+str(max_degree))




    