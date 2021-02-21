var express = require('express');
var router = express.Router();

//add by kris
var ContatoController = require("../controllers/ContatoController");
var EstudanteController = require("../controllers/EstudanteController");

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


//add by Kris
router.get("/contato", ContatoController.index);
router.get("/estudante", EstudanteController.index);
module.exports = router;
