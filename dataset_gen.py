
data_name="aids"
prev_data_path=data_name+".igraph"
new_data_path=data_name+"_new.igraph"
prev_data=open(prev_data_path,'r')
while True:
    tmp_line=prev_data.readline().strip()
    

prev_data.close()