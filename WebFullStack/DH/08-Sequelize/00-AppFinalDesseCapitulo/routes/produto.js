const express = require('express');
const router = express.Router();
const ProdutoController = require('../controllers/ProdutoController');

/*Listar produtos*/
router.get('/', ProdutoController.index);

module.exports = router;
