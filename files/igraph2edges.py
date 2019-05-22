data_name="nasa"
igraph_path=data_name+"_new.igraph"
igraph_file=open(igraph_path,'r')
edge_path=data_name+"_edges.txt"
edge_file=open(edge_path,'w')


while True:
    raw_igraph_line=igraph_file.readline()
    tmp_line=raw_igraph_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    if(tmp_line[0]=='e'):
        v_left=int(tmp_line[1])
        v_right=int(tmp_line[2])
        edge_file.write(str(v_left)+" "+str(v_right)+"\n")


igraph_file.close()
edge_file.close()
