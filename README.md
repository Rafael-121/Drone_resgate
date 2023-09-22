# Sea Guardian

Projeto de auxílio à bombeiros e salvavidas no resgate, principalmente, de pessoas.

![hi (2)](https://github.com/Rafael-121/Rafael-121/assets/137511020/21530c48-37ce-45c0-810f-b89565e73ba1)

---

Nosso projeto é dirigido pelos integrantes:.

Rafael Oliveira, Kimberly Rotman, Gabriela Grigoleto, Jhully Ferreira, Guilherme Setin
e DR. Álvaro Cantieri.

22/06/2023

---

## Objetivo

   Somos estudantes do IFPR Capmus Pinhais e estamos no nosso último ano do Ensino Médio Técnico. Como projeto de Conclusão de Curoso(TCC) nós nos propomos em parceria com as Oficinas 2.0 a fazer um drone de monitoramento em ambientes com superfície aquática. Nosso comprometimento é de utilizar um drone com sistema embarcado que será responsável pelo envio de imagens para um comutador com maior poder de processamento que contará com uma inteligência artificial(IA) que processará as imagens capturadas pelo drone e fornecerá um panorama de entidades presentes no seu campo de visão, com isso ajudar na identificação de pessoas em risco de acidente aquático, além de declarar a posição dos respectivos objetos capturados.

| __Objetivos de Desenvolvimento__ | _Descrição_ |
| --- | --- |
| __Projeto:__ Drone para Resgate de Pessoas em Condição de Afogamento | __Versão:__ Beta |
| __Cliente:__ Socorristas/Bombeiros | __Data:__ 31/01/2024 |

## Escopo

Os casos de afogamentos não são novidades, pelo contrário, são contribuintes para que a porcentagem aumente no Brasil. De acordo com o artigo “ O material técnico de salvamento aquático”, o número de óbitos por afogamentos em nosso país supera os 6.000 casos por ano, e os incidentes não fatais que chegam a mais de 100.000. 

No Brasil, o afogamento é a segunda causa de óbito de 1 a 9 anos, terceira causa de 10 a 19 anos, e quarta causa de 20 a 25. A maioria dos afogamentos ocorrem em áreas abertas, sejam elas mar aberto, praias, rios, lagos, represas, considerando que 75% dos óbitos ocorrem em rios e represas, sendo o Norte do Brasil a região com mais mortalidade. 

Segundo o Material técnico de salvamento aquático, é de grande pesar e importância a utilização dos equipamentos para salvamento de banhistas, como bóias e coletes. Contudo, em situações específicas, como competições de nado em mar aberto, é preciso se atentar em uma competição justa e concluir que todos os competidores chegem ao destino final, evitando acidentes como afogamentos. Situação não diferente nas praias, embora os bombeiros possuam torres para a visibilidade da praia, não conseguem atuar com precisão em situações de relatos de desaparecimentos de banhistas. Sendo que, o banhista pode estar sendo realmente arrastado pela correnteza, ou apenas pode ter ido ao banheiro.  

O objetivo geral do projeto, foi solicitado através do corpo de bombeiros, o qual visa resgatar pessoas de situações de afogamento. Utilizando de um drone semi-autônomo, com câmeras 4k e térmicas, juntamente com a inteligência artificial para o auxílio do reconhecimento de pessoas no ambiente aquático. Tornando mais fácil, seguro e preciso o resgate e trabalho do corpo de bombeiros. 


   * Nosso Minimo produto viável(MVP) é a entrega de um drone com sistema embarcado capaz de enviar dados de imagem(.jpg) e vídeo(.h264) para um dispositivo secundário via wifi, esse dispositivo possuirá nossa IA capaz de processar as imagens e vídeos, e apresenta-los aos socorristas.
  
   * Principais entrgas do projeto: Indentificar pessoas utilizando IA; Transferir dados drone e sistema e Salvar gravações (Banco de Dados).

   * Sucesso ou fracasso do projeto. O projeto pode ser considerado um sucesso caso atenda as exigências citadas acima de forma autônoma. Podemos considerar um fracasso caso uma das bases não sejam concluidas nem por meios manuais.

   * ***Criterios de aceitação do produto serão definidos quando o projeto for apresentado aos socorristas.***

|__Função__|_Nome_|**_Responsabilidade_**|**_Competências_**|
|---|---|---|---|
|Documentação e Comunicação entre máquinas|Gabriela|Organizar os documentos compartilhados entre a equipe, documentar no artigo o que foi feito e enviar arquivos para o servidor/maáquina para analize utilizando a IA|Normas ABNT, Conhecimento Liguagem Culta e Redes |
|Assuntos técnicos específicos|Guilherme|Fazer o drone voar, compatibilizar camera termica e configurar biblioteca de funções ROS| Ros, e Robótica|
|Treinamento IA|Jhully|Fazer as notações necessérias nas imagens disponibilizadas e posteriormente utiliza-las para o treinamento da IA em função do reconhecimento de pessoas submersas na água.| Yolo|
|Treinamento IA|Kimberly|Fazer as notações necessérias nas imagens disponibilizadas e posteriormente utiliza-las para o treinamento da IA em função do reconhecimento de pessoas submersas na água.| Yolo|
|Configurações das Máquinas|Rafael|Tornar possível a conectividade entre maquinas, instalar bibliotecas necessarias para compatibilidade de: Cameras e servidores(conexão ao servidor)|Conhecimento de SO, Configuração via Terminal e Redes|

## Matriz de Risco

| __Risco 1__ |
| --- |
| __Importância:__ Alta. |
| __Descrição:__ Falta de tempo para treinar IA. |
| __Efeito no Projeto:__ Atraso no desenvolvimento. |
| __Probabilidade:__ Média. |
| __Impacto:__ Alto. |
| Ação: Mitigar: Extender o prazo de entrega dentro do cronograma previsto. |


| __Risco 2__ |
| --- |
| __Importância:__ Média. |
| __Descrição:__ Queima da Placa Raspberry. |
| __Efeito no Projeto:__ Atraso no projeto. |
| __Probabilidade:__ Média. |
| __Impacto:__ Alta. |
| Ação: Mitigar: Buscar outra placa e oferecer proteção adequada. |


| __Risco 3__ |
| --- |
| __Importância:__ Alta. |
| __Descrição:__ Falha na identificação de pessoas com câmera térmica. |
| __Efeito no Projeto:__ Não entrega da primeira proposta. |
| __Probabilidade:__ Baixa. |
| __Impacto:__ Alto. |
| Ação: Eliminar: Tirar a câmera térmica e finalizar com a câmera digital. |


| __Risco 4__ |
| --- |
| __Importância:__ Alta. |
| __Descrição:__ Instabilidade nes redes wifi. |
| __Efeito no Projeto:__ Entrega parcial da proposta. |
| __Probabilidade:__ Baixa. | 
| __Impacto:__ Alto. |
| Ação: Mitigar: Extender o prazo de entrega prevista no cronograma para concerto do problema. |


| __Risco 5__ |
| --- |
| __Importância:__ Media. |
| __Descrição:__ Não concluir em tempo hábil. |
| __Efeito no Projeto:__ Não conclusão do projeto. |
| __Probabilidade:__ Baixa. |
| __Impacto:__ Alto. |
| Ação: Mitigar: Dividir as tarefas em tarefas menores e redistribuição de tarefas. |

## Organização do Projeto

Estamos organizando nosso cronograma pelo Trello

Cronograma no Trello https://trello.com/b/0hzw7z82/atividades

   **Rafael Oliveira e Gabriela Grigoleto:** Responsáveis pela conexão Drone-Rede Neural e desenvolvimento de um banco de dados.

   **Kimberly Rotman e Jhully Ferreira:** Criação, desenvolvimento e treinamento da rede neural com a utilização da técnica YOLO

[Cronograma -  TCC.pdf](https://github.com/Rafael-121/Rafael-121/files/11916023/Cronograma.-.TCC.pdf)


## Ferramentas e Resultados

Resultados esperados com o projeto desenvolvido;

Seguindo o que foi apresentado, espera-se tornar possível fazer o reconhecimento de uma pessoa em ambiente aquático utilizando imagens capturadas pelo drone e processadas com o auxílio do treinamento da rede neural YOLOv8. Bem como uma conexão estabelecida entre a ferramenta Raspberry e a estação base por uma antena WI-FI, para assim, transmitir as imagens captadas em tempo real. Utilizaremos:

 __Software__ - Python nos compiladores: Google colaboratory e Visual studio. YOLO como técnica e também o conjunto de biblioteca ROS para acompanhar a atividade do drone.

__Hardware__ - Um drone e um controle, um microcomputador(Raspberry Pi) acoplado ao mesmo e este fará a conectividade wifi com uma estação que contará com um computador mais potente para processar imagens fornecidas pela câmera do drone usando IA.

### Requisitos do projeto e Diagramas

[Requisitos do projeto - drone de resgate.pdf](https://github.com/Rafael-121/Rafael-121/files/11962295/Requisitos.do.projeto.-.drone.de.resgate.pdf)

![Drone de resgte_](https://github.com/Rafael-121/Rafael-121/assets/137511020/7eebe1b4-e629-426b-83d6-12aa763c6d03)

![DIAGRAMA DE FERRAMENTAS ](https://github.com/Rafael-121/Rafael-121/assets/137511020/4dcc0f06-4aa4-45c5-b56c-1fc4c807c7a4)

<!---
Rafael-121/Rafael-121 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
