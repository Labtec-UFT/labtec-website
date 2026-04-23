# Labtec Website

O **Labtec Website** é a plataforma oficial do Laboratório de Tecnologias Computacionais (Labtec) da UFT. O sistema foi desenvolvido para centralizar informações institucionais, projetos, publicações, serviços e comunicação, oferecendo uma experiência completa para visitantes e administração do laboratório.

---

## Objetivos do Projeto

* Apresentar o laboratório de forma institucional.
* Exibir projetos ativos e concluídos com detalhes completos.
* Disponibilizar notícias e publicações para manter visitantes atualizados.
* Permitir solicitação de serviços e orçamentos automatizados.
* Facilitar o contato direto entre visitantes e a equipe do laboratório.
* Prover área administrativa completa para gerenciamento de conteúdo e métricas.

---

## Stack Tecnológica

- **Backend:** Django 6.0.2 + Django REST Framework 3.16.1
- **Frontend:** React + Vite
- **Banco de Dados:** SQlite e MariaDB

**Outras Ferramentas:** Axios, Three.js, JWT e SMTP

---

## Funcionalidades

### Para Visitantes

* Página Inicial: visão geral do Labtec e navegação rápida.
* Quem Somos & Nossa Missão: identidade institucional e propósito do laboratório.
* Estrutura do Laboratório: visualização de infraestrutura física e tecnológica.
* Equipe: apresentação dos membros do laboratório.
* Liga AutoLab: divulgação e informações sobre participação.
* Listagem de Projetos e Projeto Individual: detalhes e objetivos de cada iniciativa.
* Notícias: listagem e leitura completa.
* Modelos 3D: visualização e informações técnicas.
* Serviços e Orçamentos: solicitação de serviços e envio de orçamento.
* Contato: envio de mensagens ao laboratório.
* Termos de Uso: informações sobre regras do site.

### Para Administradores

* Login seguro e dashboard com métricas gerais.
* CRUD completo de Notícias, Projetos e Modelos 3D.
* Upload e organização de arquivos e mídia.
* Configurações gerais do sistema.
* Registro de logs básicos e estatísticas.
---

## Estrutura de Desenvolvimento

### Backend

* API REST estruturada e escalável.
* Autenticação via JWT ou sessão do Django Admin.
* Models principais: `User`, `Project`, `News`, `3DModel`, `ServiceRequest`.
* Validações de dados e envio de e-mails automáticos.

### Frontend

* SPA em React com roteamento protegido.
* Consumo de API via Axios.
* Componentização modular e responsiva.
* Integração com visualizador 3D para modelos técnicos.

---

## Metodologia

* Desenvolvimento ágil baseado em **sprints**, com backlog priorizado.
* Gestão visual através de **Kanban** para acompanhamento de tarefas.
* Revisões de sprint e entregas incrementais, do setup inicial ao deploy em produção.

**Resumo das Sprints:**

1. Estrutura Base + Autenticação
2. CRUD de Projetos e Notícias
3. Modelos 3D e Uploads
4. Serviços e Contato
5. Dashboard e Estatísticas
6. Qualidade, Segurança e Deploy

---

## Equipe

### Orientação do Projeto

**Prof. Warley Gramacho** – Professor Orientador

* Orientação do projeto e acompanhamento do progresso geral.

### Gestão e Arquitetura

**[Luís Gustavo Alves Bezerra](https://github.com/lu1zss)**
* Planejamento e organização de sprints, arquitetura e desenvolvimento de funcionalidades.

### Equipe de Desenvolvimento

**[Tarciso Filho](https://github.com/tarcisof)**
<br>

* Responsável pela implementação de funcionalidades, integração backend/frontend e manutenção do sistema.

---

## Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/Labtec-UFT/labtec-website.git
```

2. Configure o ambiente backend (Django + PostgreSQL)

3. Configure o ambiente frontend (React + Vite)

4. Configure variáveis de ambiente (.env)

5. Instale as dependências do projeto:
```bash
# Você precisara do PIP
  pip install -r requirements.txt
```

6. Execute os servidores:

```bash
# Backend
python manage.py runserver

# Frontend
cd .\frontend
npm install
npm run dev
```

## **Instruções para Produção**

Para preparar a aplicação para execução em ambiente de produção, siga os passos abaixo no diretório raiz do projeto:

### **1. Instalar as dependências do projeto**

Execute o comando abaixo para instalar todas as bibliotecas necessárias definidas no arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

### **2. Aplicar as migrações do banco de dados**

Após instalar as dependências, execute as migrações para criar e atualizar a estrutura do banco de dados:

```
python manage.py migrate
```

### **3. Coletar os arquivos estáticos**

Por fim, execute o comando abaixo para reunir todos os arquivos estáticos da aplicação (CSS, JavaScript, imagens, etc.) em uma única pasta de produção:

```
python manage.py collectstatic
```

Esse processo é necessário para que os arquivos estáticos sejam servidos corretamente em ambiente de produção.

### **Observação**

Antes de executar esses comandos, verifique se as variáveis de ambiente necessárias estão configuradas corretamente, especialmente as relacionadas ao banco de dados, chave secreta da aplicação e configurações de debug.

As variáveis de ambiente da aplicação devem ser definidas em um arquivo `.env`, localizado na raiz do projeto. Esse arquivo contém informações sensíveis e deve ser mantido em segurança, com acesso restrito apenas à aplicação e aos responsáveis pela infraestrutura.

É importante adotar medidas de segurança adequadas para garantir o acesso seguro a esse arquivo em ambiente de produção, protegendo dados sensíveis e evitando exposição indevida das configurações da aplicação.



## Links Úteis

* GitHub: [github.com/Labtec-UFT/labtec-website](https://github.com/Labtec-UFT/labtec-website)

