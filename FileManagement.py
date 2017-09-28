import time
import module_share

from Settings import COMMAND_CLEAR_TIMER, COMMAND_CLEAR_RUN


class fileManager():

	lastCommandCheck = time.time()

	def clearPendingCommands():
		if fileManager.lastCommandCheck < time.time()-int(COMMAND_CLEAR_RUN):
			fileManager.lastCommandCheck = time.time()
			for u in module_share.pending_commands:
				for c in module_share.pending_commands[u]:
					if int(c["time"]) < time.time()-int(COMMAND_CLEAR_TIMER):
						print("deleting command:")
						print(c)
						module_share.pending_commands[u].remove(c)