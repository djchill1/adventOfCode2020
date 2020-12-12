import logging

def create_day_files(day):
    day = str(day)
    try:
        open(day+'_input.txt', "x")
    except:
        logging.error("Can't create input file for day " + day + " due to a conflict")
    try:
        open(day + '_test.txt', "x")
    except:
        logging.error("Can't create test file for day " + day + " due to a conflict")
    try:
        f = open(day + '.py', "x")
        f.write('import init\n\ndata = init.read_data(True, )')
        f.close()
    except:
        logging.error("Can't create python file for day " + day + " due to a conflict")

create_day_files(13)