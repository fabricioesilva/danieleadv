from livereload import Server

# Cria o servidor
server = Server()

# Observa a pasta atual (".") e recarrega o navegador quando arquivos mudarem
server.watch('.', delay=1)

# Inicia o servidor na porta 8000 (pode mudar se quiser)
server.serve(port=8000, host='localhost')
