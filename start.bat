start "ui" cmd.exe /k "npm run start -w=ui"
start "server-main" cmd.exe /k "npm run main -w=node_servers"
start "server-metadata" cmd.exe /k "npm run metadata -w=node_servers"
start "server-text" cmd.exe /k "cd text_server && mix run --no-halt"
start "server-weather" cmd.exe /k "weather_server/env/Scripts/Activate.bat && python3 -m ./weather_server"
start "server-body" cmd.exe /k "body_server/env/Scripts/Activate.bat && python3 -m ./body_server"
start "server-animal" cmd.exe /k "animal_server/env/Scripts/Activate.bat && python3 -m ./animal_server"
start "server-style" cmd.exe /k "style_server/env/Scripts/Activate.bat && python3 -m ./style_server"
start "server-people" cmd.exe /k "cd ./people_server/build/bin && ./peopleServer.exe"
start "server-format" cmd.exe /k "format_server/env/Scripts/Activate.bat && python3 -m ./format_server"
start "server-color" cmd.exe /k "color_server/env/Scripts/Activate.bat && python3 -m ./color_server"
