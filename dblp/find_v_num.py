
prev_e_path="dblp_edges.txt"
prev_e_file=open(prev_e_path,'r')

v_set=set()
max_vid=0

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

print("max vid: "+str(max_vid))
print("v num: "+str(len(v_set)))



prev_e_file.close()