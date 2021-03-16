import sys

f = open("LFA_lab.txt")

#ignoram liniile cu comentarii

Sigma = []
States = {}
Transitions = []
t = []

init = 0
nr_line = 0
error = 0

def check_letter(letter):
    for i in Sigma:
        if letter == Sigma[i]:
            return 1
    return 0

#def check_transition(letter, letter2):



for i in range(1,4):
    line = f.readline()
    nr_line += 1
    while line[:1] == "#":
        line = f.readline()
        nr_line += 1
    if line.strip() == "Sigma:":
        line = f.readline()
        nr_line += 1
        while line.strip() != "End" and line != "":
            Sigma.append(line.strip()) # Sigma este o lista de cuvinte
            line = f.readline()
            nr_line += 1
        print("Sigma", Sigma, sep=": ")
    else:
        if line.strip() == "States:":
            line = f.readline()
            nr_line += 1
            while line.strip() != "End" and line != "":
                # numaram cate stari initale avem
                if line.strip().find(", S") == len(line.strip()) - 3:
                    init = init + 1
                    S = {line[0:len(line.strip()) - 2].strip():'S'}
                else:
                    # numaram cate stari finale avem
                    if line.strip().find(", F") == len(line.strip()) - 3:
                        S = {line[0:len(line.strip()) - 2].strip(): 'F'}
                    else:
                        S = {line.strip(): 'N'} # N de la None - pentru cele care nu au sunt stare initiala, nici stare finala
                States.update(S) # States este un dictionar in care key reprezinta starea, iar value reprezinta tipul de stare('S' - initiala, 'F; - finala, 'N' - None)
                line = f.readline()
                nr_line += 1
            if init != 1:
                print("EROARE: Exista mai multe stari initiale.")
                error = 1
                break
            else:
                print("States", States, sep=": ")
        else:
            line = f.readline()
            nr_line += 1
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
                    print("EROARE: nu exista prima stare la linia: ", nr_line)
                    error = 1
                    break
                if OK2 == 0:
                    print("EROARE: nu exista a doua starela linia: ", nr_line)
                    error = 1
                    break
                OK = 0
                for s in Sigma:
                    if t[1] == s: # verificam daca t[1], cuvantul din mijloc, este in Sigma
                        OK = 1
                if OK == 0:
                    print("EROARE: nu exista cuvantul la linia: ", nr_line)
                    error = 1
                    break
                Transitions.append(t) # Transitions este  lista ,a carei elemente sunt liste
                line = f.readline()
                nr_line += 1
            print("Transitions", Transitions, sep=": ")

f.close()

if error == 0:
    word = input()
    for key in States:
        if States[key] == 'S':
            last_state = key
    for i in range(len(word) - 2):
        if check_letter(word[i]) == 1 and check_transition(word[i], word[i+1]) == 1:
            print("Este in DFA.")

    else:
        print("Nu este in DFA.")

