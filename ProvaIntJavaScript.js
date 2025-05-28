// Solicita ao usuário dois números
let num1 = parseFloat(prompt("Digite o primeiro número:"));
let num2 = parseFloat(prompt("Digite o segundo número:"));

// Cria uma variável base para usar os operadores de atribuição
let resultado;

// Adição
resultado = num1;
resultado += num2;
console.log(`Adição: ${num1} + ${num2} = ${resultado}`);

// Subtração
resultado = num1;
resultado -= num2;
console.log(`Subtração: ${num1} - ${num2} = ${resultado}`);

// Multiplicação
resultado = num1;
resultado *= num2;
console.log(`Multiplicação: ${num1} * ${num2} = ${resultado}`);

// Divisão
resultado = num1;
resultado /= num2;
console.log(`Divisão: ${num1} / ${num2} = ${resultado}`);

// Resto da divisão
resultado = num1;
resultado %= num2;
console.log(`Resto: ${num1} % ${num2} = ${resultado}`);