const Sequelize = require('sequelize');
const Config = require('../config/database');
const ProdutoController = {
    index: async (req,res)=> {
        const db = new Sequelize(Config);
        nomeLivro = "Harry Pother";
        const result = await db.query('select * from produto where produto.nome = :nomeLivro',
        {
            replacements: {
                nomeLivro
            },
            type:Sequelize.QueryTypes.SELECT
        })

        console.log(result)
    }
}

module.exports = ProdutoController;