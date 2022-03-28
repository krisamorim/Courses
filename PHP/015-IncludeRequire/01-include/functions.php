<?php
    function sum(){
        $args = func_get_args();
        $tot = func_num_args();
        $v = 0;

        for($x=0;$x<$tot;$x++){
            $v += $args[$x];
        }
        return $v;
    }

    #need to fix
    function minus($x,$y,$z){
        // $args = func_get_args();
        // $totArgs = func_num_args();
        // $v = $args[0];

        // for($x=1;$x<$totArgs;$x++){
        //     $v =- $args[$x];
        //}
        $res = $x - $y;
        $v = $res -$z;
        return $v;
    }

    function times(){
        $args = func_get_args();
        $totArgs = func_num_args();
        $v = 1;

        for($x=0;$x<$totArgs;$x++){
            $v *= $args[$x];
        }
        return $v;
    }
?>