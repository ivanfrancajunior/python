'''

# Ambientes virtuais em Python (venv)

Um ambiente virtual carrega toda a sua instalação do Python para uma pasta no caminho escolhido.

    # Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.

    # venv é o módulo que vamos usar para criar ambientes virtuais.

    # Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:

    # venv env .venv .env

'''

**iniciando ambiente:**

```cmd
python -m venv .venv
```

### Extrutura de pastas

'''

    venv/
    │
    ├── bin/            # Contém scripts executáveis (como python, pip, etc.) específicos para o ambiente virtual.
    │
    ├── include/        # Contém arquivos de cabeçalho (headers) para a instalação de extensões Python.
    │
    ├── lib/            # Contém as bibliotecas (libs) necessárias para a execução das extensões Python.
    │
    └── lib64/          # (Opcional) Uma alternativa ao diretório "lib", usado em sistemas de 64 bits.

'''

**bin/:** Este diretório contém os scripts executáveis específicos para o ambiente virtual, como o interpretador Python (python), o gerenciador de pacotes (pip), entre outros. Estes scripts são ajustados para funcionar dentro do ambiente virtual e não afetam o sistema Python global.

**include/:** Aqui ficam os arquivos de cabeçalho (headers) que são necessários para compilar e instalar extensões Python que dependem de bibliotecas externas.

**lib/:** Contém as bibliotecas (libs) necessárias para a execução das extensões Python instaladas no ambiente virtual. Isso inclui tanto as bibliotecas padrão do Python quanto as bibliotecas instaladas via pip.

**lib64/:** Este é um diretório opcional, que pode ser encontrado em sistemas de 64 bits. Ele serve como uma alternativa ao diretório "lib", armazenando as bibliotecas (libs) para sistemas de 64 bits.

### Ativando o ambiente virtual:

```powershell
   <!-- path_venv\Scripts\activate -->

   python .\.venv\Scripts\activate
```

### Desativando o ambiente virtual:

```powershell
 deactivate
```

### Chegando path do python sendo executado:

```powershell
gcm python.exe -Syntax
<!-- path do iniciavel do python -->

output: C:\Users\Junior\Desktop\python course\.venv\Scripts\python.exe

```

### Instalação de pacotes (`pip`):

O `pip` é a ferramenta de gerenciamento de pacotes padrão para Python. Ele facilita a instalação, atualização e remoção de pacotes Python de repositórios públicos e privados.

Para instalar um pacote, você pode usar o seguinte comando no terminal:

```shell
pip install nome_do_pacote==versao_do_pacote
```

Para desinstalar um pacote, você pode usar o seguinte comando:

```shell
pip uninstall nome_do_pacote
```

### Verificando pacotes instalados

```shell
pip freeze
```

### `requirements.txt`

O arquivo `requirements.txt` é comumente usado em projetos Python para listar todas as dependências necessárias do projeto, facilitando assim a instalação de todas as bibliotecas requeridas de uma vez só.

**Funcionalidade:**
Listagem de Dependências: No arquivo requirements.txt, você lista todas as bibliotecas Python que seu projeto depende, uma por linha.

Versões de Dependências: Você também pode especificar as versões exatas ou faixas de versões das bibliotecas que seu projeto requer. Isso garante que outras pessoas que trabalham no projeto instalem as mesmas versões das bibliotecas para evitar conflitos de versões.

O arquivo requirements.txt é comumente usado em projetos Python para listar todas as dependências necessárias do projeto, facilitando assim a instalação de todas as bibliotecas requeridas de uma vez só.

```shell 
    
    requests==2.26.0
    flask>=2.0.0
    numpy~=1.21.0
```
#### Uso do requirements.txt:

**Gerando Arquivo de Instalação de Dependências:** Para gerar o arquivo requirements.txt a partir do ambiente atual do seu projeto Python, você pode usar o seguinte comando:

```shell
pip freeze > requirements.txt
```
Este comando irá listar todas as bibliotecas instaladas no ambiente atual junto com suas versões exatas e gravá-las no arquivo requirements.txt. Isso é útil para capturar todas as dependências do seu projeto de uma só vez, tornando mais fácil para outros desenvolvedores ou máquinas reproduzirem o mesmo ambiente de desenvolvimento.

**Instalação de Dependências:** Outros desenvolvedores ou máquinas podem instalar todas as dependências listadas no arquivo requirements.txt usando o comando: 

```shell
pip install -r requirements.txt
```

**Ambientes Virtuais**: O requirements.txt é comumente usado em conjunto com ambientes virtuais (venv) para garantir que cada projeto tenha suas próprias dependências isoladas.

**Integração Contínua**: Em práticas de integração contínua, o requirements.txt é frequentemente usado para especificar as dependências necessárias para construir e testar um projeto automaticamente.

O uso do requirements.txt é uma prática recomendada para gerenciar as dependências de projetos Python de forma eficiente e consistente. Isso ajuda a garantir que o ambiente de desenvolvimento seja reproduzível e que outras pessoas possam configurar facilmente o ambiente de desenvolvimento.


