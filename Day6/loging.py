#critical ,Error ,INFO ,Debug ,Warning 

import  logging as lg

lg.basicConfig(filename="day6_log.txt",filemode="a",
               level=lg.DEBUG,format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
               datefmt="%d/%m/%Y %I:%M:%S:%p")
logger=lg.getLogger("lilly_app")
age =int(input("Enter the Age : "))

if age <0:   
    logger.error("The Age is Negative ",exc_info=True)
elif age <18:
    logger.warning("The Age is less 18 ",exc_info=True)
