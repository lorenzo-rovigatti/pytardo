'''
Created on 18 mag 2018

@author: lorenzo
'''
import time
import smtplib
from email.mime.text import MIMEText

class WriteToFile(object):
    '''
    Writes the warnings to a file
    '''

    def __init__(self, filename, append):
        '''
        Constructor
        '''
        self.filename = filename
        self.append = append
        
    def react(self, current_values, warnings):
        if self.append:
            mode = "a"
        else:
            mode = "w"
            
        with open(self.filename, mode) as output:
            for w in warnings:
                line = time.strftime('%Y-%m-%d %H:%M:%S')
                condition = str(w.condition) % w.value
                line += " %s = %s" % (w.name, condition)
                print >> output, line


class SendEmail(object):
    '''
    Sends emails 
    '''
    
    def __init__(self, from_address, recipients, min_interval):
        self.from_address = from_address
        self.recipients = recipients
        self.subject = "Patchy Monitor Warning"
        self.base_text = "%s\n\nThe following readings have exceeded their associated user-defined thresholds:\n"
        self.last_warnings = []
        self.min_interval = min_interval
        self.time_last_email = 0
        
    def _send_email(self, msg):
        if (time.time() - self.time_last_email) > self.min_interval:
            s = smtplib.SMTP('localhost')
            s.sendmail(self.from_address, self.recipients, msg.as_string())
            s.quit()
            self.time_last_email = time.time()
        
    def react(self, current_values, warnings):
        if len(warnings) > 0:
            text = self.base_text % time.strftime('%Y-%m-%d %H:%M:%S')
            for w in warnings:
                condition = str(w.condition) % w.value
                text += "\n%s = %s" % (w.name, condition)
        
            msg = MIMEText(text)
            msg['Subject'] = self.subject
            msg['From'] = self.from_address
            msg['To'] = ",".join(self.recipients)
            
            self._send_email(msg)
            
            self.last_warnings = warnings
            