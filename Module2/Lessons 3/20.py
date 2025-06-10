import time

import progress.bar as pb

bar = pb.ChargingBar("Loading", max=100)
for i in range(100):
    bar.next()
    time.sleep(0.1)

bar.finish()
print("Loading complete")
