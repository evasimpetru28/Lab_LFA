f = open("LFA_lab.txt")

#ignoram liniile cu comentarii

Sigma = []
States = {}
Transitions = []
t = []

init = 0
fin = 0


for i in range(1,4):
    line = f.readline()
    while line[0:1] == "#":
        line = f.readline()
    if line == "Sigma:":
        line = f.readline()
        while line != "End\n" or line != "":
            Sigma.append(line.strip()) # Sigma este o lista de cuvinte
            line = f.readline()
        print("Sigma", Sigma, sep=": ")
    else:
        if line == "States:":
            line = f.readline()
            while line != "End\n" or line != "":
                # numaram cate stari initale avem
                if line.find(", S") == len(line.strip()) - 3:
                    init = init + 1
                    S = {line[0:len(line) - 3].strip():'S'}
                else:
                    # numaram cate stari finale avem
                    if line.find(", F") == len(line.strip()) - 3:
                        fin = fin + 1
                        S = {line[0:len(line) - 3].strip(): 'F'}
                    else:
                        S = {line.strip(): 'N'} # N de la None - pentru cele care nu au sunt stare initiala, nici stare finala
                States.update(S) # States este un dictionar in care key reprezinta starea, iar value reprezinta tipul de stare('S' - initiala, 'F; - finala, 'N' - None)
                line = f.readline()
            if init != 1:
                print("EROARE: Exista mai multe stari initiale.")
            else:
                print("States", States, sep=": ")
        else:
            line = f.readline()
            while line != "":
                t = line.strip().split(", ")
                OK1 = 0
                OK2 = 0
                for key in States:
                    if t[0] == key: # verificam daca prima stare este in States
                        OK1 = 1
                    if t[2] == key: # verificam daca a doua stare este in States
                        OK2 = 1
                if OK1 == 0:
                    print("EROARE: nu exista prima stare.")
                if OK2 == 0:
                    print("EROARE: nu exista a doua stare.")
                OK = 0
                for s in Sigma:
                    if t[1] == s: # verificam daca t[1], cuvantul din mijloc, este in Sigma
                        OK = 1
                if OK == 0:
                    print("EROARE: nu exista cuvantul.")
                Transitions.append(t) # Transitions este  lista ,a carei elemente sunt liste
                line = f.readline()
            print("Transitions", Transitions, sep=": ")

f.close()

f = open("LFA_lab.txt")


# Nu merge :(

Sigma = []
States = {}
Transitions = []
t = []
init = 0
fin = 0


for i in range(1,4):
    line = f.readline()
    while line[0:1] == "#":
        line = f.readline()

    if line[0:6] == "Sigma:":
        line = f.readline()
        while line != "End\n" or line != "":
            Sigma.append(line.strip()) # Sigma este o lista de cuvinte
            line = f.readline()

    if line[0:8] == "States:":
        line = f.readline()
        while line != "End\n" or line != "":
            # numaram cate stari initale avem
            if line.find(", S") == len(line.strip()) - 3:
                init = init + 1
                S = {line[0:len(line) - 3].strip():'S'}
            else:
                # numaram cate stari finale avem
                if line.find(", F") == len(line.strip()) - 3:
                    fin = fin + 1
                    S = {line[0:len(line) - 3].strip(): 'F'}
                else:
                    S = {line.strip(): 'N'} # N de la None - pentru cele care nu au sunt stare initiala, nici stare finala
            States.update(S) # States este un dictionar in care key reprezinta starea, iar value reprezinta tipul de stare('S' - initiala, 'F; - finala, 'N' - None)
            line = f.readline()

        if init != 1:
            print("EROARE: Exista mai multe stari initiale.")
        else:
            print("States", States, sep=": ")

    if line[0:12] == "Transitions:":
        line = f.readline()
        while line != "":
            t = line.strip().split(", ")
            OK1 = 0
            OK2 = 0
            for key in States:
                if t[0] == key: # verificam daca prima stare este in States
                    OK1 = 1
                if t[2] == key: # verificam daca a doua stare este in States
                    OK2 = 1
            if OK1 == 0:
                print("EROARE: nu exista prima stare.")
            if OK2 == 0:
                print("EROARE: nu exista a doua stare.")
            OK = 0
            for s in Sigma:
                if t[1] == s: # verificam daca t[1], cuvantul din mijloc, este in Sigma
                    OK = 1
            if OK == 0:
                print("EROARE: nu exista cuvantul.")
            Transitions.append(t) # Transitions este  lista ,a carei elemente sunt liste
            line = f.readline()

f.close()

