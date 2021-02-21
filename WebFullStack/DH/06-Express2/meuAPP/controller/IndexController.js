let IndexController = {
    semView: (req,res) => {    
//        res.send(req.query); //metodo Query pega a query String
        let {nome, idade} = req.query;
        res.send("Olá "+nome+"! Você tem "+idade+" anos");
    },

    comView: (req,res) => {
        let {nome, idade} = req.query;
        res.render('contatoComView', {nomeUsuario:nome, idadeUsuario:idade});
    },

    // metodo que recebe e trata os dados do formulario /view/contatoUsandoFormComView
    contatoConfirmar: (req,res) => {
        let {nome, idade, altura} = req.query;
        res.send("Nome: "+nome+"<br>Idade: "+idade+"<br> Altura: "+altura+"<br>Foram enviados!");
    },

    //esse metodo somente direciona o usuario para a view contatousandoformcomview
    contatoUsandoFormComView: (req,res) => {
        res.render('contatoUsandoFormComView')
    }
}

module.exports = IndexController;