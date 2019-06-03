#%%
import numpy as np

output = np.load('output.npz')

#print(output['z'])



print("\n",output['z'][15], "-> 15")
print(output['z'][22], "-> 22")
#print(output['z'][25], "-> 25")
print(output['z'][28], "-> 28")
#print(output['z'][32], "-> 32")
print(output['z'][32], "-> 32")
print(output['z'][35], "-> 35")


nz = 60
u0   = float(1)*np.ones(nz)
u00 = 12
u00_sh = 20
#for i in range (0, nz):
#    u0[i] = 10
#print(u0)

float(12)*np.ones(nz)

n_5 = 15
n_7 = 22
n_8 = 28
n_10 = 32
n_11 = 36

nk_shl = n_5
nk_sht = n_7 

u0_temp1 = float(u00)*np.ones(nk_shl)
u0_temp2 =np.linspace(u00, u00_sh, nk_sht - nk_shl)
u0_temp3 = np.concatenate((u0_temp1, u0_temp2), axis=None)
u0_temp4 = float(u00_sh)*np.ones(nz-nk_sht)
u0_temp5 = np.concatenate((u0_temp3, u0_temp4), axis=None)

print("u0_temp5 = ", u0_temp5 )

u0_temp5 = np.linspace(0,1,3)

print("u0_temp5 = ", u0_temp5 )

i = np.zeros((3,5))
print(len(i))
print(i)
#print(type(u0_temp1), type(u0_temp2))
#print(u0_temp5)

#print(len(u0_temp5))
#%%

#%%
