var express = require('express');
var router = express.Router();


var ContatoController = require("../controller/ContatoController");
var HomeController = require("../controller/HomeController");
var TesteController = require("../controller/TesteController");

/* GET home page. */
router.get('/', HomeController.index);
router.get("/contato", ContatoController.index);
router.get("/teste", TesteController.index);

module.exports = router; 