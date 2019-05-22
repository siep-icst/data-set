import random

data_name="email_eu"
prev_v_path="email-Eu-core-department-labels.txt"
prev_e_path="email-Eu-core.txt"
new_data_path=data_name+"_new.igraph"
# info_data_path=data_name+"_info.igraph"
prev_v_file=open(prev_v_path,'r')
prev_e_file=open(prev_e_path,'r')
new_data_file=open(new_data_path,'w')
# info_data_file=open(info_data_path,'r')

new_data_file.write("t # 0\n")
new_data_file.write("0 0 0 0\n")

#add vertices
while True:
    raw_prev_v_line=prev_v_file.readline()
    tmp_line=raw_prev_v_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    new_data_file.write("v "+tmp_line[0]+" "+tmp_line[1]+"\n")

while True:
    raw_prev_e_line=prev_e_file.readline()
    tmp_line=raw_prev_e_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    new_data_file.write("e "+tmp_line[0]+" "+tmp_line[1]+"\n")

new_data_file.write("t # -1\n")
prev_v_file.close()
prev_e_file.close()
new_data_file.close()