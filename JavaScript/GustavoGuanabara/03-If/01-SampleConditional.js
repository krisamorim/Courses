      //children viables
            var cleo = "cleoPires";
            var fiuk = "fiuk";
            var sandy = "sandy";
            var junior = "junior";
      //returns father
        function dadOf(children){
            var dadCleoFiuk = "Fábio Júnior";
            var dadSandyJunior = "Xitãozinho";
            var cleo = "cleoPires";
            var fiuk = "fiuk";
            var sandy = "sandy";
            var junior = "junior";

            if (children==cleo || children==fiuk){
                return dadCleoFiuk;
            }else if (children==sandy || children==junior) {
                return dadSandyJunior;
            }
        }
        //returns mother
        function mommyOf(children){
            var mommyOfCleo = "Glória Pires";
            var mommyOfSandy = "Mãe de Sandy e Jr";
            var mommyFiuk = "Mãe de Fiuk";
            var cleo = "cleoPires";
            var fiuk = "fiuk";
            var sandy = "sandy";
            var junior = "junior";

            if (children==cleo){
                return mommyOfCleo;
            } if (children==fiuk){
                return mommyFiuk;
            } if (children==sandy || children==junior) {
                return mommyOfSandy;
            }
        }
        //check if you have the same mother
        function sameMommy(children1, children2){
            return  mommyOf(children1)==mommyOf(children2);
        }
        //check if you have the same father
        function sameDad(children1, children2){
            return dadOf(children1)==dadOf(children2);
        }
        //check if they are half brothers
        function halfSiblings(children1, children2){
            return sameMommy(children1, children1) && sameDad(children1, children2);
        }

        //Show in console
        console.log("=== Mostrar os dads===\n-> Fiuk \ndad: "+dadOf(fiuk)+"\nMãe: "+mommyOf(fiuk)+"\n-> Cleo \ndad: "+dadOf(cleo)+"\nMãe: "+mommyOf(cleo)+"\n\nCleo e Fiuk tem o mesmo dad: "+sameDad(cleo,fiuk)+"\nCleo e Fiuk tem a mesma mãe: "+sameMommy(cleo,fiuk)+"\nCleo e Fiuk are half siblings: "+halfSiblings(cleo,fiuk)+"\n\n\n-> Sandy \ndad: "+dadOf(sandy)+"\nMãe: "+mommyOf(sandy)+"\n-> Junior \ndad: "+dadOf(junior)+"\nMãe: "+mommyOf(junior)+"\n\nSandy e Junior tem o mesmo dad: "+sameDad(sandy,junior)+"\nSandy e Junior tem a mesma mãe: "+sameMommy(sandy,junior)+"\nSandy e junior são meio irmãos: "+halfSiblings(sandy,junior));

        console.log(sameMommy(fiuk,cleo));
        console.log(sameDad(cleo,fiuk));
        console.log(false && true);
