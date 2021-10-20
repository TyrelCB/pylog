# Read Syslog output and alert

import Write_Output as wo
import glob
import datetime as dt
import time
from Email import send_email as se

while True:
    # Import Match Criteria and Email Config
    action_alerts = wo.read_file('py_reader_alert_criteria')
    action_alerts = eval(action_alerts)
    config = wo.read_file('py_reader_config')
    config = eval(config)
    mail_server = config['mail_server']
    from_address = config['from_address']
    to_address = config['to_address']
    date = dt.datetime.now().date() # Set the Date
    logfiles = glob.glob('*'+str(date)+'.log') # Gather the logfiles
    print(logfiles)

    try:
        # Get the current line count (don't examine lines already proccessed)
        track_dict = wo.read_file('count_track_'+str(date))
        track_dict = eval(track_dict)
        print('imported','count_track_'+str(date))
    except:
        # if there is no line count file, create a new ConnectHandler
        master_count = 0
        track_dict = {}
        for logfile in logfiles:
            track_dict[logfile] = master_count
            wo.write_to_file('count_track_'+str(date), track_dict)
        print('created','count_track_'+str(date))

    for logfile,master_count in track_dict.items():
        log = wo.read_file(logfile)
        log = log.split('\n')
        #print(len(log))
        count = len(log)
        if count > master_count:
            linecount = 0
            for line in log:
                linecount = linecount+1
                if linecount > master_count:
                    for alert,interesting in action_alerts.items():
                        if interesting in line:
                            print(alert,linecount,line)
                            data = [str(alert),'Syslog Line: '+str(linecount),str(line)]
                            data = '\n'.join(data)
                            subject = alert
                            se.send_email(mail_server,subject, from_address, to_address, data)
        else:
            print('no new lines')
        track_dict[logfile] = count
        wo.write_to_file('count_track_'+str(date), track_dict)
    time.sleep(10)
