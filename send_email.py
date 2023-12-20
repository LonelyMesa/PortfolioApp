def send_email(message):
    import smtplib, ssl
    host = "smtp.gmail.com"
    port = 465

    username = "lonelymesa5@gmail.com"
    password = ""

    receiver = "lonelymesa5@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


