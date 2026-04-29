// let nome = "Orion";

// console.log(nome.length);
// nome.trim();  // Mesma coisa que strip

// if(nome.length < 2){
//     alert("Digite um nome válido")
// }

// console.log(nome.toLowerCase().includes("C"));
// console.log(nome.replaceAll("a", "o"));

// console.log(Math.random()); // De 0 à 0.9999


// function saudacao(nome) {
//     return
//     alert(`"Olá! ${nome}"`)
// }

// const mensagem = saudacao(nome);

// saudacao("Bruno");


// DESAFIO 1
// let texto = prompt("Digite um texto");

// function limpar_texto(texto){
//     const texto_formatado = texto.trim().toUpperCase()
//     return texto_formatado
// }

// texto_fomatado = limpar_texto(texto)
// console.log(texto_fomatado)



// DESAFIO 2
let texto = prompt("Digite um texto");

function verificar_texto(texto) {
    texto_formatado = texto.replaceAll("a", "o").replaceAll("A", "O");

    return texto_formatado
}

texto_formatado = verificar_texto(texto)
alert(texto_formatado)