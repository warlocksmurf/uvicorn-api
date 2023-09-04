import json
import uvicorn
from fastapi import FastAPI

# Initialize blockchain platform details as JSON strings
platform1 = json.loads('{ "name":"EOSIO", "type":"Public"}')
platform2 = json.loads('{ "name":"Ethereum", "type":"Public"}')
platform3 = json.loads('{ "name":"Hyperledger Fabric", "type":"Consortium"}')
platform4 = json.loads('{ "name":"Ethereum", "type":"Consortium"}')
platform5 = json.loads('{ "name":"Hyperledger Fabric", "type":"Private"}')
platform6 = json.loads('{ "name":"Ethereum", "type":"Private"}')
platform7 = json.loads('{ "name":"Ethereum", "type":"Hybrid"}')

# Assign a numerical value to each crtiteria
    # 1: Requires payment
    # 2: Does not require payment
    # 3: Privacy
    # 4: Transparency
    # 5: Requires large payment
    # 6: Does not require large payment
    # 7: Efficiency
    # 8: Maturity
    # 9: Contract management
    # 10: Information management
    # 11: Decentralized governance
    # 12: Consortium governance
    # 13: Centralized governance

# Set the criteria for each blockchain platform
p1 = [platform1,[1,4,6,7],[2,9,4,7],[2,10,11,4,7]]
p2 = [platform2,[1,4,5],[1,4,6,8],[2,9,4,8],[2,10,11,4,8]]
p3 = [platform3,[2,10,12,7]]
p4 = [platform4,[2,10,12,8]]
p5 = [platform5,[2,10,13,7]]
p6 = [platform6,[2,10,13,8]]
p7 = [platform7,[1,3],[2,9,3],[2,10,11,3]]

# Places platforms in an array to be looped through when checking
platforms = [p1,p2,p3,p4,p5,p6,p7]

# Function to check given parameters against all the platforms' set criteria
def Check(platform, parameters):
    for i in range(1,len(platform)):
        if all(x in parameters for x in platform[i]):
            return True

# Creation of the API
ourAPI = FastAPI()
@ourAPI.get("/")
def main(p1: int | None = None, p2 : int | None = None, p3 : int | None = None, p4 : int | None = None, p5: int | None = None): #gets parameters
      x = [p1,p2,p3,p4,p5] #places parameters in array to be checked against set criteria
      for p in platforms:
          if Check(p, x):
              return (p[0])
      return json.loads('{"message":"Sorry, no blockchain platforms meet your crtiteria"}')

# Starts the server
uvicorn.run(ourAPI, host="0.0.0.0", port=8080)