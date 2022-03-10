#!/usr/bin/env python

import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    resp = requests.get(f"{API}sets")
    
    print( resp.json() )

if __name__ == "__main__":
    main()
