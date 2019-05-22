import random

data_name="email_eu"
prev_data_path=data_name+"_new.igraph"
new_data_path=data_name+"_2.igraph"
info_data_path=data_name+"_info.igraph"
prev_data_file=open(prev_data_path,'r')
new_data_file=open(new_data_path,'w')
info_data_file=open(info_data_path,'r')
while True:
    raw_tmp_line=prev_data_file.readline()
    tmp_line=raw_tmp_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    if(tmp_line[0]=='t'):
        new_data_file.write(raw_tmp_line)
        # adjusted to query_gen, with no meaning, vertex count,edge count,vertex label range,
        # edge label range
        if(tmp_line[2]!="-1"):
            raw_info_line=info_data_file.readline()
            new_data_file.write(raw_info_line)
    elif(tmp_line[0]=='v'):
        
        new_data_file.write(raw_tmp_line)
    elif(tmp_line[0]=='e'):
        new_data_file.write('e'+' '+str(tmp_line[1])+' '+str(tmp_line[2])+'\n')


prev_data_file.close()
new_data_file.close()