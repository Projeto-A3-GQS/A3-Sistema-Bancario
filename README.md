# 🏦 Sistema Bancário –> Projeto A3 (Refatoração + Clean Code)

Este repositório contém o desenvolvimento do **Projeto A3 Sistema Bancário**, focado na prática de refatoração, Clean Code, modularização, boas práticas de POO e testes unitários utilizando Python.

---

## 📌 Objetivos do Trabalho

- ✔ Identificar deficiências estruturais no código original  
- ✔ Refatorar o sistema utilizando princípios de Clean Code  
- ✔ Modularizar o projeto para melhorar manutenção e legibilidade  
- ✔ Implementar testes unitários para as principais funcionalidades  
- ✔ Documentar contribuições individuais de cada membro via commits  
- ✔ Entregar relatório técnico e código em repositório público  

---

## 📂 Estrutura do Projeto

<img width="255" height="444" alt="image" src="https://github.com/user-attachments/assets/2fecfd16-a207-4892-9c3f-bbeed92d5b99" />

---

## 🧠 Tecnologias Utilizadas

- Python **3.10+**
- **Pytest** para testes unitários
- **POO** (Programação Orientada a Objetos)
- **Clean Code**
- Estrutura modular em **pacotes**

---

## 🚀 Funcionalidades do Sistema

- ✔ Cadastro de clientes  
- ✔ Criação e gerenciamento de contas bancárias  
- ✔ Operações de depósito  
- ✔ Operações de saque com regras de limite  
- ✔ Registro de histórico de transações  
- ✔ Interface simples via **CLI**  

---

## 🛠 Refatorações Realizadas

As principais melhorias aplicadas ao código incluem:

### 🔸 Modularização completa
- Separação do código em pacotes **dominio**, **operacoes** e **app**  
- Isolamento de responsabilidades em arquivos independentes  

### 🔸 Encapsulamento e limpeza do código
- Uso de `@property`  
- Atributos privados  
- Type hints em todas as classes  

### 🔸 Reestruturação das operações bancárias
- Criação da classe abstrata **Transacao**  
- Operações especializadas (**Saque**, **Deposito**)  
- Registro seguro em **Historico**  

### 🔸 Separação entre domínio e interface
- `cli.py` concentra apenas a interação com o usuário  
- Regras de negócio mantidas no domínio e nas operações  

### 🔸 Testes unitários completos
- Cobertura de **Conta**, **Cliente**, **Saque**, **Depósito**, **Histórico** e **Conta Corrente**
