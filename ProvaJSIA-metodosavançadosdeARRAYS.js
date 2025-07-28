const nomes = [];

while (true) {
  const opcao = prompt(
    "Escolha uma opção:\n" +
    "1 - Adicionar nome\n" +
    "2 - Filtrar nomes por letra\n" +
    "3 - Buscar nome exato\n" +
    "4 - Transformar nomes em MAIÚSCULO\n" +
    "5 - Verificar se todos têm mais de 3 letras\n" +
    "6 - Mostrar lista atual\n" +
    "0 - Sair"
  );

  if (opcao === "0") {
    alert("Programa encerrado.");
    break;
  }

  switch (opcao) {
    case "1":
      const nome = prompt("Digite o nome para adicionar:");
      nomes.push(nome);
      console.log("Lista atualizada:", nomes);
      break;

    case "2":
      const letra = prompt("Digite a letra para filtrar:");
      const filtrados = nomes.filter(n => n.startsWith(letra));
      console.log("Nomes filtrados:", filtrados);
      break;

    case "3":
      const busca = prompt("Digite o nome que deseja buscar:");
      const encontrado = nomes.find(n => n === busca);
      if (encontrado) {
        console.log("Nome encontrado:", encontrado);
      } else {
        console.log("Nome não encontrado.");
      }
      break;

    case "4":
      const maiusculos = nomes.map(n => n.toUpperCase());
      console.log("Nomes em MAIÚSCULO:", maiusculos);
      break;

    case "5":
      const todosValidos = nomes.every(n => n.length > 3);
      console.log("Todos os nomes têm mais de 3 letras?", todosValidos);
      break;

    case "6":
      console.log("Lista atual:", nomes);
      break;

    default:
      alert("Opção inválida!");
  }
}
