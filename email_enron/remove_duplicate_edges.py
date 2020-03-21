
edge_duplicate_path="email_enron_edges_duplicate.txt"
edge_new_path="email_enron_edges.txt"

edge_duplicate_file=open(edge_duplicate_path,"r")
edge_new_file=open(edge_new_path,"w")

while True:
    raw_e_line=edge_duplicate_file.readline()
    tmp_e=raw_e_line.strip().split()
    tmp_len=len(tmp_e)
    if(tmp_len<1):
        break
    prev_vid0=int(tmp_e[0])
    prev_vid1=int(tmp_e[1])
    if (prev_vid0>prev_vid1):
        continue
    edge_new_file.write(raw_e_line)

edge_duplicate_file.close()
edge_new_file.close()