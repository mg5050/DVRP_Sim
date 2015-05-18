"""
Michael Gonzalez
CS356 Project Step #3
Routing Algorithm - Router 1
04.21.2015
"""
import socket
import pickle
import router

def SendAllRT():
	router.SendRT("localhost",port_Table[2], rTable)
	router.SendRT(machine0, port_Table[0], rTable)

# Init
print("\n\t\t---Router #1 Program---")
machine0 = input("\n\tEnter Machine #0 IP: ")

rTable = [[0, 2, 1], [1, "Local", 0], [2, 0, 1], [3, "None", 65535]] # Rtr#, If#, Cost
port_Table = [50000, 50111, 50222, 50333] # Rtr# = index, port number

# Receive all
print("Receiving table replies...")
passive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
passive.bind(("", port_Table[1]))
while True:
	data, addr = passive.recvfrom(1024) # listen
	peerTable = pickle.loads(data) # decode, receive table
	peerNum = router.ident(peerTable)
	if(router.updateRT(rTable, peerNum, peerTable) == False): continue # we have not received any better info
	else: SendAllRT()
passive.close()
SendAllRT()

# Print final table
print("\nFinal updated table:")
router.printRT(rTable)