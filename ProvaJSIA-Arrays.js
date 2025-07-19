const listaCompras = [];

while (true) {
  const acao = prompt(
    'Escolha uma ação: \n1 - Adicionar item\n2 - Remover item\n3 - Atualizar item\n4 - Exibir lista\n5 - Sair'
  );

  if (acao === null) {
    alert('Programa encerrado.');
    break;
  }

  switch (acao.trim()) {
    case '1': {
      const item = prompt('Digite o nome do item para adicionar:');
      if (item && item.trim() !== '') {
        listaCompras.push(item.trim());
        alert(`Item "${item.trim()}" adicionado.`);
      } else {
        alert('Nome inválido.');
      }
      break;
    }

    case '2': {
      if (listaCompras.length === 0) {
        alert('A lista está vazia.');
        break;
      }
      exibirLista(listaCompras);
      const indiceRemover = prompt(
        'Digite o índice do item que deseja remover (começando em 1):'
      );
      const idx = Number(indiceRemover) - 1;
      if (idx >= 0 && idx < listaCompras.length) {
        const removido = listaCompras.splice(idx, 1);
        alert(`Item "${removido[0]}" removido.`);
      } else {
        alert('Índice inválido.');
      }
      break;
    }

    case '3': {
      if (listaCompras.length === 0) {
        alert('A lista está vazia.');
        break;
      }
      exibirLista(listaCompras);
      const indiceAtualizar = prompt(
        'Digite o índice do item que deseja atualizar (começando em 1):'
      );
      const idxAtualizar = Number(indiceAtualizar) - 1;
      if (idxAtualizar >= 0 && idxAtualizar < listaCompras.length) {
        const novoValor = prompt('Digite o novo valor do item:');
        if (novoValor && novoValor.trim() !== '') {
          const antigo = listaCompras[idxAtualizar];
          listaCompras[idxAtualizar] = novoValor.trim();
          alert(`Item "${antigo}" atualizado para "${novoValor.trim()}".`);
        } else {
          alert('Novo valor inválido.');
        }
      } else {
        alert('Índice inválido.');
      }
      break;
    }

    case '4': {
      if (listaCompras.length === 0) {
        alert('A lista está vazia.');
      } else {
        exibirLista(listaCompras);
      }
      break;
    }

    case '5':
      alert('Programa encerrado.');
      break;

    default:
      alert('Opção inválida. Tente novamente.');
  }

  if (acao === '5') {
    break;
  }
}

function exibirLista(lista) {
  console.log('Lista de Compras:');
  let i = 1;
  for (const item of lista) {
    console.log(`${i}: ${item}`);
    i++;
  }
}
