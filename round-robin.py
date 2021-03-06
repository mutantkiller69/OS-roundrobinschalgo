def findWaitingTime(processes, n, bt, wt, quantum):
    remaining_bt=[0]*n

    for i in range(n):
        remaining_bt[i]=bt[i]
    t=0

    while(1):
        done=True

        for i in range(n):
            if (remaining_bt[i]>0):
                done=False

                if (remaining_bt[i]>quantum):
                    t+=quantum
                    remaining_bt[i]-=quantum

                else:
                    t=t+remaining_bt[i]
                    wt[i]=t-bt[i]
                    remaining_bt[i]=0

        if (done==True):
            break

def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]


def findavgTime(processes, n, bt, quantum):
    wt=[0]*n
    tat=[0]*n

    findWaitingTime(processes, n, bt, wt, quantum)

    findTurnAroundTime(processes, n, bt, wt, tat)

    print("Processes    Brust Time    Waiting","Time    Turn-Around Time")

    total_wt=0
    total_tat=0
    for i in range(n):
        total_wt=total_wt+wt[i]
        total_tat=total_tat+tat[i]
        print( i+1, "\t\t" ,bt[i], "\t\t", wt[i], "\t\t", tat[i])

if __name__ =="__main__":
    processes=[1,2,3,4]
    n=4;
    bt=[9,5,3,4]
    quantum=2;
    findavgTime(processes,n,bt,quantum)
