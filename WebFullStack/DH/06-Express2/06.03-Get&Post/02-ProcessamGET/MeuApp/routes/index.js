var express = require('express');
var router = express.Router();
var IndexController = require('../controller/IndexController')
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/contato', IndexController.viewContato);
router.get('/celulares', IndexController.viewCelulares);
router.get('/celulares/deletar/:id', (req,res) => {
  var celulares = [
    {
        id: 1,
        nome: 'Motorola Moto E6 Plus',
        preco: 14999
    },
    {
        id: 2,
        nome: 'Motorola Moto G7',
        preco: 19999
    }
  ];
  // res.send(req.params)
  function remover(celulares){
    return celulares.id !== req.params
  }

  var celulares = celulares.filter(remover);
  res.send(celulares)
  
})
module.exports = router;
