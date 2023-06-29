# Factory Method - Um padrão de design para criar objetos

O Factory Method é um padrão de design creacional que fornece uma abordagem para criar objetos em uma classe base, permitindo que as subclasses decidam qual objeto concreto criar. Esse padrão promove o princípio de design "programar para uma interface, não para uma implementação" e é amplamente utilizado em muitas linguagens de programação.

## Quando usar o Factory Method?

O Factory Method é útil quando você tem uma classe base abstrata que define uma interface para criar objetos, mas deseja delegar a responsabilidade de criação para suas subclasses. Ele é útil quando:

1. Você quer desacoplar o código cliente da criação de objetos concretos, permitindo que o cliente trabalhe com a interface da classe base, em vez de depender de classes concretas.

2. Você precisa criar diferentes variantes de um objeto dentro de uma hierarquia de classes, deixando que as subclasses decidam qual objeto concreto criar.

3. Você deseja adicionar novos tipos de objetos sem modificar o código existente, seguindo o princípio do Open/Closed (aberto/fechado) do SOLID.

## Componentes do Factory Method

Existem geralmente quatro componentes principais no padrão Factory Method:

1. **Product (Produto)**: Define a interface dos objetos criados pelo Factory Method.

2. **ConcreteProduct (Produto Concreto)**: Implementa a interface do Produto e representa os objetos concretos que serão criados pelo Factory Method.

3. **Creator (Criador)**: Declara o método Factory Method, que retorna um objeto do tipo Produto. Pode conter implementações padrão ou concretas para criar objetos, mas também pode ser uma classe abstrata.

4. **ConcreteCreator (Criador Concreto)**: Subclasse do Criador, que implementa o Factory Method para criar objetos específicos do Produto.




# Prós 
## Você evita acoplamentos firmes entre o criador e os produtos concretos.
 ## Princípio de responsabilidade única. 
 Você pode mover o código de criação do produto para um único local do programa, facilitando a manutenção do código.
 ## Princípio aberto/fechado. 
 Você pode introduzir novos tipos de produtos no programa sem quebrar o código cliente existente.
# Contras
## O código pode se tornar mais complicado.
você precisa introduzir muitas subclasses novas para implementar o padrão. 

O melhor cenário é quando você está introduzindo o padrão em uma hierarquia existente de classes criadoras.












## Colaboradores

<a href="https://github.com/ggramoss"><img src="https://github.com/ggramoss.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/GuedesPeter"><img src="https://github.com/GuedesPeter.png" width="45" height="45"></a> &nbsp;
<a href="https://github.com/TaizaReis"><img src="https://github.com/TaizaReis.png" width="45" height="45"></a> &nbsp;
