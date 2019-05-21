import random

data_name="human"
prev_data_path=data_name+".igraph"
new_data_path=data_name+"_new.igraph"
prev_data_file=open(prev_data_path,'r')
new_data_file=open(new_data_path,'w')
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
            new_data_file.write("0 0 0 0\n")
    elif(tmp_line[0]=='v'):
        label_cnt=len(tmp_line)-2
        selected_label_id=random.randrange(label_cnt)+2
        selected_label_id=int(selected_label_id)
        selected_label=tmp_line[selected_label_id]
        new_data_file.write("v "+str(tmp_line[1])+" "+str(selected_label)+"\n")
    elif(tmp_line[0]=='e'):
        new_data_file.write('e'+' '+str(tmp_line[1])+' '+str(tmp_line[2])+' '+'0'+'\n')


prev_data_file.close()
new_data_file.close()