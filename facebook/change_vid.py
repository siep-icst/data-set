prev_edges_path="facebook_edges_prev.txt"
new_edges_path="facebook_edges.txt"

prev_edges_file=open(prev_edges_path,'r')
new_edges_file=open(new_edges_path,'w')

vid_set=set()
while True:
    raw_prev_e_line=prev_edges_file.readline()
    tmp_line=raw_prev_e_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    v_left=int(tmp_line[0])
    v_right=int(tmp_line[1])
    vid_set.add(v_left)
    vid_set.add(v_right)
# v_num=len(vid_set)
# max_id=-1
# for v in vid_set:
#     if(v>max_id):
#         max_id=v
# print("v_num: "+str(v_num))
# print("max id: "+str(max_id))
vid_list=[]
for v in vid_set:
    vid_list.append(v)
vid_list.sort()
v_num=len(vid_list)
v_old2new={}
for i in range(v_num):
    new_v=i
    old_v=vid_list[i]
    v_old2new[old_v]=new_v
prev_edges_file.close()
prev_edges_file=open(prev_edges_path,'r')
while True:
    raw_prev_e_line=prev_edges_file.readline()
    tmp_line=raw_prev_e_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    old_v_left=int(tmp_line[0])
    old_v_right=int(tmp_line[1])
    new_v_left=v_old2new[old_v_left]
    new_v_right=v_old2new[old_v_right]
    new_edges_file.write(str(new_v_left)+" "+str(new_v_right)+"\n")


prev_edges_file.close()
new_edges_file.close()
