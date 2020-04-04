import send
data = open('gpu').read()
ds = data.split('\n')
g0 = int(ds[8].split('|')[2].split('/')[0][:-4]) 
g1 = int(ds[11].split('|')[2].split('/')[0][:-4]) 
g2 = int(ds[14].split('|')[2].split('/')[0][:-4]) 
g3 = int(ds[17].split('|')[2].split('/')[0][:-4]) 

print(g0,g1,g2,g3)
gs = [g0,g1,g2,g3]
g_str = str(g0)+' '+str(g1)+' '+str(g2)+' '+str(g3)
ga = [i<9000 for i in gs]
print(ga)
print(sum(ga))
if(sum(ga)):
    send.send(g_str)


