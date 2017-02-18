import smtplib, os, sys, re
from email.mime.text import MIMEText

try:
    cmd = "sudo systemctl status " + sys.argv[1] + " -l > status"
    os.system(cmd)

    with open('status') as f:
        mime  = f.read()
        reg = mime
        m = re.search("active \(running\)", reg)
        try:
            if m.group(0):
                pass
                #Do nothing, service is up and running
        except:
            msg = MIMEText(mime)
            msg['Subject'] = str(sys.argv[1]) + ' has stopped working'
            msg['From'] = 'you@yourdomain.com'
            msg['To'] = 'reciver@yourdomain.com'

            s = smtplib.SMTP('smtp.yourdomain.com')
            s.send_message(msg)
            s.quit()
except Exception as e:
        print('Exception! => %s' %e)
        sys.exit(2)
