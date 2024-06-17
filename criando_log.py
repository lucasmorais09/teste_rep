from botcity.maestro import * 

maestro = BotMaestroSDK() 

# Pegue as informações no DEV.ENVIROMENT no Maestro 
maestro.login(server="https://developers.botcity.dev", login="6219f921-52c4-4aed-861f-7ddbb694d49e", key="621_U4OI1GPZ2REKAMVQOE5E") 

maestro.new_log_entry( 
    activity_label="nomes", 
    values={ 
        "Nome": "João", 
        "Idade": "24" 
    }
)