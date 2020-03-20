v_num=1034
vlabel_path="dblp_vlabel.txt"
edge_path="dblp_edges.txt"

standard_path="dblp_2.igraph"
standard_file=open(standard_path,"w")
vlabel_file=open(vlabel_path,"r")
vlabel_list=[]
vlabel_lines=vlabel_file.readlines()
vlabel_file.close()
for vlabel_line in vlabel_lines:
    vlabel_list.append(int(vlabel_line.split()[0]))
standard_file.write("t # 0\n")
standard_file.write("317080 1049866 19\n")
for v_id in range(v_num):
    tmp_line="v "+str(v_id)+" "+str(vlabel_list[v_id])+"\n"
    standard_file.write(tmp_line)

edge_file=open(edge_path,"r")
edge_lines=edge_file.readlines()
edge_file.close()
for edge_line in edge_lines:
    items=edge_line.split()
    v_left=int(items[0])
    v_right=int(items[1])
    tmp_line="e "+str(v_left)+" "+str(v_right)+"\n"
    standard_file.write(tmp_line)

standard_file.write("t # -1\n")

standard_file.close()