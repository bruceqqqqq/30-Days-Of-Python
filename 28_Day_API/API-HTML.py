"""
API é um mecanismo que permite a interação entre duas aplicações utilizando algumas regras.
Main Types of API
Open API = Tambem conhecida por api publica, não tem restrições de acesso.
Partner API = Um programador precisa de acesso restrito ou licenças para acessar.
Internal API = ou api privada, só os sistemas internos estão expostos a essa API,
essas apis são desenhas especificamente para alguns sistemas, são usados para
aprimorar seus times e produtos.
Composite API = Esse tipo de API combina diferentes tipos de API, é uma sequerencia de tarefas
que roda simultaneamente para o resultado de uma execução, é usado para acelerar processos e
melhorar a performance de web interfaces.

Web Services API:
Um web service é um sistema ou software que usa IP, i.e., url na internet, para prover acessos a serviços

SOAP:Simple Object Access Protocol - Esse protocolo usa XML como formato para transformar em data.
Sua maior função é definir estruturas de mensagens e métodos de comunicação, tambem utiliza WSDL, na
leitura-maquina de documento para definir interfaces.

XML-RPC: Esse é um protocolo que usa especificamente XML para transformar em dados, diferente do SOAP,
esse usa propriamente XML, e é mais velho a SOAP. XML-RPC usa a menor banda larga e é muito mais simples que SOAP
Example:
<employees>
  <employee>
    <firstName>Becky</firstName> <lastName>Smith</lastName>

JSON-RPC: Esse é similiar a XML-RPC mas inves de XML usa JSON.
Example:
{"employees":[
 { "firstName":"Becky", "lastName":"Smith" }
 ]

REST: Rest não é um protocolo como os outros, invés disso, é um bando de arquitetura principios.
O REST serviço precisa de algumas características, incluindo interfaces simples, que são recursos indetificados facilmente
com request e manipulação de recursos usando interface.

Qual a diferença de SOAP e REST?
SOAP:
Tem regras restritas e segurança avançada a seguir.
É dirigido por funções
Requer bastante internet

REST:
Existem diretrizes vagas a serem seguidas, permitindo que os desenvolvedores façam recomendações facilmente
É dirigido por data
Requer o minimo de internet

Qual a diferença de JSON e XML?

JSON:
Suporta somente numeros e textos
Foco principalmente em data
Tem segurança baixa

XML:
Suporta varios tipos de data
Foco principalmente em documento
Tem mais segurança

Tipos de API por categoria
Clima: https://rapidapi.com/blog/access-global-weather-data-with-these-weather-apis/
Esporte: https://rapidapi.com/blog/best-sports-apis-ranked/
Mensagem de Texto: https://rapidapi.com/blog/sms-apis-send-texts/
Comida e Restaurantes: https://rapidapi.com/blog/we-love-these-restaurant-apis/
Musica: https://rapidapi.com/blog/top-free-music-data-apis/
Noticias: https://rapidapi.com/blog/rapidapi-featured-news-apis/
Dicionario(Palavras, not dict): https://rapidapi.com/blog/dictionary-apis/
Viagem: https://rapidapi.com/blog/best-travel-apis-guide/
Imobiliária: https://rapidapi.com/blog/best-real-estate-apis/
IP Geolocation: https://rapidapi.com/blog/ip-geolocation-api/
Cupom: https://rapidapi.com/blog/best-coupon-rewards-api/
Video Games: https://rapidapi.com/blog/top-video-game-apis/
Álcool: https://rapidapi.com/blog/best-beer-wine-alcohol-api/
And others...

Font of traduction: https://rapidapi.com/blog/types-of-apis/
"""

