<p align="center">
  <a href="http://www.climatempo.com.br">
      <img src="http://i.imgur.com/Q9lCAMF.png" alt="Climatempo" width="300px"/>
  </a>
</p>

___


## Processo de recrutamento

Olá desenvolvedor, pronto para participar do nosso
processo de recrutamento para vaga de Estágio em Análise de Dados?

### Sobre a Vaga

- Empresa: Climatempo;
- Bolsa auxílio – R$ 1.200,00;
- Horário: das 8h às 15h com 1h de almoço (30 horas semanais em horário comercial);
- Benefícios – auxílio transporte de R$ 200,00 / VR;
- Local: Parque Tecnológico - São José dos Campos (http://www.pqtec.org.br/).


### Atividades que serão desenvolvidas:

- Inclusão, exclusão e alteração de grande massa de dados via arquivos (Excel, CSV, JSON ou similar);
- Prestar auxílio no gerenciamento de cadastros realizados através das ferramentas internas.


### Requisitos

- Cursando 3º Semestre ou superior em Banco de Dados (ou curso relacionado à TI com ênfase em Banco de Dados);
- Conhecimentos intermediários em SGBD e SQL;
- Conhecimentos básicos em Python (para auxiliar na automatização de tarefas);
- Perfil analítico e comunicativo.


### Diferencial:

Conhecimentos em:

 - Nodejs
 - PHP
 - Postgres
 - MongoDB
 - Git
 - Docker


### IMPORTANTE:

- Residir no vale do paraíba ou nas proximidades.


## DESAFIO PARA ANÁLISE DE DADOS:

Através desse teste iremos analisar as seguintes competências:

- Gerenciamento e análise de dados;
- Conhecimentos em estrutura e modelagem de banco de dados;
- Conhecimentos em lógica de programação;
- Criatividade na resolução de problemas.

Imagine que você precise modelar o banco de dados de um sistema cuja finalidade é disparar alertas de raios via **email, sms, push, voz ou whatsapp** para determinados contatos de regiões específicas, e tudo isso deve ser armazenado de forma íntegra, ou seja, não podemos ter duplicação de dados, inconsistências e repetições.

Nesse banco de dados deve-se armazenar as seguintes informações:

- Nome, números de telefone e emails dos contatos que devem receber os alertas, as regiões escolhidas e as configurações de envio para cada um deles, seguindo as seguintes especificações:

1. Você deve armazenar o nome do contato que vai receber o alerta, o email e o número de telefone (caso o contato possua estes dados);

2. Cada contato pode ter um ou mais números de telefone cadastrados e o número obrigatoriamente deve conter **ddi** e **ddd**;

3. Cada contato pode ter um ou mais emails cadastrados;

4. O contato pode receber alerta dos seguintes tipos: **email, sms, voz, push notification e whatsapp**;

5. Deve ser definido o período em que o contato vai receber o alerta. Ele deve poder escolher em quais dias da semana ele deseja ser alertado e em qual intervalo de horário.

6. Deve-se ter uma tabela para armazenar os nomes das localidades que o contato deseja receber alertas;

7. Cada localidade pode estar em uma ou mais configurações de envio de alerta;

8. Existem três tipos de alertas que o contato pode receber: **verde, amarelo e vermelho.**

9. O cadastro de um alerta não necessariamente será feito em todos os emails e telefones cadastrados para o contato, no arquivo **contacts.xlsx** está especificado qual email e/ou telefone deverá receber alertas da localidade;

### Atenção:

- É importante que cada configuração de envio de alerta tenha um período de envio único, para que a sua customização não interfira nas outras configurações de envio;

- Deve ser possível registrar para que ele receba qualquer um desses tipos de alertas, independente da combinação, cada contato pode receber alerta de uma ou mais localidades diferentes, de um ou mais tipos diferentes.

- Só é possível cadastrar a mesma localidade para um mesmo contato se for para um tipo de envio diferente, por exemplo, se ele já vai receber alerta da localidade X via SMS, só poderá registrar a mesma localidade para um tipo que seja diferente de SMS.

### Abaixo um diagrama de relacionamento para auxiliar no desenvolvimento:

![diagrama-bd](https://user-images.githubusercontent.com/25674507/71759948-8cc54f00-2e94-11ea-95dc-c19b82925738.png)

### Você deverá:

1. Fazer um fork desse projeto no seu github;

2. Desenvolva! Você terá **7 dias** a partir da data do envio do desafio.

3. Criar o banco de dados utilizando o SGBD que quiser, mas achamos o uso do Postgres mais interessante :D

4. Desenvolver um script em **Python** ou **Nodejs** para realizar a inserção dos dados do arquivo **contacts.xlsx** no banco de dados;

5. Nos enviar um pull request contendo o arquivo **.sql** com a criação das tabelas, o **script** criado para realizar a inserção no banco e um arquivo em markdown chamado **PROJECT.md** contando um pouco sobre o seu desenvolvimento para o teste e como podemos testá-lo :D

6. Envie um e-mail para **curriculo@climatempo.com.br** com seu **currículo** com o assunto: **Vaga de Estágio - Análise de Dados** e o **link do seu pull request**.


Boa sorte!

___


Qualquer dúvida entre em contato com nossa equipe.


