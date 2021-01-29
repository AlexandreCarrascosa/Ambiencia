# Ambiencia

**PARA ACESSAR O SITE:** https://alexandrecarrascosa.github.io/Ambiencia/

A pasta [**"Sensore_modulo_rele"**](/Sensores_modulo_rele) contém o código do arduíno que foi enviado para a placa.  
A pasta [**"Backend"**](/backend) contém os códigos em __Python__ que fazem a leitura e escrita do XML e fazem o _upload_ para o GitHub dos arquivos.  
  
**As demais pastas são correspondentes a programação em __JavaScript__ e a estrutura do site feitos em HTML e CSS.**

## Pasta Backend

* **[CalcPsic.py:](/backend/CalcPsic.py)** função responsável por fazer os cálculos psicométricos com os dados atuais
* **[Atualreplace.py:](/backend/atualreplace.py)** altera os valores do arquivo **atual.xml** para as informações recém coletadas do arduino.  
* **[ReadTemp.py:](/backend/readTemp.py)** arquivo principal, responsável por acionar o **Serial** do arduino e iniciar o código já escrito dentro da placa, este chama as funções/bibliotecas que estão
contidas nesta pasta.  
* **[timer.py:](/backend/timer.py)** Sem utilidade
* **[update.py:](/backend/update.py)** Possui as funções responsáveis por calcular o tempo para cada registro e a função de enviar as informações para o GitHub.



### Pasta [__Assets__](/assets)
* Contém as imagens de logos tanto e _backgroud_ da página  

### Pasta [__icons__](/icons)
* Contém os icones utilizados nas tabelas  

### Pasta [__pages__](/pages)
* Contém as páginas do site, fora a principal.  
* Dentro do site, apenas as páginas [__historico.html__](/pages/historico.html) e [__info.html__](/pages/info.html) foram utilizados.

### Pasta [__scripts__](/scripts)
* Códigos em __JavaScript__ que fazem a leitura dos arquivos XML e criam o sistema de paginação da lista na página [__historico.html__](/pages/historico.html)

### Pasta [__styles__](/styles)
* Contém o __design__ para cada página do site e o sistema para tornar o design responsivo para celular.

### Demais arquivos
* [__calc.xml:__](calc.xml) arquivo xml com os cálculos para temperatura e umidade atual, para cidade Rondonópolis - MT  
* [__atual.xml:__](atual.xml) arquivo xml com as informações da estufa: Temperatura, Umidade e situação dos componentes  
* [__data.xml:__](data.xml) arquivo xml com o histórico de registros da estufa  
* [__index.html__](index.html) arquivo que carrega o site e página inicial do mesmo.


**OS DEMAIS ARQUIVOS NÃO SÃO RELEVANTES PARA O FUNCIONAMENTO DO SISTEMA E/OU SITE.**
