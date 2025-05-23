-- Criação da tabela Produtos com ProdutoID gerado automaticamente
CREATE TABLE Produtos (
    ProdutoID INT AUTO_INCREMENT PRIMARY KEY,
    NomeProduto VARCHAR(100),
    Quantidade INT,
    Preco DECIMAL(10, 2)
);

-- Inserção de três registros (sem precisar informar o ProdutoID)
INSERT INTO Produtos (NomeProduto, Quantidade, Preco)
VALUES 
    ('Camiseta Algodão', 50, 29.90),
    ('Calça Jeans', 30, 89.90),
    ('Tênis Esportivo', 20, 199.99);
