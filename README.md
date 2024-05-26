# Olá a todos!


# Piano Tiles Automation

O projeto no qual eu realizei consiste em um script de automação para o jogo Piano Tiles. O script usa as bibliotecas `pyautogui`, `keyboard`, `win32api`, e `win32con` para detectar pixels específicos na tela e simular cliques do mouse, permitindo que o jogo seja jogado automaticamente.

Caso queira conferir pode acessar o Piano Tiles nesse [link](https://www.agame.com/game/magic-piano-tiles#theatermode). Te garato que não irá se arrepender, é muito Fantástico!

## Como Funciona

O script monitora quatro posições específicas na tela, cada uma representando uma "tecla" no Piano Tiles. Se a cor do pixel em qualquer uma dessas posições for preta (RGB: (0, 0, 0)), o script simula um clique do mouse naquela posição.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `pyautogui`
- `keyboard`
- `win32api`
- `win32con`


## Instalação

1. Clone meu repositório:
    ```bash
    git clone https://github.com/nz-cloud/automation_piano_tiles.git
    ```

2. Instale as dependências:
    ```bash
    pip install pyautogui keyboard pywin32
    ```

    
## Uso

1. Execute o script:
    ```bash
    python main.py
    ```

2. O script começará a monitorar as posições dos pixels. Para parar o script, pressione a tecla `q`.


## Contribuição

Se você quiser contribuir com o meu projeto, sinta-se à vontade para fazer um fork, criar uma nova branch e enviar um pull request com suas melhorias.

1. Faça um fork do projeto.

2. Crie uma branch para sua feature:
    ```bash
    git checkout -b new-feature
    ```
3. Faça commit das suas alterações:
    ```bash
    git commit -m 'Adiciona minha new-feature'
    ```
4. Envie para o branch principal:
    ```bash
    git push origin new-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.
