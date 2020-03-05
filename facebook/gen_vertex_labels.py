import random
import math

# gen label by power law distribution

def get_val_by_prob(_val_list,_cum_prob_list):
    x=random.uniform(0,1)
    n=len(_val_list)
    for i in range(n):
        if(x<_cum_prob_list[i]):
            return _val_list[i]

def prob_density_func(_x,_alpha=1):
    return math.pow(_x,-_alpha-1)

v_num=1034
label_num=10
vlabel_path="facebook_vlabel.txt"
vlabel_file=open(vlabel_path,"w")

cum_prob_list_prev=[]
prob_cum=0
label_val_list=list(range(label_num))
for label_id in range(label_num):
    prob_dens=prob_density_func(label_id+1)
    prob_cum+=prob_dens
    cum_prob_list_prev.append(prob_cum)
print("cum_prob_list_prev:")
print(cum_prob_list_prev)
prob_sum=prob_cum
cum_prob_list=[]
for cum_prob_prev in cum_prob_list_prev:
    cum_prob=float(cum_prob_prev)/prob_sum
    cum_prob_list.append(cum_prob)
cum_prob_list[label_num-1]=1

print(cum_prob_list)

for vid in range(v_num):
    label=get_val_by_prob(label_val_list,cum_prob_list)
    vlabel_file.write(str(label)+"\n")


vlabel_file.close()

