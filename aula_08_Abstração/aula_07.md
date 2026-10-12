### Abstração
É a prática de ignorar o irrelevante e focar-se estritamente no essencial.  
Existe a abstração de dados, que acontece quando ignoramos informações desnecessárias  
para o escopo do projeto.  
Existe a abstração de processos, quando não precisamos saber como um método faz seu trabalho,  
apenas sabe que ele existe pela interface.  
Uma classe abstrata nunca será instanciada, já que ela será usada apenas como base para as  
subclasses.  
Ao definir um conjunto de métodos abstratos, dizemos que estamos criando a interface pública  
da classe.  
Uma classe abstrata pode ter métodos abstratos que deverão ser obrigatoriamente implementados nas  
subclasses.  
Mas uma classe abstrata pode ter métodos concretos se eles funcionarem da mesma maneira para todas  
as subclasses (DRY).

### Principais vantagens:

* Maior legibilidade
* Padronização
* Simplificação
* Segurança
