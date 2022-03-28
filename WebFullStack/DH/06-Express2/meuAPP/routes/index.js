var express = require('express');
var router = express.Router();
var IndexController = require('../controller/IndexController');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/contatosemview', IndexController.semView);
router.get('/contatocomview', IndexController.comView);
router.get('/contatousandoformcomview', IndexController.contatoUsandoFormComView);

// rota que recebe os dados do form da view contatoUsandoFormComView
router.get('/contatoconfirmar', IndexController.contatoConfirmar);


module.exports = router;
