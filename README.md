# Grupo ATTOS - G6

**Integrantes do grupo - CC:**
- Julia Felix
- Matheus Roberto
- Talita Daniele  
- Victor Guilherme 
- Vitória Régia
  
**Integrantes do grupo - Design:**
- Arthur Batista
- Charles Araújo
- Gabrielle Siqueira
- Giovanna Gondim
- Luiza Lins
- Luiza Moreira

## Requisitos SR1

### Histórias do usuário

**1. Como uma ONG, eu gostaria de ter um espaço reservado para mostrar minhas informações.(Nome da ONG, email, telefone de contato, endereço e fundação)**
- Cenários de aceitação:
  
  - Cenário: Deve adicionar informações na página.
    
      **Dado que** a ONG não tem suas informações de e-mail, ano de fundação e endereço na página

      **Quando** quando o responsável pela ONG inserir esses dados na página de perfil
    
      **Então** o sistema mostrará na página da ONG essas informações


**2. Como uma ONG, eu gostaria de ter um campo para colocar uma breve descrição sobre meu trabalho**
- Cenários de aceitação:
  - Cenário: Deve adicionar uma descrição a página
    
  	**Dado que** a plataforma possui um campo para descrição da ONG.
    
  	**Quando**  o responsável pela ONG escrever e enviar essa descrição
    
  	**Então** o sistem a mostrará na página correspondente a ONG


**3. Como uma ONG, eu gostaria de inserir na minha página o link para meu perfil no instagram.**
- Cenários de aceitação:
  - Cenário: Deve adicionar um link do Instagram.
  
    **Dado que** a Ong não possuía nenhuma rede social cadastrada
    
    **Quando** for inserida no sistema, com o nome e link
    
    **Então** a ONG terá uma rede social cadastrada

  
**4. Como uma ONG, gostaria de adicionar fotos à minha página.**
- Cenários de aceitação:
  - Cenário: Deve remover uma foto da página

    
    **Dado que** a ONG tenha cinco fotos adicionada na página
    
    **Quando** a ONG selecionar apenas uma foto para removê-lá
    
    **Então** a página deve conter quatro fotos


**5. Como ONG que possui uma página, gostaria de editar as informações que já foram inseridas.**
- Cenários de aceitação:
  - Cenário: Deve alterar informações da página
    
      **Dado que** possuo um site
    
      **Quando** eu fizer alterações em qualquer seção do site e clicar em “Salvar alterações”
    
      **Então** as alterações devem ser refletidas imediatamente no site público

### Histórias implementadas para o SR1

1- Como uma ONG, eu gostaria de ter um espaço reservado para mostrar minhas informações.(Nome da ONG, email, telefone de contato, endereço e fundação)

3. Como uma ONG, eu gostaria de inserir na minha página o link para meu perfil no instagram.

### Protótipo de baixa fidelidade

https://www.figma.com/file/eKETbfkDCNHzvM7OyACGbp/Wireframe?type=design&node-id=0%3A1&mode=design&t=IwqEGvG4eMyYerJf-1

