# !cve queries the CIRCL CVE database

import os, requests, json, re
from errbot import BotPlugin, botcmd, arg_botcmd

class cve(BotPlugin):

    @botcmd(split_args_with=None, hidden=True)
    def cve(self, mess, args):

        if len(args)!=1:
            return("Incorrect number of parameters.  Syntax:  !cve <number>")
            exit()

        # Assign arguments to variables
        arg=args[0]
        if re.match(r'[\d]+', arg):
          urlip = "http://cve.circl.lu/api/last/" + arg

          try:
              response = requests.get(urlip)
          except:
              return("Could not retrieve page")
              exit()
        else:
          return("Error: Input must be an integer.")

        #read html code
        data = response.json()
        return(json.dumps(data, sort_keys=True, indent=4))

