let express = require('express');
let router = express.Router();
let ProdutoController = require ('../controller/ProdutoController')

//rota  que irá apontar para  a view que irá mostrar o formulário
router.get('/criar', ProdutoController.viewForm);

//rota para receber os dados do form da view através de POST. Pode ser a mesma que de cima mas o method tem que ser diferente
router.post('/criar', ProdutoController.salvarForm)


module.exports = router;