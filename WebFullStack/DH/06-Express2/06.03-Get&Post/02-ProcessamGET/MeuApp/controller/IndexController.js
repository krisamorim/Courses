const IndexController = {
    viewContato: (req, res) => {
        res.send(req.query);
    },

    viewCelulares: (req, res) => {
        let celulares = [
            {
                nome: 'Motorola Moto E6 Plus',
                preco: 14999
            },
            {
                nome: 'Motorola Moto G7',
                preco: 19999
            },
            {
                nome: 'Alcatel 5033A',
                preco: 6999
            },
            {
                nome: 'Samsung Galaxy A50',
                preco: 33499
            }
        ];
        var {max} = req.query;

        function valorMax(celulares) {
            return celulares.preco < max 
        } 

        let buscaCel = celulares.filter(valorMax);
        // let buscaCel = celulares.filter(function(preco){
        //     return preco > max;
        // });
        
        res.send(buscaCel);
    }
    
}
module.exports = IndexController;

