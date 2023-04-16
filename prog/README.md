# Executar o back-end:
`python3 server.py`

# Acessar o back-end (teste):
`curl localhost:5000/listar_pessoas`

# Executar o front-end:
`python3 -m http.server`

# Acessar o front-end:
## no terminal:
`curl localhost:8000/listing.html`
## no navegador web:
`localhost:8000/listing.html`

# POST (Terminal):
`curl localhost:5000/incluir -d '{"nome":"John Stick","idade":17, "email":"jostick@gmail.com","telefone":"47 9 9222 1234"}' -H "Content-Type:application/json"`
