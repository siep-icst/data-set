
prev_e_path="dblp_edges_prev.txt"

new_e_path="dblp_edges.txt"


v_set=set()
max_vid=0

prev_e_file=open(prev_e_path,'r')
while True:
    raw_e_line=prev_e_file.readline()
    tmp_e=raw_e_line.strip().split()
    tmp_len=len(tmp_e)
    if(tmp_len<1):
        break
    vid0=int(tmp_e[0])
    vid1=int(tmp_e[1])
    v_set.add(vid0)
    v_set.add(vid1)
    if vid0>max_vid:
        max_vid=vid0
    if vid1>max_vid:
        max_vid=vid1
prev_e_file.close()
v_num=len(v_set)
# print("max vid: "+str(max_vid))
print("v num: "+str(len(v_set)))

prev_vid_list=list(v_set)
prev_vid_list.sort()
new_vid_list=list(range(v_num))
prev_to_new_dict=dict()
for pos in range(v_num):
    prev_vid=prev_vid_list[pos]
    new_vid=new_vid_list[pos]
    prev_to_new_dict[prev_vid]=new_vid

prev_e_file=open(prev_e_path,'r')
new_e_file=open(new_e_path,"w")
while True:
    raw_e_line=prev_e_file.readline()
    tmp_e=raw_e_line.strip().split()
    tmp_len=len(tmp_e)
    if(tmp_len<1):
        break
    prev_vid0=int(tmp_e[0])
    prev_vid1=int(tmp_e[1])
    new_vid0=prev_to_new_dict[prev_vid0]
    new_vid1=prev_to_new_dict[prev_vid1]
    new_line_str=str(new_vid0)+" "+str(new_vid1)+"\n"
    new_e_file.write(new_line_str)
prev_e_file.close()
new_e_file.close()






prev_e_file.close()