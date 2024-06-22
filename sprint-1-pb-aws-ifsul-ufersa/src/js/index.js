let numeroRandomico = ''
let numerosDigitados = []
let maxTentativas = 12
let tentativas = 0

function novoJogo(){
    window.location.reload()
}

function atualizarTentativas(){
    document.getElementById('num').value=''
    tentativas++
    document.getElementById('tentativas').innerHTML= tentativas
}

function verDiferenca(diferenca){
    if(diferenca === 0){
        document.getElementById('span').innerHTML = "Parabéns"
        atualizarTentativas()
        document.getElementById('num').setAttribute('Readonly','Readonly')
    }else if(diferenca < 0){
        if(diferenca > -1000){
            document.getElementById('span').innerHTML = "Digite um número maior que o anterior"
            atualizarTentativas()
        }else{
            document.getElementById('span').innerHTML = "Digite um número muito maior que o anterior"
            atualizarTentativas()
        }
    }else{
        if(diferenca < 1000){
            document.getElementById('span').innerHTML = "Digite um número menor que o anterior"
            atualizarTentativas()
        }else{
            document.getElementById('span').innerHTML = "Digite um número muito menor que o anterior"
            atualizarTentativas()
        }

    }
}


function init() {
    const numero = [4, 6, 8][Math.floor(Math.random() * 3)];
    for (let i = 0; i < numero; i++) {
        numeroRandomico += Math.floor(Math.random() * 10);
    }
    console.log('numeroRandomico: ' + numeroRandomico);
}

function lancarExcessao(numeroDigitado){
    try{
        if( numeroDigitado.toString().length < 4 ){
            document.getElementById('num').value=''
            document.getElementById('span').innerHTML = 'Insira um número de no mínimo quatro dígitos'
            throw new Error("Insira um número de no mínimo quatro dígitos")
        }else if(!Number.isInteger(Number(numeroDigitado))){
            document.getElementById('num').value=''
            document.getElementById('span').innerHTML = 'O número não deve ter casas decimais'
            throw new Error("O número não deve ter casas decimais")
        }else{
            numerosDigitados.push(' ' + numeroDigitado)
            document.getElementById('guesses').innerHTML = numerosDigitados
            if(tentativas < maxTentativas){
                let diferenca = numeroDigitado - numeroRandomico
                verDiferenca(diferenca)
            }else{
                document.getElementById('span').innerHTML = 'Número de tentativas ultrapassadas'
                document.getElementById('num').value=''
                document.getElementById('num').setAttribute('Readonly','Readonly')

            }
        }}
     catch (error) {

        console.error("Mensagem de erro: " + error.message);
    }
}

function compararNumeros(){
    const numeroDigitado = Number(document.getElementById('num').value)
    lancarExcessao(numeroDigitado)
}

