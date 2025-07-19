const tarefas = [];

while (true) {
  const acao = prompt(
    'Escolha uma ação:\n' +
    '1 - Adicionar tarefa\n' +
    '2 - Listar tarefas\n' +
    '3 - Remover tarefa\n' +
    '4 - Concluir tarefa\n' +
    '5 - Sair'
  );

  if (acao === null) {
    alert('Programa encerrado.');
    break;
  }

  switch (acao.trim()) {
    case '1': { // Adicionar tarefa
      const tarefa = prompt('Digite o nome da tarefa:');
      if (tarefa && tarefa.trim() !== '') {
        tarefas.push(tarefa.trim());
        alert(`Tarefa "${tarefa.trim()}" adicionada.`);
      } else {
        alert('Nome inválido para a tarefa.');
      }
      break;
    }

    case '2': { // Listar tarefas
      if (tarefas.length === 0) {
        alert('Nenhuma tarefa na lista.');
      } else {
        let lista = 'Tarefas:\n';
        for (let i = 0; i < tarefas.length; i++) {
          lista += `${i + 1} - ${tarefas[i]}\n`;
        }
        alert(lista);
      }
      break;
    }

    case '3': { // Remover tarefa
      if (tarefas.length === 0) {
        alert('Nenhuma tarefa para remover.');
        break;
      }
      const indiceRemover = prompt('Digite o número da tarefa que deseja remover:');
      const idx = Number(indiceRemover) - 1;
      if (idx >= 0 && idx < tarefas.length) {
        const removida = tarefas.splice(idx, 1);
        alert(`Tarefa "${removida[0]}" removida.`);
      } else {
        alert('Número inválido.');
      }
      break;
    }

    case '4': { // Concluir tarefa
      if (tarefas.length === 0) {
        alert('Nenhuma tarefa para concluir.');
        break;
      }
      const indiceConcluir = prompt('Digite o número da tarefa que deseja concluir:');
      const idxC = Number(indiceConcluir) - 1;
      if (idxC >= 0 && idxC < tarefas.length) {
        if (!tarefas[idxC].startsWith('✅ ')) {
          tarefas[idxC] = '✅ ' + tarefas[idxC];
          alert(`Tarefa "${tarefas[idxC]}" marcada como concluída.`);
        } else {
          alert('Essa tarefa já está concluída.');
        }
      } else {
        alert('Número inválido.');
      }
      break;
    }

    case '5': {
      alert('Programa encerrado.');
      break;
    }

    default: {
      alert('Opção inválida. Tente novamente.');
    }
  }

  if (acao === '5') break;
}
