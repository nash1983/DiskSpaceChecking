import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def colored_mail():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"{compName} Disk Usage Statistics \n\n"
    msg['From'] = "easupport@boltonclarke.com.au"
    msg['To'] = "ISEnterpriseApplications@boltonclarke.com.au"

    text = (f"Warning: <br>\n"
            f" ***********************************************  <br>\n"
            f"{path} - Less than 5% disk space is remaining  <br> \n"
            f"*********************************************** <br>\n"
            f"Total Disk size is: {disk_total1} GB <br>\n"
            f"Total Free space is: {disk_free1} GB <br>\n"
            f"Total Used space is: {disk_used1} GB <br>\n")

    html = """\
    <html>
      <head></head>
      <body>
        <p style="color: red;"> {text}
        </p>
        
      </body>
    </html>
    """.format(**locals())

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)  # text must be the first one
    msg.attach(part2)  # html must be the last one

    s = smtplib.SMTP('relay.rslc.local', 25)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()


def sending_mail():
    with smtplib.SMTP('relay.rslc.local', 25) as smtp:
        body2 = (
            f"*********************************************** \n"
            f"{path} - Less than 10% disk space is remaining  \n "
            f"*********************************************** \n"
            f"Total Disk size is: {disk_total1} GB \n"
            f"Total Free space is: {disk_free1} GB \n"
            f"Total Used space is: {disk_used1} GB\n")
        smtp.sendmail(from_addr='easupport@boltonclarke.com.au',
                      to_addrs='ISEnterpriseApplications@boltonclarke.com.au',
                      msg=f"Subject:{compName} Disk Usage Statistics \n\n {body2}")


workstations = ['t1sqlag01', 't1sqlag02', 'Prd-cc0-sql01', 'prd-cc0-sql02', 'prd-cc0-sql03', 'prd-CMC0-SQL01',
                'PRD-CMC0-SQL02', 'PRD-CMC0-SQL03', 'PRD-PROCSQL01', 'PRD-PROCSQL02', 'PRD-PROCSQL03', 'PRD-YCH0-SQL01',
                'RSLSQL', 'RSLSQLDAG01', 'RSLSQLDAG02', 'P2SQLAG01', 'P2SQLAG02', 'PRD-ACSQL01', 'PRD-ACSQL02']

for compName in workstations:
    path1 = '\\\\' + compName + '\\C$'
    path2 = "\\\\" + compName + "\\E$"
    path3 = "\\\\" + compName + "\\F$"
    path4 = "\\\\" + compName + "\\G$"
    path5 = "\\\\" + compName + "\\H$"
    path6 = "\\\\" + compName + "\\I$"
    path7 = "\\\\" + compName + "\\J$"
    path8 = "\\\\" + compName + "\\K$"
    path9 = "\\\\" + compName + "\\L$"
    path10 = "\\\\" + compName + "\\M$"
    path11 = "\\\\" + compName + "\\N$"
    path12 = "\\\\" + compName + "\\O$"
    path13 = "\\\\" + compName + "\\P$"
    path14 = "\\\\" + compName + "\\R$"
    path15 = "\\\\" + compName + "\\T$"
    path16 = "\\\\" + compName + "\\U$"
    path17 = "\\\\" + compName + "\\V$"
    path18 = "\\\\" + compName + "\\W$"
    path19 = "\\\\" + compName + "\\Y$"
    path20 = "\\\\" + compName + "\\Z$"

    paths = [path1, path2, path3, path4, path5, path5, path6, path7, path8, path9, path10, path11, path12, path13,
             path14, path15, path16, path17, path18, path19, path20]

    for path in paths:
        try:
            check_drive = shutil.disk_usage(path)
            disk_free = float(check_drive.free / 2 ** 30)
            disk_total = float(check_drive.total / 2 ** 30)
            disk_used = float(check_drive.used / 2 ** 30)
            disk_free1 = float("{0:.2f}".format(disk_free))
            disk_total1 = float("{0:.2f}".format(disk_total))
            disk_used1 = float("{0:.2f}".format(disk_used))
            percent = lambda part, whole: float(whole) / 100 * float(part)
            percent1 = percent(5, disk_total)
            percent2 = percent(10, disk_total)
            if disk_free < percent1:
                colored_mail()
            elif disk_free < percent2:
                sending_mail()
        except:
            pass
