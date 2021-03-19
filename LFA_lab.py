import sys

f = open(sys.argv[1])

# ignoram liniile cu comentarii

Sigma = []
States = {}
Transitions = []
t = []

init = 0
nr_line = 0
error = 0


def check_transition(letter, state):
    for i in range(len(Transitions)):
        if Transitions[i][0] == state and Transitions[i][1] == letter:
            return Transitions[i][2]
    return "Nu exista tranzitie"


for i in range(1, 4):
    line = f.readline()
    nr_line += 1
    while line[:1] == "#":
        line = f.readline()
        nr_line += 1
    if line.strip() == "Sigma:":
        line = f.readline()
        nr_line += 1
        while line.strip() != "End" and line != "":
            Sigma.append(line.strip())  # Sigma este o lista de cuvinte
            line = f.readline()
            nr_line += 1
        print("Sigma", Sigma, sep=": ")
    else:
        if line.strip() == "States:":
            line = f.readline()
            nr_line += 1
            while line.strip() != "End" and line != "":
                if line.strip().find(", S") == len(line.strip()) - 3:
                    init = init + 1  # numaram cate stari initale avem
                    S = {line[0:len(line.strip()) - 2].strip(): 'S'}
                else:
                    if line.strip().find(", F") == len(line.strip())-3 and line.strip().find(", S, F") != len(line.strip())-6:
                        S = {line[0:len(line.strip()) - 2].strip(): 'F'}
                    else:
                        if line.strip().find(", S, F") == len(line.strip()) - 6:
                            S = {line[0:len(line.strip()) - 5].strip(): "S, F"}  # schimbare: -5 -> -2 ??
                            init = init + 1  # numaram cate stari initale avem
                        else:
                            S = {line.strip(): 'N'}  # N: None - nu au stare initiala/ finala
                States.update(S)  # States: dictionar | key: starea, value: tipul stare(S - init, F - fina, N - None)
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
            while line != "" and line.strip() != "End":
                t = line.strip().split(", ")
                OK1 = 0
                OK2 = 0
                for key in States:
                    if t[0] == key:  # verificam daca prima stare este in States
                        OK1 = 1
                    if t[2] == key:  # verificam daca a doua stare este in States
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
                    if t[1] == s:  # verificam daca t[1], cuvantul din mijloc, este in Sigma
                        OK = 1
                if OK == 0:
                    print("EROARE: nu exista cuvantul la linia: ", nr_line)
                    error = 1
                    break
                Transitions.append(t)  # Transitions este  lista ,a carei elemente sunt liste
                line = f.readline()
                nr_line += 1
            print("Transitions", Transitions, sep=": ")

f.close()

if error == 0:
    word = sys.argv[2]
    last_state = ''
    double_state = ''
    for key in States:
        if States[key] == 'S':
            last_state = key
        else:
            if States[key] == 'S, F':
                double_state = key
                last_state = double_state
    if double_state != '' and word == '':
        print("Cuvantul vid este acceptat.")
        last_state = double_state
    else:
        i = 0
        while i <= len(word)-1:
            last_state = check_transition(word[i], last_state)
            if last_state == "Nu exista tranzitie":
                i = len(word)
            i += 1
        OK = 0
        for key in States:
            if key == last_state and States[key] == 'F':
                print("Cuvantul este acceptat.")
                OK = 1
        if OK == 0:
            print("Cuvantul nu este acceptat.")
else:
    print("Limbajul dat nu poate genera un DFA.")
