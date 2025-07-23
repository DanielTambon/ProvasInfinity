// Array para armazenar tarefas
const tarefas = [];

// Função anônima para adicionar tarefas
const adicionarTarefa = function(novaTarefa) {
  tarefas.push({ texto: novaTarefa, concluida: false });
  console.log(`Tarefa adicionada: "${novaTarefa}"`);
};

// Arrow function para listar tarefas
const listarTarefas = () => {
  console.log("Lista de tarefas:");
  tarefas.forEach((tarefa, index) => {
    const status = tarefa.concluida ? "[Concluída]" : "[Pendente]";
    console.log(`${index}: ${tarefa.texto} ${status}`);
  });
};

// Função que recebe um callback para manipular tarefas
function manipularTarefa(indice, callback) {
  if (indice < 0 || indice >= tarefas.length) {
    console.log("Índice inválido.");
    return;
  }
  callback(indice);
}

// Callback para remover tarefa
const removerTarefa = (indice) => {
  const removida = tarefas.splice(indice, 1);
  console.log(`Tarefa removida: "${removida[0].texto}"`);
};

// Callback para atualizar tarefa
const atualizarTarefa = (indice) => {
  const novoTexto = prompt("Digite o novo texto para a tarefa:");
  if (novoTexto) {
    tarefas[indice].texto = novoTexto;
    console.log(`Tarefa ${indice} atualizada para: "${novoTexto}"`);
  } else {
    console.log("Texto inválido, atualização cancelada.");
  }
};

// Callback para concluir tarefa
const concluirTarefa = (indice) => {
  tarefas[indice].concluida = true;
  console.log(`Tarefa ${indice} marcada como concluída.`);
};

// Função para interação com o usuário
function iniciarGerenciador() {
  let continuar = true;

  while (continuar) {
    const acao = prompt(
      "Escolha uma ação:\n" +
      "1 - Adicionar tarefa\n" +
      "2 - Listar tarefas\n" +
      "3 - Remover tarefa\n" +
      "4 - Atualizar tarefa\n" +
      "5 - Concluir tarefa\n" +
      "6 - Sair"
    );

    switch (acao) {
      case "1":
        const nova = prompt("Digite a nova tarefa:");
        if (nova) adicionarTarefa(nova);
        else console.log("Tarefa inválida.");
        break;

      case "2":
        listarTarefas();
        break;

      case "3":
        const removerIndice = parseInt(prompt("Digite o índice da tarefa para remover:"));
        manipularTarefa(removerIndice, removerTarefa);
        break;

      case "4":
        const atualizarIndice = parseInt(prompt("Digite o índice da tarefa para atualizar:"));
        manipularTarefa(atualizarIndice, atualizarTarefa);
        break;

      case "5":
        const concluirIndice = parseInt(prompt("Digite o índice da tarefa para concluir:"));
        manipularTarefa(concluirIndice, concluirTarefa);
        break;

      case "6":
        continuar = false;
        console.log("Encerrando o gerenciador de tarefas.");
        break;

      default:
        console.log("Opção inválida, tente novamente.");
    }
  }
}

// Inicia o programa
iniciarGerenciador();
