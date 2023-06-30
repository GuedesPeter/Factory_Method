# Factory Method - Um padrão de design para criar objetos

O Factory Method é um padrão de design creacional que fornece uma abordagem para criar objetos em uma classe base, permitindo que as subclasses decidam qual objeto concreto criar. Esse padrão promove o princípio de design "programar para uma interface, não para uma implementação" e é amplamente utilizado em muitas linguagens de programação.

## Quando usar o Factory Method?

O Factory Method é útil quando você tem uma classe base abstrata que define uma interface para criar objetos, mas deseja delegar a responsabilidade de criação para suas subclasses. Ele é útil quando:

1. Você quer desacoplar o código cliente da criação de objetos concretos, permitindo que o cliente trabalhe com a interface da classe base, em vez de depender de classes concretas.

2. Você precisa criar diferentes variantes de um objeto dentro de uma hierarquia de classes, deixando que as subclasses decidam qual objeto concreto criar.

3. Você deseja adicionar novos tipos de objetos sem modificar o código existente, seguindo o princípio do Open/Closed (aberto/fechado) do SOLID.

## Estrutura - Componentes do Factory Method

Existem geralmente quatro componentes principais no padrão Factory Method:

1. **Product (Produto)**: Define a interface dos objetos criados pelo Factory Method.

2. **ConcreteProduct (Produto Concreto)**: Implementa a interface do Produto e representa os objetos concretos que serão criados pelo Factory Method.

3. **Creator (Criador)**: Declara o método Factory Method, que retorna um objeto do tipo Produto. Pode conter implementações padrão ou concretas para criar objetos, mas também pode ser uma classe abstrata.

4. **ConcreteCreator (Criador Concreto)**: Subclasse do Criador, que implementa o Factory Method para criar objetos específicos do Produto.


# Relações com outros padrões

- Muitos projetos começam usando o Factory Method (menos complicado e mais customizável através de subclasses) e evoluem para o Abstract Factory, Prototype, ou Builder (mais flexíveis, mas mais complicados).

- Classes Abstract Factory são quase sempre baseadas em um conjunto de métodos fábrica, mas você também pode usar o Prototype para compor métodos dessas classes.

- Você pode usar o Factory Method junto com o Iterator para permitir que uma coleção de subclasses retornem diferentes tipos de iteradores que são compatíveis com as coleções.

- O Prototype não é baseado em heranças, então ele não tem os inconvenientes dela. Por outro lado, o Prototype precisa de uma inicialização complicada do objeto clonado. O Factory Method é baseado em herança mas não precisa de uma etapa de inicialização.

- O Factory Method é uma especialização do Template Method. Ao mesmo tempo, o Factory Method pode servir como uma etapa em um Template Method grande.



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
