import sys
import random

def sample_RHS_vertex(Vvertex, t):
    r = random.uniform(0, 1)    
    cur=0
    for key in Vvertex:
        if cur+Vvertex[key]["arrivals"][t] >= r:
            return key
        cur+=Vvertex[key]["arrivals"][t]
    return -1

if __name__ =="__main__":

    xefile=sys.argv[1]
    Bkfile=sys.argv[2]
    pjtfile=sys.argv[3]
    aefile=sys.argv[4]
    deadlinesfile=sys.argv[5]

    ROOT="../../small_dataset/"
    CSV=".csv"
   
    T=300


    lhsf=open(ROOT + "LHSvertices" + CSV, "r")
    deadlinef=open(ROOT + deadlinesfile + CSV, "r")

    deadlines=dict()
    for line in deadlinef:
        vals=line.split(",")
        deadlines[vals[0]] = int(float(vals[1].split("\n")[0]))
    deadlinef.close()

    LHSvertices = dict()
    for line in lhsf:
        vals = line.split(",")
        temp=dict()
        _id = vals[0]
        LHSvertices[_id]=dict()
        LHSvertices[_id]["deadline"]=deadlines[_id]
        LHSvertices[_id]["active"]=True
    lhsf.close()

    edgef=open(ROOT + "edgeNumbers" + CSV, "r")
    edges=dict()
    revEdges=dict()
    Vvertex=dict()
    VvertexMap=dict()
    edgeMapping=dict()
    
    cnt = 0
    cntv=0
    for line in edgef:
        vals=line.split(",")
        r = vals[1]
        l=vals[2].split("\n")[0]
        edges[l+ ";" + r] = dict()
        edges[l + ";" + r]["id"] = vals[0]
        revEdges[vals[0]]=l+";"+r
        edgeMapping[cnt]=vals[0]
        cnt+=1
        if r not in Vvertex:
            VvertexMap[cntv]=r
            cntv+=1
            Vvertex[r]=dict()
            Vvertex[r]["neighbor"] = list()
            Vvertex[r]["arrivals"]=list()
        Vvertex[r]["neighbor"].append(l)
    edgef.close()
    
    print cntv

    edgef=open(ROOT + "Wevalues" + CSV, "r")

    for line in edgef:
        vals=line.split(",")
        edges[revEdges[vals[0]]]["weight"]=float(vals[1].split("\n")[0])
    edgef.close()

    resources=list()
    Bkf=open(ROOT + Bkfile + CSV, "r")


    for line in Bkf:
        vals=line.split(",")
        resources.append(float(vals[0].split("\n")[0]))    
    Bkf.close()

    Aef = open(ROOT + aefile + CSV, "r")
    for line in Aef:
        vals=line.split(",")
        val = vals[0].split("\n")[0]
        edges[revEdges[val]]["Ae"] = list()
        edges[revEdges[val]]["xe"] = list()
        
        for i in xrange(1, len(vals)):
            edges[revEdges[vals[0]]]["Ae"].append(vals[i])
    Aef.close() 
    
    xef=open(ROOT + xefile + CSV, "r")
    e=0
    for line in xef:
        edges[edgeMapping[e%T]]["xe"].append(float(line.split("\n")[0]))
        e+=1

    pjtf=open(ROOT + pjtfile + CSV, "r")
    
    vv=0
    for line in pjtf:
        vals=line.split(",")
        Vvertex[VvertexMap[vv%cntv]]["arrivals"].append(float(vals[0].split("\n")[0]))   
        vv+=1
    pjtf.close()

    #Start simulation of the problem
    ALGcost=0
    LPvalue=0

    #Obtain the cost of LP

    count = 0
    for t in xrange(T):
        RHSarrival = sample_RHS_vertex(Vvertex, t)
        if RHSarrival == -1:
            continue
        #Get Available Assignments
        available=list()
        atLeastOnce=False
        for key in Vvertex[RHSarrival]["neighbor"]:
            if LHSvertices[key]["active"]:
                potentialEdge=str(key) + ";" + str(RHSarrival)
                possible=True
                for i in edges[potentialEdge]["Ae"]:
                    if resources[int(i)]<1:
                        possible=False
                        break
                if possible:
                    available.append(key)
        #Make an assignment
        assigned = -1
        maxi = -1
        r = random.uniform(0, 1)
        cur = 0
        total=0
        for u in available:
            potentialEdge=str(u) + ";" + str(RHSarrival)
            total+=edges[potentialEdge]["xe"][t]

        for u in available:
            potentialEdge=str(u) + ";" + str(RHSarrival)
            if edges[potentialEdge]["xe"][t]/float(total)-cur>r:
                assigned=u
                break
            cur+=edges[potentialEdge]["xe"][t]/float(total)
        
        #Update parameters
        for key in LHSvertices:
            if key == assigned:
                LHSvertices[key]["active"]=False
            if t+1 > LHSvertices[key]["deadline"]:
                LHSvertices[key]["active"]=False
       
        if assigned == -1:
            continue
        print "Assigned"
        matchedEdge=str(assigned) + ";" + str(RHSarrival)
        for i in xrange(len(resources)):
            if i not in edges[matchedEdge]["Ae"]:
                continue
            for j in xrange(len(edges[matchedEdge]["Ae"])):
                if edges[matchedEdge]["Ae"][j]==i:
                    resources[i]-=edges[matchedEdge]["Ae"][j]

        ALGcost+=edges[matchedEdge]["weight"]


    print float(ALGcost)
    #print float(ALGcost)/float(LPvalue)







