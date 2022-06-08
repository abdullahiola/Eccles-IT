from datetime import dtetime

import cgitb
cgitb.enable()

current_time = datetime.now()

print("Content-type : text/plain\n")
print(current_time)

