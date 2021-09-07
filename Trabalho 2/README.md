# 2° Trabalho - Laboratório de Expirementação de Software

## Um Estudo das Características de Qualidade de Sistemas Java 
---

## Autores

**Arthur Rocha Amaral**

**Guilherme Oliveira Antônio**

---

## Objetivo

O objetivo deste laboratório é analisar aspectos da qualidade de repositórios desenvolvidos na linguagem Java, correlacionado-os com características do seu processo de desenvolvimento, sob a perspectiva de métricas de produto calculadas através da ferramenta [CK](https://github.com/mauricioaniche/ck).

---

## Como testar

- Rodar comando para inciar ambiente virtual e acessa-lo.
- 
    ``python3 - venv .venv``
    
    ``source .venv/bin/activate``

- Instalar bibliotecas usadas.

    ``python -m pip install -r requirements.txt``

- Para rodar o script

    ``python scripts/<SCRIPT_NAME> --token TOKEN --should-fetch (true/false) --should-analyse (true/false)``

***Obs.:*** é necessário ter um [Personal access tokens](https://docs.github.com/pt/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
 do github. Para que funcione é só colocar o token dentro do script na variavel token.
