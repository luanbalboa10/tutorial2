# Tutorial 2

Este repositório é um projeto de estudo para praticar Python e os principais
recursos do Git e do GitHub.

## Sobre o projeto

O projeto contém exercícios iniciais em Python e serve como ambiente de
aprendizagem para:

- criar e organizar um repositório;
- registrar alterações com commits;
- publicar código no GitHub;
- trabalhar com branches e Pull Requests.

## Pré-requisitos

Para executar o projeto, você precisa ter instalado:

- [Python 3](https://www.python.org/downloads/);
- [Git](https://git-scm.com/downloads).

Você pode verificar as instalações no terminal:

```bash
python --version
git --version
```

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/luanbalboa10/tutorial2.git
cd tutorial2
```

2. Execute o arquivo principal:

```bash
python tutorial.py
```

O arquivo `tutorial.py` está disponível para receber os exercícios do tutorial.

## Estrutura do projeto

```text
tutorial2/
├── .gitignore
├── README.md
└── tutorial.py
```

## Como contribuir

1. Crie uma branch para sua alteração:

```bash
git switch -c minha-mudanca
```

2. Faça a alteração e revise os arquivos modificados:

```bash
git status
git diff
```

3. Adicione e confirme a alteração:

```bash
git add README.md tutorial.py
git diff --cached
git commit -m "docs: melhora o README do projeto"
```

4. Envie a branch para o GitHub:

```bash
git push -u origin minha-mudanca
```

5. No GitHub, abra um Pull Request para enviar a alteração à branch principal.

## Licença

Adicione aqui a licença escolhida para o projeto. Enquanto não houver uma
licença, considere o código disponível apenas para estudo neste repositório.

## Autor

- [luanbalboa10](https://github.com/luanbalboa10)