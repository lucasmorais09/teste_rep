from botcity.plugins.email import BotEmailPlugin

# Instanciar o plug -in 
email = BotEmailPlugin() 

# Configure IMAP com o servidor Gmail 
email.configure_imap("outlook.office365.com", 993) 

# Configure SMTP com o servidor Gmail 
email.configure_smtp("outlook.office365.com", 587) 

# Faça login com uma conta de email válida 
email.login("lucas.morais@t2cgroup.com.br", "1972luci!@#")

# Definindo informações do email 
para = ["morais.lucas.2004@gmail.com", "felipemor@gmail.com"] 
assunto = "Teste de envio de emai!" 
corpo_email = "<h1>Olá!</h1> Isso é um teste!" 

# Enviando a mensagem de e -mail 
email.send_message(assunto, corpo_email, para, use_html=True)

# Feche a conexão com os servidores IMAP e SMTP 
email.disconnect()