let idade = Number(prompt("Digite sua idade: "));
let status = prompt("Digite o status: ").trim().toLowerCase();

let resultado = (idade >= 18) 
    ? "Maior de idade!" 
    : "Menor de idade!";
    
console.log(resultado);

switch (status) {
    case "registrado":
        console.log("Bem vindo ao site!");
        break;
    case "não registrado":
        console.log("Complete seu registro!");
        break;
    default:
        console.log("Status desconhecido");
}

let final = (idade >= 18 && status === "registrado") 
    ? "Acesso Completo!" 
    : "Acesso Limitado!";
    
console.log(final);
