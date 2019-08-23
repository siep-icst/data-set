import random

data_name="facebook"
# prev_v_path="email-Eu-core-department-labels.txt"
prev_e_path="facebook_edges.txt"
new_data_path=data_name+"_new.igraph"
# info_data_path=data_name+"_info.igraph"
# prev_v_file=open(prev_v_path,'r')
prev_e_file=open(prev_e_path,'r')
new_data_file=open(new_data_path,'w')
# info_data_file=open(info_data_path,'r')

# new_data_file.write("t # 0\n")
# new_data_file.write("0 0 0 0\n")

# find largest label

#add vertices
# while True:
#     raw_prev_v_line=prev_e_file.readline()
#     tmp_line=raw_prev_v_line.strip().split()
#     tmp_len=len(tmp_line)
#     if(tmp_len<1):
#         break
#     new_data_file.write("v "+tmp_line[0]+" "+tmp_line[1]+"\n")
vid_set=set()
while True:
    raw_prev_e_line=prev_e_file.readline()
    tmp_line=raw_prev_e_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    v_left=int(tmp_line[0])
    v_right=int(tmp_line[1])
    # new_data_file.write("e "+v_left+" "+v_right+"\n")
    vid_set.add(v_left)
    vid_set.add(v_right)
v_num=len(vid_set)
max_id=-1
for v in vid_set:
    if(v>max_id):
        max_id=v
print("v_num: "+str(v_num))
print("max id: "+str(max_id))

# new_data_file.write("t # -1\n")
# prev_v_file.close()
prev_e_file.close()
new_data_file.close()