data_name="nasa"
info_path=data_name+"_info.igraph"
info_file=open(info_path,'r')

graph_num=0
tot_v_num=0
tot_e_num=0
max_vlabel=0
while True:
    raw_info_line=info_file.readline()
    tmp_info_list=raw_info_line.strip().split()
    tmp_line_len=len(tmp_info_list)
    if(tmp_line_len<1):
        break
    graph_num+=1
    tmp_v_num=int(tmp_info_list[0])
    tmp_e_num=int(tmp_info_list[1])
    tmp_max_vlabel=int(tmp_info_list[2])
    tot_v_num+=tmp_v_num
    tot_e_num+=tmp_e_num
    if(tmp_max_vlabel>max_vlabel):
        max_vlabel=tmp_max_vlabel

print("dataset: "+data_name)
print("graph_num: "+str(graph_num))
print("tot_v_num: "+str(tot_v_num))
print("tot_e_num: "+str(tot_e_num))
print("max_vlabel: "+str(max_vlabel))



info_file.close()
