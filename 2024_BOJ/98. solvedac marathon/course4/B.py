import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == "": break
    dance = list(map(str,line.split()))
    N = len(dance)
    error = set()

    twirl,hop,dip = False,False,False
    #E1
    for i in range(N):
        if dance[i] == "twirl": twirl = True
        elif dance[i] == "hop": hop = True
        elif dance[i] == "dip":
            dip = True
            if not((i > 0 and dance[i-1] == "jiggle") or (i > 1 and dance[i-2] == "jiggle") or (i < N-1 and dance[i+1] == "twirl")):
                error.add(1)
                dance[i] = "DIP"

    #E2
    if not(N > 2 and dance[-3:] == ["clap","stomp","clap"]): error.add(2)

    #E3
    if twirl and not hop: error.add(3)

    #E4
    if dance[0] == "jiggle": error.add(4)

    #E5
    if not dip: error.add(5)

    error = list(error)
    if error:
        if len(error) > 1:
            print("form errors {} and {}: {}".format(", ".join(map(str,error[:-1])),error[-1]," ".join(dance)))
        else:
            print("form error {}: {}".format(error[0]," ".join(dance)))
    else:
        print("form ok: {}".format(" ".join(dance)))