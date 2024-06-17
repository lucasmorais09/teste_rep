from botcity.web import WebBot, By
from botcity.plugins.excel import BotExcelPlugin

# Iniciando uma nova instância de BotExcelPlugin 
bot_excel = BotExcelPlugin()

var_strCaminhoArquivo = r"C:\Users\lucas.morais\Downloads\challenge.xlsx"

# Iniciando uma nova instância de um WebBot 
bot = WebBot() 

# Caso você queira que o robô rode em segundo plano, marque como True 
bot.headless = False 

# O caminho do seu Chromedriver aqui 
bot.driver_path = r"C:\BotCity\chrome_driver\chromedriver.exe" 

# Abrindo o site da T2C 
bot.browse("https://www.rpachallenge.com/")

bot.maximize_window()

bot.wait(1000)

btn_submit = bot.find_element("//input[@type='submit']", By.XPATH)
btn_submit.click()



input_last_name = bot.find_element("//*[@ng-reflect-name='labelLastName']", By.XPATH)
input_last_name.click()
input_last_name.send_keys("Morais")

# Esperando 5 segundos 
bot.wait(5000)

# Fechando o navegador 
bot.stop_browser()