"""
HTTP é a tecnologia padrão (Hypertext Transfer Protocol) é ela que utilizamos para se comunicar quando utilizamos o browser.
A Level fundamental, quando você visita um site, seu navegador faz uma HTTP request para um servidor. Então esse server
responde com um recurso(um imagem, um video, ou um pagina em HTML) - o que aparecer na tela do seu navegador

Isso é HTTP mensagem-baseada-modelo. toda interação HTTP inclui um REQUEST e RESPONSE

Por natureza, o HTTP é stateless.

Stateless significa que todos requests são separados um do outro. Então todo request do seu navegador precisa conter 
informação suficiente para que o server preencha o request. Isso significa que toda transação de mensagens baseadas em HTTP
é processada separadamente uma da outra.

URL (Uniform Resource Locator)
Provavelmente é o conceito mais conhecido pela Web. E tambem é o mais importante e o que tem mais conceitos uteis.
A URL é o endereço para identificar recursos na internet.

A ideia de uma Internet é estrutura por recursos, desde o começo a internet é uma plataforma de compartilhar text/html
documentos, imagens e etc e isso é considerado uma coleção de recursos.

Exemplo de uma URL
http:/   | //www.example.com/ |  search | ?item=vw+beetle
protocolo| domínio            |  path   | parametros

Protocolo: Maioria das vezes são http ou https (versão mais segura do HTTP).
Outros protocolos: ftp transferência de arquivos e smtp email transmission 

Domínio: Nome usado para identificar um ou mais IP's onde o conteúdo está localizado

Path: Especifica onde o conteúdo está localizado no servidor. exemplo /search/cars/VWBeetle.pdf or C:/my cars/VWBeetle.pdf).

Parametros: Informação adicional usada para identificar ou filtrar um conteúdo

Nota: Quando estiver procurando por post e mais informação sobre HTTP, você provavelmente pode encontrar o termo URI.
URI as vezes é usado invés de URL. (Pesquisar depois)

HTTP Requests 
No HTTP, todo request precisa ter uma URL. Adicionalmente, o request precisa de um method, o HTTP tem 4 methods padrões:
GET / POST / PUT / DELETE
Esses methods correspondem diretamente a 
read / create / update / delete

Todos HTTPS mensagens tem pelo menos 1 ou mais headers, seguido por uma opcional mensagem.
O body tem informações que sera mandado com o request ou a informações enviada pelo response

A primeira parte de todo HTTP request tem esses 3 itens:
Exemplo: Example:
GET /adds/search-result?item=vw+beetle HTTP/1.1

Quando a url tem "?" significa que contém uma query, isso significa que está mandando parametros de um recurso de request.

1- A primeira parte é um method que avisa o http qual método esta usando, mais comum é o GET. Get recupera um recurso
do servidor Web e uma vez que GET não tem body de mensagem, nada depois do cabeçalho é necessário.
2- A segunda parte é a url solicitada
3- A terceira parte é a versão do HTTP sendo usada. Versão 1.1. é a mais comum versão para maioria dos browsers, versão 2.0
está tentando aparecer mais.

E tem outras coisas interessantes sobre o request:

Referer header = Informa o URL de onde a solicitação se originou.
User-agent Header = informação adicional sobre o navegador sendo usado para gerar o request
Host header = Identifica o host name, usado quando o multiplas paginas em 1 web server
Cookie-Header = Adiciona parametros adicionais ao client.

Agora vamos ao HTTP response.

Igualmente o HTTP request, HTTP response tambem tem 3 itens:
Exemplo: HTTP/1.1 200 OK
1- A primeira parte é a versão do HTTP
2- A segunda parte é o código numérico do resultado para o request (200 means ok)
3- A terceira parte é um descrição em texto da segunda parte

E tem outras coisas interessantes sobre o response:

Server-header = Informação sobre o web server software sendo usado
Set-Cookie-Header = emite o cookie para o navegador.
Message body = é comum que uma resposta HTTP contenha o corpo de uma mensagem.
Content-Length header = fala o tamanho mensagens do body em bytes

HTTP Methods:

O mais comum method é o GET e POST, mas tem alguns outros também.

GET - Você vai usar esse method para request data de um especifico recurso onde o data não é modificado em nenhum momento.
Get requests não mudam o estado do recurso.

POST - Você usa esse method para enviar data para o server para criar um recurso.

PUT - Você usa esse method para atualizar um recurso existente no server usando o conteúdo do body do request.
Pense que é como se você estivesse editando algo

HEAD - Você usa esse method do mesmo jeito quem GET, mas com a diferença que o retorno do HEAD deve não conter body na response.
Mas o retorno vai conter algumas HEADERS se o GET for usado. Você usa o HEAD para verificar o recurso está presente antes de fazer um GET request.

TRACE - Você usa esse method para diagnosticar. a response vai conter no body o conteúdo exato do request.

OPTIONS - Você usa esse method para descrever a opções de comunicação (HTTP methods) que estão disponíveis para o alvo.

PATCH - Você usa esse method para aplicar modificações parciais para o recurso.

DELETE - Você usa esse method para deletar recurso especifico.
--------------------------------------------------------------------
REST - (Representational state transfer)
É um estilo de estrutura onde request e response contém representações do atual estado dos recursos do sistema.

“Regular” way:
http://carapp.com/search?make=wv&model=beetle

REST-style:
http://carapp.com/search/vw/beetle
--------------------------------------------------------------------
HTTP Headers
Aqui tem três principais componentes que montam uma estrutura de request/response 
First line
Headers
Body/Content

A gente já falou da primeira linha no HTTP e da função do body, agora vamos falar dos headers.

O HTTP Headers foi adicionado depois da primeira linha e foi definido como "name:value" pares separados por uma coluna
HTTP Headers são usados para enviar parametros adicionais junto com o request e o response.

Como foi dito anteriormente, a mensagem do body inclui a informação a ser enviada com o request, ou informação a ser devolvida
com o response.

Mas tem diferentes tipos de headers que estão agrupados baseado em seu uso em 4 categorias:
GENERAL HEADER: Cabeçalhos que podem ser usados em request e response e que são independentes dos dados que estão sendo trocados.
REQUEST HEADER: Cabeçalhos que definem parametros para os dados requested ou parametros que dão informações importantes sobre
o client fazendo request.
RESPONSE HEADER: Esses cabeçalhos contém informações sobre o response encaminhado
ENTITY HEADER: Os cabeçalhos das entidades descrevem o conteúdo que compõe o corpo da mensagem.
--------------------------------------------------------------------
HTTP Status code
Navegando na Web, você provavelmente encontro 404 error not found ou 500 error server not responding, esse são HTTP status codes.
Todo HTTP response mensagem tem de conter um HTTP status code na primeira linha, falando para nós o resultado do request.
HTTP Status in a nutshell
1xx: Informativo.
2xx: Request com sucesso.
3xx: O Client foi redirecionado a um outro recurso.
4xx: Request com algum erro.
5xx: O servidor encontrou um erro ao cumprir a solicitação.
--------------------------------------------------------------------
HTTPS (Hypertext transfer protocol secure)
A versão segura do protocolo HTTP, ele provém uma comunicação criptografada usando TLS ou SSL.
Tanto o SSL quanto o TSL protocolos usa o assimétrico criptografado sistema. usa a chave publica e uma chave private para criptografar a mensagem
Qualquer um pode usar uma chave publica para criptografar mensagens, porém, chaves privadas são secretas, e significa que apenas o receptor pode descriptografar
-------------------------------------------------------------------- 
Handshake SSL / TLS
Quando você solicita uma conexão HTTPS a um site, o site envia seu certificado SSL para o seu navegador. 
Esse processo em que o navegador e o site iniciam a comunicação é chamado de “handshake SSL / TLS”.
O handshake SSL / TLS envolve uma série de etapas em que o navegador e o site validam um ao outro e iniciam a comunicação por meio do túnel SSL / TLS.
Como você provavelmente notou, quando um túnel seguro confiável é usado durante uma conexão HTTPS,
o ícone de cadeado verde é exibido na barra de endereço do navegador.
Exemplo de uma das minhas páginas seguras
-------------------------------------------------------------------- 
Benefícios de HTTPS
Os principais benefícios de um HTTPS são:
As informações do cliente, como números de cartão de crédito e outras informações confidenciais, são criptografadas e não podem ser interceptadas.
Os visitantes podem verificar se você é uma empresa registrada e se é o proprietário do domínio.
Os clientes sabem que não devem visitar sites sem HTTPS e, portanto, são mais propensos a confiar e concluir compras de sites que usam HTTPS.
"""