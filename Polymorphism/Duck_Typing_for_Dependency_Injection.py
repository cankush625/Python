class flight :
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine() :
    def start(self):
        print("Starting the Airbus engine")

class BoingEngine() :
    def start(self):
        print("Starting the Boing engine")

ae = AirbusEngine()
f = flight(ae)
f.startEngine()

be = BoingEngine()
f1 = flight(be)
f1.startEngine()

'''By Ankush Chavan'''