import os
from livereload import Server

# Garante que o diretório de trabalho seja a pasta 'public'
# Assim o 'localhost:8000' já vai abrir o index.html diretamente
os.chdir('public')

# Cria o servidor
server = Server()

# Observa todas as alterações dentro da pasta public
server.watch('.', delay=1)

# Inicia o servidor na porta 8000
print("Servidor rodando em http://localhost:8000")
server.serve(port=8000, host='localhost')