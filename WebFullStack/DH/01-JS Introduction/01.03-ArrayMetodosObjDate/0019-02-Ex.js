/*
//ex01
let alunos = ["João", "Pedro", "Jorge", "Francisco"]
let indiceJoao = alunos.indexOf('João');
let indiceFrancisco = alunos.indexOf('Francisco');

//ex02 Fasendo uma nova 
let arrayFrase = [
    "Não",
    "fracassei,",
    "simplesmente",
    "encontrei",
    "dez",
    "mil",
    "soluções",
    "equivocadas"
]
let fraseNova = String(arrayFrase.join(' '))
console.log(fraseNova);

//ex03
let estudantes = [
  {
    nome: "Álvaro",
    media: 9,
    curso: "Android"
  },
  {
    nome: "Daniel",
    media: 6,
    curso: "Full Stack"
  },
  {
    nome: "Alexis",
    media: 3,
    curso: "iOS"
  }
];

let alunoFormado = estudantes.pop();


//ex 04-00 Não aceito
let estudantes = [
    {
      nome: 'Álvaro',
      media : 9,
      curso : 'Android',
    },
    {
      nome: 'Daniel',
      media : 6,
      curso : 'Full Stack',
    }
  ]

  let alvaro = {
    nome: 'João',
    media : 5,
    curso : 'IOS',
  };

  let miguel = {
      nome: 'Miguel',
      media: 2,
      curso: 'Android'
    }

    estudantes.push(alvaro);
    estudantes.push(miguel);

    console.log(estudantes);

    //ex 04-01 Nõa usa o push
   var estudantes = [
    {
      nome: 'Álvaro',
      media : 9,
      curso : 'Android',
    },
    {
      nome: 'Daniel',
      media : 6,
      curso : 'Full Stack',
    }
  ]

  let joao = {
    nome: 'João',
    media : 5,
    curso : 'IOS',
  };

  let miguel = {
    nome: 'Miguel',
    media: 2,
    curso: 'Android'
  };

  var estudantes = [...estudantes, joao, miguel]
  console.log(estudantes);

 

//ex 04-05 nãoa ceito tb
 let estudantes = [
    {
      nome: 'Álvaro',
      media : 9,
      curso : 'Android',
    },
    {
      nome: 'Daniel',
      media : 6,
      curso : 'Full Stack',
    }
  ]
let joao = [
    {
      nome: 'João',
      media : 5,
      curso : 'IOS',
    }
 ]
let miguel = [
    {
      nome: 'Miguel',
      media: 2,
      curso: 'Android',
  }
 ]

Array.prototype.push.apply(estudantes, joao)
Array.prototype.push.apply(estudantes, miguel)
console.log(estudantes);

//ex04-06 ACEITO (palavra iOS estava diferente do enunciado)
 let estudantes = [
    {
      nome: 'Álvaro',
      media : 9,
      curso : 'Android',
    },
    {
      nome: 'Daniel',
      media : 6,
      curso : 'Full Stack',
    }
  ]

estudantes.push({nome: 'João', media : 5, curso : 'iOS',})
estudantes.push({nome: 'Miguel', media : 2, curso : 'Android',})
 
//ex 05
let estudantes = [
    {
       nome: 'Álvaro',
       media : 9,
       curso : 'Android',
     },
      {
        nome: 'Daniel',
        media : 6,
        curso : 'Full Stack',
      },
      {
        nome: 'Alexis',
        media : 3,
        curso : 'iOS',
      },
    ]
    let alunoDesistente = estudantes.shift();


    //ex06
   let estudantes = [
    {
      nome: 'Alvaro',
      media : 9,
      curso : 'Android',
    },
    {
      nome: 'Daniel',
      media : 6,
      curso : 'Full Stack',
    },
    {
      nome: 'Alexis',
      media : 3,
      curso : 'iOS',
    }
  ]
  estudantes.unshift({nome: 'Mariana', media : 9, curso : 'Full Stack',})
  estudantes.unshift({nome: 'Francisco', media : 2, curso : 'Android',})
  */