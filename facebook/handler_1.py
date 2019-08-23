import random

# get graph info
# v_num e_num max_v_label
data_name="facebook"
prev_data_path=data_name+"_new.igraph"
new_data_path=data_name+"_info.igraph"
prev_data_file=open(prev_data_path,'r')
new_data_file=open(new_data_path,'w')

v_num=0
e_num=0
max_v_label=0

def write_info(_v_num,_e_num,_max_v_label):
    write_str=str(_v_num)+' '+str(_e_num)+' '+str(_max_v_label)+"\n"
    new_data_file.write(write_str)

first_line=True
while True:
    raw_tmp_line=prev_data_file.readline()
    tmp_line=raw_tmp_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    if(tmp_line[0]=='t'):
        if(first_line):
            first_line=False
        else:
            write_info(v_num,e_num,max_v_label)
            v_num=0
            e_num=0
            max_v_label=0
        if(tmp_line[2]=="-1"):
            break
    elif(tmp_line[0]=='v'):
        v_num+=1
        tmp_v_label=int(tmp_line[2])
        if tmp_v_label>max_v_label:
            max_v_label=tmp_v_label
    elif(tmp_line[0]=='e'):
        e_num+=1


prev_data_file.close()
new_data_file.close()