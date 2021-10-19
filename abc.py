from qiskit import QuantumRegister, ClassicalRegister,QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
IBMQ.save_account('6b5dce45561a72edd27ccd67f0a724eb1466ef5b1af9b927afe5dd2314d236f79db0b775ac8fabeadb56b669594e79cdf73c728e3b007c525761c85879401a3a', overwrite=True)
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q')

def qrandom(n1):
    q = QuantumRegister(n1,'q')
    c = ClassicalRegister(n1,'c')
    circuit = QuantumCircuit(q,c) 
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 
    backend = provider.get_backend('ibmq_qasm_simulator')
    job = execute(circuit, backend, shots=1)                 
    counts = job.result().get_counts()
    return counts

def choosepair(numarray,n,result):
    #numarray is a 2D list of n pairs
    a = qrandom(n)
    akey = ''
    i = 0
    for key in a.keys():
        akey = key
    for i in range(n):
        if akey[i] == '0':
            result[i] = numarray[i][0]
        else:
            result[i] = numarray[i][1]
    return result
 
arr = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

#print(arr)
    

#c = [0 for i in range(len(arr))]
#c = choosepair(arr,len(arr),c)
#print(c)

def chooseone(num5):
    a = qrandom(3)
    if '000' in a.keys():
        return num5[0]
    elif '001' in a.keys():
        return num5[1]
    elif '010' in a.keys():
        return num5[2]
    elif '011' in a.keys():
        return num5[3]
    elif '100' in a.keys():
        return num5[4]
    else:
        chooseone(num5)

#li = [0,1,2,3,4]
#print(chooseone(li)) 
IBMQ.disable_account()
