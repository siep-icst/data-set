
v_num=1005

visited=[]
for i in range(v_num):
    visited.append(0)

def dfs_walk(i):
    if visited[i]:
        return
    visited[i]=1
    for nei in v2nei_list[i]:
        dfs_walk(nei)

e_path="email-Eu-core.txt"
e_file=open(e_path,'r')

v2nei_list=[]

for i in range(v_num):
    tmp_neighbors=set()
    v2nei_list.append(tmp_neighbors)

# construct neighbor sets of all vertices
while True:
    raw_tmp_line=e_file.readline()
    tmp_line=raw_tmp_line.strip().split()
    tmp_len=len(tmp_line)
    if(tmp_len<1):
        break
    vid0=int(tmp_line[0])
    vid1=int(tmp_line[1])
    v2nei_list[vid0].add(vid1)
    v2nei_list[vid1].add(vid0)

e_file.close()

dfs_walk(0)

connected=True
for i in range(v_num):
    if(visited[i]==0):
        connected=False

print("connected graph: "+str(connected))