### Screencast Protótipo de Baixa Fidelidade
[https://drive.google.com/file/d/1KoaUvc6jR0fqAHj-TKX7utW-RnOsRQeD/view?usp=drive_link](https://drive.google.com/file/d/1KoaUvc6jR0fqAHj-TKX7utW-RnOsRQeD/view?usp=sharing)

### Diagrama de atividades

https://drive.google.com/file/d/1UTOd5p0q6E0jcMnwi_I_FqzYtx_WNoEp/view?usp=sharing

### Issue/bug tracker

![image](https://github.com/mateusioliveira/projetos-attos/assets/98843736/e8a7bff1-53fd-4e12-a08c-fc7a6a2711bf)

![image](https://github.com/mateusioliveira/projetos-attos/assets/98843736/a4bafee4-d3a7-4393-a9d2-0bfe07914d2c)

### Deployment na Azure

https://project-attos.azurewebsites.net/

### Screencast Deployment
https://drive.google.com/file/d/1AF14gEdJD4Bnf-GVM9LZ-9enWJUW0c6i/view?usp=sharing

### Relato programação em pares

https://docs.google.com/document/d/1PhdnrsMWYIwlh3XZIB1KhjPRZmlufF1EG-vm1H_GWdE/edit?usp=sharing



## Requisitos SR2

### Historias implementadas para o SR2

**6. Como um doador, eu gostaria de deixar um feedback na página da ONG.**
- Cenários de aceitação:
  - Cenário: Deve alterar informações da página
        **Dado que** o sistema possui um campo para os doadores escreverem comentarios sobre a ONG e eu sou um doador
  
  	**Quando** escrevo e envio o meu comentário sobre a ONG
  
 	**Então** o sistema o mostrará na página da ONG

**7. Como uma ONG, eu gostaria de mostrar o quantitativo de doadores na minha página**
- Cenários de aceitação:
  - Cenário: Deve mostrar quantos doadores a ONG tem
        **Dado que** o sistema possui um campo para os doadores escreverem comentarios sobre a ONG e eu sou um doador
  
  	**Quando** escrevo e envio o meu comentário sobre a ONG
  
 	**Então** o sistema o mostrará na página da ONG
    
**8. Como um doador, eu gostaria de saber a última vez que os dados da página da ONG foram atualizados**
- Cenários de aceitação:
  - Cenário: Deve mostrar a data e hora da última modificação
        **Dado que** o sistema possui um campo de descrição da ONG
  
  	**Quando** o responsável pela ONG escreve o texto sobre a ONG e é enviado
  
 	**Então**  a data e a hora da última modificação será atualizada para o momento em que o texto foi enviado.


**9.  Como uma ONG, eu gostaria de mostrar a minha meta anual de arrecadações no meu site.**
- Cenários de aceitação:
  - Cenário: Deve mostrar a meta anual
        **Dado que** possuo uma meta de R$5000 
  
  	**Quando** atualizo o valor da meta para R$10000
  
 	**Então** a meta será de R$10000


**10. Como uma ONG, eu gostaria de mostrar o quantitativo de valor doado até o momento no meu site.**
- Cenários de aceitação:
  - Cenário: Deve mostrar a meta anual
        **Dado que** possuo registrado um total de R$2000,00 doados 
  
  	**Quando** adiciono R$ 500,00 ao valor doado
  
 	**Então** terei R$2500,00 de valor doado

### Histórias implementadas para o SR1

2. Como uma ong eu gostaria de ter um campo para colocar uma breve descrição sobre meu trabalho 
4. Como uma ONG, gostaria de adicionar fotos à minha página. 
5. Como ONG que possui uma página, gostaria de editar as informações que já foram inseridas.
6. Como um doador, eu gostaria de deixar um feedback na página da ONG.
7. Como uma ONG, eu gostaria de mostrar o quantitativo de doadores na minha página
8. Como um doador, eu gostaria de saber a última vez que os dados da página foram atualizados
9. Como uma ONG, eu gostaria de mostrar a minha meta anual de arrecadações no meu site
10.Como uma ONG, eu gostaria de mostrar o quantitativo de valor doado até o momento no meu site.


## Protótipo de média fidelidade

https://www.figma.com/file/VllWFhJIAQV6TzRIa1zPhw/Prot%C3%B3tipo-de-m%C3%A9dia---CC?type=design&node-id=0-1&mode=design&t=mOGLEIJJtjWovJXZ-0


### Screencast Protótipo de Média Fidelidade
[https://drive.google.com/drive/u/0/my-drive](https://drive.google.com/file/d/1ov7oh05v8JqX-2APfJ1V4SkzSixINrj3/view?usp=sharing)


## Issue/Bug traclker atualizado:

![image](https://github.com/mateusioliveira/projetos-attos/assets/98843736/b05abe80-05f9-4183-ba2e-7d016c30cc35)

![image](https://github.com/mateusioliveira/projetos-attos/assets/98843736/dfe0e015-8dbc-4eb1-919b-70c0fc6bf83c)

### Deployment na Azure

https://project-attos.azurewebsites.net/

### Screencast Deployment



### Relato programação em pares

https://docs.google.com/document/d/1PhdnrsMWYIwlh3XZIB1KhjPRZmlufF1EG-vm1H_GWdE/edit?usp=sharing

### Diagrama de atividades atualizado

https://drive.google.com/file/d/1XwMnqJcUUv4eSq_qNaMpiyXQToLnvK8k/view?usp=sharing

### Screencast pipeline CI/CD

https://drive.google.com/file/d/19G7EadCbJOBxQWCdgNVGVM4YzTyC3bM_/view?usp=sharing

### Sreencast testes do selenium

https://drive.google.com/file/d/1VdPaY9oc4C5GcVZt71P9VHmyMvei4Edf/view?usp=sharing

