inf_disk = 1.44*1024*1024
kniga_pag = 100
pag_strok = 50
strok_sym = 25
ves_koda = 4
number=int(inf_disk // (kniga_pag*pag_strok*strok_sym*ves_koda))


print ('Количество книг, помещающихся на дискету:',number)