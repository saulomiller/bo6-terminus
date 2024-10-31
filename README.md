# bo6-terminus
 <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seleção de Valores e Cálculo de Expressões</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            width: 350px;
            padding: 20px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            text-align: center;
        }
        .selection-group {
            margin: 15px 0;
        }
        .image-option {
            margin: 5px;
            cursor: pointer;
        }
        .image-option input[type="radio"] {
            display: none;
        }
        .image-option label {
            display: inline-block;
            margin: 5px;
            padding: 2px;
            border-radius: 4px;
            border: 2px solid transparent;
        }
        .image-option input[type="radio"]:checked + label {
            border-color: #007BFF;
        }
        button {
            margin-top: 15px;
            padding: 10px;
            font-size: 1rem;
            width: 100%;
            cursor: pointer;
        }
        .reset-button {
            background-color: #FF6347;
            color: white;
            border: none;
        }
        .resultado {
            color: red;
            font-weight: bold;
        }
        .doacao {
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Seleção de Valores</h2>

    <div class="selection-group">
        <p>Escolha o valor de x:</p>
        <div class="image-option">
            <input type="radio" name="x" id="x0" value="0" checked>
            <label for="x0"><img src="0.png" alt="0" width="50" height="50"></label>
            
            <input type="radio" name="x" id="x10" value="10">
            <label for="x10"><img src="10.png" alt="10" width="50" height="50"></label>
            
            <input type="radio" name="x" id="x11" value="11">
            <label for="x11"><img src="11.png" alt="11" width="50" height="50"></label>
            
            <input type="radio" name="x" id="x20" value="20">
            <label for="x20"><img src="20.png" alt="20" width="50" height="50"></label>
            
            <input type="radio" name="x" id="x21" value="21">
            <label for="x21"><img src="21.png" alt="21" width="50" height="50"></label>
            
            <input type="radio" name="x" id="x22" value="22">
            <label for="x22"><img src="22.png" alt="22" width="50" height="50"></label>
        </div>
    </div>

    <div class="selection-group">
        <p>Escolha o valor de y:</p>
        <div class="image-option">
            <input type="radio" name="y" id="y0" value="0" checked>
            <label for="y0"><img src="0.png" alt="0" width="50" height="50"></label>
            
            <input type="radio" name="y" id="y10" value="10">
            <label for="y10"><img src="10.png" alt="10" width="50" height="50"></label>
            
            <input type="radio" name="y" id="y11" value="11">
            <label for="y11"><img src="11.png" alt="11" width="50" height="50"></label>
            
            <input type="radio" name="y" id="y20" value="20">
            <label for="y20"><img src="20.png" alt="20" width="50" height="50"></label>
            
            <input type="radio" name="y" id="y21" value="21">
            <label for="y21"><img src="21.png" alt="21" width="50" height="50"></label>
            
            <input type="radio" name="y" id="y22" value="22">
            <label for="y22"><img src="22.png" alt="22" width="50" height="50"></label>
        </div>
    </div>

    <div class="selection-group">
        <p>Escolha o valor de z:</p>
        <div class="image-option">
            <input type="radio" name="z" id="z0" value="0" checked>
            <label for="z0"><img src="0.png" alt="0" width="50" height="50"></label>
            
            <input type="radio" name="z" id="z10" value="10">
            <label for="z10"><img src="10.png" alt="10" width="50" height="50"></label>
            
            <input type="radio" name="z" id="z11" value="11">
            <label for="z11"><img src="11.png" alt="11" width="50" height="50"></label>
            
            <input type="radio" name="z" id="z20" value="20">
            <label for="z20"><img src="20.png" alt="20" width="50" height="50"></label>
            
            <input type="radio" name="z" id="z21" value="21">
            <label for="z21"><img src="21.png" alt="21" width="50" height="50"></label>
            
            <input type="radio" name="z" id="z22" value="22">
            <label for="z22"><img src="22.png" alt="22" width="50" height="50"></label>
        </div>
    </div>

    <button onclick="calcular()">Calcular</button>
    <button class="reset-button" onclick="resetar()">Resetar</button>

    <p id="resultado" class="resultado"></p>

    <div class="doacao">
        <h4>Se você deseja apoiar meus estudos, considere fazer uma doação:</h4>
        <a href="https://www.paypal.com/donate/?business=G67QYHTLRP8U2&no_recurring=0&item_name=Support+my+studies+to+become+a+software+engineer&currency_code=BRL" target="_blank">Doar</a>
    </div>

    <p style="margin-top: 20px;">by: SmR</p>
</div>

<script>
    function calcular() {
        // Obter valores selecionados para x, y, z
        const x = parseInt(document.querySelector('input[name="x"]:checked').value);
        const y = parseInt(document.querySelector('input[name="y"]:checked').value);
        const z = parseInt(document.querySelector('input[name="z"]:checked').value);

        // Calcular expressões
        const expressao1 = 2 * x + 11;
        const expressao2 = 2 * z + y - 5;
        const expressao3 = y + z - x;

        // Exibir resultados
        const resultado = `
            <span>${expressao1}</span><br>
            <span>${expressao2}</span><br>
            <span>${expressao3}</span>
        `;
        document.getElementById('resultado').innerHTML = resultado;
    }

    function resetar() {
        // Reseta os valores para os valores iniciais (0) e limpa o resultado
        document.querySelectorAll('input[type="radio"][value="0"]').forEach(input => input.checked = true);
        document.getElementById('resultado').innerHTML = "";
    }
</script>

</body>
</html>

