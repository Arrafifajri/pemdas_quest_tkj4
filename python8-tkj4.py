list_integer =[1,2,3,10,100,250]
list_string =["fajri",'hilal','lulu','dewi','nazla']
list_mix =[20,'hilal kamal', True,'bocah linux']

print("data string yang sebelum di rubah", list_string)
list_string[1] = "halal kamal"
list_string[2] = "lulu penuh"
print("data string yang setelah di rubah", list_string)

print("\ndata mix sebelum di rubah",list_mix)
list_mix[0] =100
list_mix[1] ="halal aja"
list_mix[2] =False
list_mix[3] ="anak ff"
print("setelah di rubah", list_mix)

# perulangan for

print('\nlist nama temen gw:')
print("\n")
for nama_temen in list_string:
    print(nama_temen)
print("\n")
for angka in list_integer:
    print(angka)
print("\n")
for reamix in list_mix:
    print(reamix)