// function contador(numero){
//     while(numero <=10){
//         console.log(numero);
//         numero +=2; // soma 2
//     }
// }

// contador(2)


//Exercicio 1

// function contagemRegressiva(numero){
//     while (numero >= 1){
//         console.log(numero)
//         numero--
//     }
// }

// const numero = Number(prompt("Digite um número:"))
// contagemRegressiva(numero)


// Exercicio 2

// let nome

// do{
//     nome = prompt("Digite seu nome:")
// } while(nome.length <=3)


// let idade
// do{
//     idade = prompt("Digite sua idade:")
// } while(idade > 0 && idade < 150)


// let salario
// do{
//     salario = parseFloat(pompt("Digite seu salário:"))
// } while(salario > 0)


// let genero
// do{
//     genero = prompt("Digite seu gênero:")
// } while(genero.toLowerCase() )




// for(contador inicial; condição; como esse contador vai mover)

    // for(let i = 0; 1 <= 10; i++){
    //     console.log(i)
    // }


// Exercício tabuada

let numero = Number(prompt("Digite um número para ver a tabuada:"))
for(let i = 0; i <=10; i++){
    console.log(`${i} x ${numero} = ${i * numero}`)
}