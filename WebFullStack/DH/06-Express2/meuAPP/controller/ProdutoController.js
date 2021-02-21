let ProdutoController = {
    viewForm: (req,res) => res.render('produto'),
    salvarForm: (req,res) => {
        let {nomeProduto, precoProduto} = req.body;
        res.send("O produto "+nomeProduto+", teve o preço atualizado para "+precoProduto)
    }
}

module.exports = ProdutoController;