import os
iscontainer = os.environ.get("ISCONTAINER", False)
iscontainer = True

OUTPUTDIR = (
    "/root/output/" 
    if iscontainer 
    else None
)