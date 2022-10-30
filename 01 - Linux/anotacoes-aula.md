<h1>
    <div align="center">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="50px"/>
    <a href="https://cursos.alura.com.br/course/linux-ubuntu">Curso de
Linux I: conhecendo e utilizando o terminal </a><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="50px"/>
    </div>
</h1>

## 1. 📇 Índice
- [1. 📇 Índice](#1--índice)
- [2. :bookmark_tabs:Sobre](#2-bookmark_tabssobre)
- [3. :man_technologist:Distribuição Linux utilizada](#3-man_technologistdistribuição-linux-utilizada)
- [4. Comandos Linuxs](#4-comandos-linuxs)
  - [4.1. Listnado caminho atual](#41-listnado-caminho-atual)
  - [4.2. Listando arquivos e diretórios](#42-listando-arquivos-e-diretórios)
  - [4.3. Listando a pasta](#43-listando-a-pasta)
  - [4.4. Voltando as pastas](#44-voltando-as-pastas)
  - [4.5. Limpando a tela](#45-limpando-a-tela)
  - [4.6. Redirecionando para a pasta raiz](#46-redirecionando-para-a-pasta-raiz)
  - [4.7. Removendo um diretórios vazios](#47-removendo-um-diretórios-vazios)
  - [4.8. Removendo recursivamente os arquivos](#48-removendo-recursivamente-os-arquivos)
  - [4.9. Removendo um arquivo](#49-removendo-um-arquivo)
  - [4.10. Lendo um arquivo](#410-lendo-um-arquivo)
  - [4.11. Lendo mais de um arquivo](#411-lendo-mais-de-um-arquivo)
  - [4.12. Lendo qualquer um arquivo](#412-lendo-qualquer-um-arquivo)
  - [4.13. Lendo todos arquivos txt](#413-lendo-todos-arquivos-txt)
  - [4.14. Copiando um arquivo para outro](#414-copiando-um-arquivo-para-outro)
  - [4.15. Movendo o arquivo para outra pasta](#415-movendo-o-arquivo-para-outra-pasta)
  - [4.16. Movendo o arquivo para outra pasta com um novo nome](#416-movendo-o-arquivo-para-outra-pasta-com-um-novo-nome)
  - [4.17. Copiar um diretório](#417-copiar-um-diretório)
  - [4.18. Compactando arquivos](#418-compactando-arquivos)
  - [4.19. Verificnado o que há dentro do arquivo zip](#419-verificnado-o-que-há-dentro-do-arquivo-zip)
  - [4.20. Descompactando arquivos arquivos zip sem exibir logs](#420-descompactando-arquivos-arquivos-zip-sem-exibir-logs)
  - [4.21. Empacotando e zipando com tar](#421-empacotando-e-zipando-com-tar)
  - [4.22. Descompactando o tar zipado](#422-descompactando-o-tar-zipado)
  - [4.23. Encostando no arquivo sem modificar](#423-encostando-no-arquivo-sem-modificar)
  - [4.24. Head](#424-head)
  - [4.25. Tail](#425-tail)
  - [4.26. Less](#426-less)
- [5. Editor Vi](#5-editor-vi)
  - [5.1. Abrindo editor vi](#51-abrindo-editor-vi)
  - [5.2. Tabela de comandos no editor vi](#52-tabela-de-comandos-no-editor-vi)


---
## 2. :bookmark_tabs:Sobre
Esse readme foi criado dentro do curso
<a href="https://cursos.alura.com.br/course/linux-ubuntu"><b>Linux</b></a>
com intuito de colocar em prática
todo o conteúdo estudado durante o curso.

---

## 3. :man_technologist:Distribuição Linux utilizada

- [<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ubuntu/ubuntu-plain.svg" height="30px"/> Ubuntu v22.04.1](https://ubuntu.com/)

---
## 4. Comandos Linuxs

### 4.1. Listnado caminho atual

```bash
pwd
```

### 4.2. Listando arquivos e diretórios

```bash
ls
ls -a
ls -la
```

### 4.3. Listando a pasta

```bash
cd .
```

### 4.4. Voltando as pastas

```bash
cd ..
```

### 4.5. Limpando a tela

```bash
clear
```

### 4.6. Redirecionando para a pasta raiz

```bash
cd
```

### 4.7. Removendo um diretórios vazios

```bash
rmdir {diretorio}
```

### 4.8. Removendo recursivamente os arquivos

```bash
rm -r {diretorio}
```

### 4.9. Removendo um arquivo

```bash
rm {nome-do-arquivo}
```

### 4.10. Lendo um arquivo

```bash
cat {arquivo1.txt}
```

### 4.11. Lendo mais de um arquivo

```bash
cat {arquivo?.txt}
```

### 4.12. Lendo qualquer um arquivo

```bash
cat {arquivo*.txt}
```

### 4.13. Lendo todos arquivos txt

```bash
cat *.txt
```

### 4.14. Copiando um arquivo para outro

```bash
cp {arquivo-a-ser-copiado} {nome-novo-arquivo}

Movendo / renomeando um arquivo
mv {nome-do-arquivo} {nome-novo-arquivo}
```

### 4.15. Movendo o arquivo para outra pasta

```bash
mv {nome-do-arquivo-a-ser-movido} {diretorio}
```

### 4.16. Movendo o arquivo para outra pasta com um novo nome

```bash
mv {nome-do-arquivo-a-ser-movido} {diretorio/novo-nome-do-arquivo}
// EXEMPLO:
mv bemvindo.txt projetos-java/arquivo.txt
```

### 4.17. Copiar um diretório

```bash
cp -r {nome-pasta} {nome-nova-pasta}

#exemplo:
cp -r projetos-java projetos-c#
```

### 4.18. Compactando arquivos

```bash
zip -r {nome-do-zip} {pasta}
#exemplo:
zip -r work.zip workspace/

#compactando sem exibir log
zip -rq {nome-do-zip} {pasta}
#exemplo:
zip -rq work.zip workspace/
```

### 4.19. Verificnado o que há dentro do arquivo zip

```bash
unzip -l {nome-do-zip}

#exemplo:
unzip -l work.zip
```

### 4.20. Descompactando arquivos arquivos zip sem exibir logs

```bash
unzip  {nome-do-zip}

#exemplo:
unzip -q work.zip
```

### 4.21. Empacotando e zipando com tar

<div align="center">
O tar, por padrão, é recursivo.

| comando | significado                  |
| ------- | ---------------------------- |
| -c      | compact                      |
| z       | zip                          |
| >       | inserir arquivo              |
| f       | nome do arquivo a ser criado |

</div>

```bash
tar -cz {arquivo-a-ser-compactado} > {nome-do-arquivo}.tar.gz

#exemplo:
tar -cz workspace > work.tar.gz

# --------

#compactando com f
tar -czf {nome}.tar.gz {pasta}

#exeplo
tar -czf work.tar.gz workspace

```
<div align="center">

| comando | significado                  |
| ------- | ---------------------------- |
| -x      | extract                      |
| <       | ler arquivo                  |
| f       | nome do arquivo a ser criado |
| -v      | verbose (apresenta log)      |

</div>

### 4.22. Descompactando o tar zipado

```bash
tar -xz < {arquivo-a-ser-compactado} > {nome-do-arquivo}.tar.gz
#exemplo:
tar -xz < work.tar.gz


#descompactando com f
tar -xzf {nome}.tar.gz
#exeplo
tar -xzf work.tar.gz

```

### 4.23. Encostando no arquivo sem modificar

O arquivo em si não altera-se, mas sua data de modificação sim.

```bash
touch {nome-do-arquivo}

#exemplo:
touch bemvindo.txt

```

### 4.24. Head

O head traz as 10 primeiras linhas por padrão

```bash
head {nome-do-arquivo}
#exemplo:
head bemvindo.txt


#Lendo somente as 3 primeiras linhas do arquivo
head -n 3 {nome-do-arquivo}
#exemplo
head -n 3 google.txt
```

### 4.25. Tail

O tail traz as 10 últimas linhas por padrão

```bash
tail {nome-do-arquivo}
#exemplo:
tail bemvindo.txt


#Lendo somente as 3 últimas linhas do arquivo
tail -n 3 {nome-do-arquivo}
#exemplo
tail -n 3 google.txt
```

### 4.26. Less

Lendo uma parte do arquivo. Pode utilizar a seta para navegar pelo arquivo

```bash
less {nome-do-arquivo}
#exemplo:
less bemvindo.txt
```

## 5. Editor Vi

### 5.1. Abrindo editor vi

```bash
vi {nome-do-arquivo}
#exemplo:
vi bemvindo.txt
```
### 5.2. Tabela de comandos no editor vi

<div align="center">
O tar, por padrão, é recursivo.

| comando          | significado                                                   |
| ---------------- | ------------------------------------------------------------- |
| i                | adicionar palavras na posição atual                           |
| a                | adicionar palavras na posição seguinte                        |
| A                | adicionar palavras no final da linha                          |
| x                | apaga caractere na posição atual                              |
| 11x              | apaga 11 caracteres seguintes                                 |
| dd               | removendo a linha por completo                                |
| esc              | voltar navegação                                              |
| :w               | Salvar (write)                                                |
| :q               | Sair (quit)                                                   |
| :wq              | Salvar e Sair (write and quit)                                |
| :q!              | Sair sem salvar                                               |
| G                | Navega até a última linha                                     |
| 1G               | Navega até a primeira linha                                   |
| 5G               | Navega até a quinta linha                                     |
| $                | Navega até o fim da linha                                     |
| 0                | Navega até o início da linha                                  |
| /{palavra-busca} | Navega até a linha que encontrou a palavra                    |
| n                | Navega até a próxima linha de ocorrência da palavra procurada |
| N                | Navega até a ocorrência anterior que encontrou a palavra      |
| yy               | copiar a linha inteira                                        |
| 3yy              | copiar 3 linhas inteiras                                      |
| p                | colar a linha inteira                                         |
| 10p              | colar 10 vezes o mesmo conteúdo                               |

</div>
