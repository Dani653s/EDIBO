#!/usr/bin/python3.6

print("Ievadiet skaitli")
#a=2**2000000

#te ir trīs darbības - vertības sagaidīšana, vērtības pārveidošana, piešķiršana
#argument =  input()
#int(arguments)
#a - int(argument)

#pildot int(intput()) "bex izmēģinjuma", programma var vienkārši izlidot..
#tāpēc mēs izmantosim try ...except ... finally konstrukciju
paziime = False                #place mainigo
while not paziime:             #ja tas nebus paziime, tad tas bus True
#while paziime==False:         #tas pats, kas rakstīts augstāk
#while paziime!=True:          #-''-
    try:
        a=int( input() )
        paziime = True
    except:
        print("Diemžel, to, kas ievadīts, nevar pārveidot par vesela tipa skaitli")
        print("Lūdzu, ievadi s_k_a_t_l_i vēlreiz")
#if (a == int): print("a**100")
#var salīdzinat type(a) == int -> rezultāts būs True
if (a == 5):                   #ja pirms if iebazt #, tad  jebkāds cipars būs pakāpē
    print(a**100)
    print("Aprēķins ir gatavs")
print("Šis teksts atrodas ārpus darbību bloka - pierakstīts bez atstarpēm priekšā, tāpēc tas parādīsies jebkurā gadījumā")

#   print("Atstarpes šeit vairs nedrīkst būt")

...
#print ("Ievadāmai vērtībai jābūt skaitlim")
#b=a**100
