#!/usr/bin/python3
""" print error code """

if __name__ == "__main__":
    import urllib.request
    import sys
    
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode())
    
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))

                                            
