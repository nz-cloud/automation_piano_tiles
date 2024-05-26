# Olá a todos!

# PyAutoGUI = Automation Piano Tiles

Confira esse script no qual eu realizei em Python que utiliza PyAutoGUI para clicar automaticamente em posições específicas da tela com base na cor do pixel.


## Descrição

O script monitora a cor de pixels em posições pré-definidas na tela e realiza cliques automáticos quando esses pixels são pretos (RGB: 0, 0, 0). É útil para automação de tarefas que dependem de mudanças visuais na tela.


## Pré-requisitos

- Python 3.12.1
- Bibliotecas Python: `pyautogui`, `keyboard`, `pywin32`


## Instalação

1. Clone meu repositório:
    ```bash
    git clone https://github.com/nz-cloud/automation_piano_tile.git
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

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
