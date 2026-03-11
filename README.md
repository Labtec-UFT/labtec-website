# Labtec Website

O **Labtec Website** é a plataforma oficial do Laboratório de Tecnologias Computacionais (Labtec) da UFT. O sistema foi desenvolvido para centralizar informações institucionais, projetos, publicações, serviços e comunicação, oferecendo uma experiência completa para visitantes e administração do laboratório.

---

## Objetivos do Projeto

* Apresentar o laboratório de forma institucional e confiável.
* Exibir projetos ativos e concluídos com detalhes completos.
* Disponibilizar notícias e publicações para manter visitantes atualizados.
* Permitir solicitação de serviços e orçamentos automatizados.
* Facilitar o contato direto entre visitantes e a equipe do laboratório.
* Prover área administrativa completa para gerenciamento de conteúdo e métricas.

---

## Stack Tecnológica

- **Backend:** Django 5.2.3 + Django REST Framework
- **Frontend:** React + Vite
- **Banco de Dados:** PostgreSQL

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

### Coordenação e Apoio Institucional

**Prof. Warley Gramacho** – Coordenador Institucional

* Direcionamento estratégico e alinhamento entre equipe e laboratório.

### Gestão e Arquitetura

**[Luís Gustavo Alves Bezerra](https://github.com/lu1zss)** – Gerente de Projeto & Desenvolvedor
* Planejamento e organização de sprints, arquitetura e desenvolvimento de funcionalidades.

### Desenvolvimento

**[Tarciso Filho](https://github.com/)** – Desenvolvedor
<br>
**[Guilherme Araújo](https://github.com/)** – Desenvolvedor
<br>
**[Ricardo](https://github.com/)** – Desenvolvedor

* Responsáveis pela implementação de funcionalidades, integração backend/frontend e manutenção do sistema.

---
### Ambiente virtual (`venv`) no Python

Um **ambiente virtual (`venv`)** cria um espaço isolado dentro do projeto para instalar dependências.  
Isso evita conflitos entre bibliotecas de diferentes projetos e mantém o ambiente organizado.

---

**Como criar o ambiente:**

```bash
cd labtec-website
python -m venv venv
```

**Ativar o ambiente:**
```bash
# PowerShell
.\venv\Scripts\Activate
```

```bash
# Linux
source venv/bin/activate
```
#### Após ativar, o terminal exibirá algo semelhante a:
(venv) C:\labtec-website>

---

### Como Rodar Localmente
1. Clone o repositório:

```bash
git clone https://github.com/Labtec-UFT/labtec-website.git
```

2. Configure o ambiente backend (Django + PostgreSQL).
- Depois de ter criado a (`env`) você precisa rodar o comando:
```
    (venv) C:\labtec-website> pip install -m requirements.txt
```

3. Configure o ambiente frontend (React + Vite).

4. Configure variáveis de ambiente (DB, JWT, SMTP, etc.) - Disponível no grupo de comunicações, modelo base na .env-example

5. Execute os servidores:

```bash
# Backend
(venv) C:\labtec-website>
python manage.py runserver

# Frontend
cd .\frontend
npm install
npm run dev
```

## Links Úteis

* GitHub: [github.com/Labtec-UFT/labtec-website](https://github.com/Labtec-UFT/labtec-website)


