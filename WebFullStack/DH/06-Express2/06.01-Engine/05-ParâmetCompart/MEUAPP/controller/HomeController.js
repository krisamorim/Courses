//enviando informações para a view, colocando a variavel objeto dentro da função 
//no controler TesteControler um array foi importatndo e tranformado em objeto dentro da função

const HomeController = {
    index: (req, res) => {

        let info = {
            cursos: ["FullStack", "Mobile Android", "Marketin Digital"],
            alunos: ["Luciana", "kris"]
        };

        return res.render("index", info);
    }
};

module.exports = HomeController;