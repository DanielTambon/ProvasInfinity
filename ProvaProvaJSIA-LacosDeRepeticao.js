const nomes = [];

while (true) {
  const entrada = prompt('Digite um nome (ou "sair" para encerrar):');
  if (!entrada) {
    alert('Entrada vazia! Por favor, digite um nome ou "sair".');
    continue;
  }
  if (entrada.toLowerCase() === 'sair') {
    break;
  }
  nomes.push(entrada);
}

// Exibição com for, mostrando índice + nome
console.log('Lista de nomes com índice:');
for (let i = 0; i < nomes.length; i++) {
  console.log(`${i + 1}: ${nomes[i]}`);
}

// Exibição com for...of, mensagem personalizada
console.log('\nMensagens de boas-vindas:');
for (const nome of nomes) {
  console.log(`Bem-vindo(a), ${nome}!`);
}
