// enviando para uma view um array que foi transofrmado em objeto
//no controler HomeController tivemos que inserir a variavel literal dentro da função 


const produtos = ['Sorvete 250g', 'Bolacha de Chocolate', 'Maçã 500g'];
   const TesteController = {
      index: (req,res) => {
      
         res.render("teste",{items: produtos});
         }
     }

module.exports = TesteController;