"""
Michael Gonzalez
CS356 Project Step #3
Routing Algorithm - Router 2
04.21.2015
"""
import socket
import pickle
import router

def SendAllRT():
	router.SendRT("localhost",port_Table[1], rTable)
	router.SendRT(machine0, port_Table[0], rTable)
	router.SendRT(machine0, port_Table[3], rTable)

# Init
print("\n\t\t---Router #2 Program---")
machine0 = input("\n\tEnter Machine #0 IP: ")

rTable = [[0, 2, 3], [1, 0, 1], [2, "Local", 0], [3, 1, 2]] # Rtr#, If#, Cost
port_Table = [50000, 50111, 50222, 50333] # Rtr# = index, port number

# Receive all
print("Receiving table replies...")
passive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
passive.bind(("", port_Table[2])) # bind to router's own port
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