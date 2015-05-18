"""
Michael Gonzalez
CS356 Project Step #3
Routing Algorithm - Router 0
04.21.2015
"""
import socket
import pickle
import router

def SendAllRT():
	router.SendRT("localhost",port_Table[3], rTable) # send to router 3
	router.SendRT(machine1, port_Table[1], rTable) # send to router 1
	router.SendRT(machine1, port_Table[2], rTable) # send to router 2

"""
Steps:
	send rt
	receive rt
	update rt
	display rt
"""

# Init
print("\n\t\t---Router #0 Program---")
machine1 = input("\n\tEnter Machine #1 IP: ")

rTable = [[0, "Local", 0], [1, 0, 1], [2, 1, 3], [3, 2, 7]] # Rtr#, If#, Cost
port_Table = [50000, 50111, 50222, 50333] # Rtr# = index, port number

# Initial
print("\nInitial table:")
router.printRT(rTable)
# Send
print("Sending RT to r1...")
router.SendRT(machine1, port_Table[1], rTable) # send to r1 first

# Receive all
print("Receiving table replies...")
passive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
passive.bind(("", port_Table[0]))
while True:
	data, addr = passive.recvfrom(1024) # listen
	peerTable = pickle.loads(data) # decode, receive table
	peerNum = router.ident(peerTable)
	if(router.updateRT(rTable, peerNum, peerTable) == False): continue # we have not received any better info
	else: 
		SendAllRT()
		print("Reply from r"+str(peerNum)+'\n')
		router.printRT(rTable)
passive.close()

# Print final table
print("\nFinal updated table:")
router.printRT(rTable)