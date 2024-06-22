//  Classe model de atividade
class Activity {
    id;                     // ID unico de cada atividade
    atividade;               // Uma descrição da atividade
    tipo;                   // O tipo de atividade a ser analisada
    participantes;           // Quantidade de participantes
    acessibilidade;          //  Acessibilidade em porcentagem

    //  Construtor para a criação de uma nova atividade
    constructor(id, activity, type, participants, accessibility){
        this.id = id;
        this.atividade = activity;
        this.tipo = type;
        this.participantes = participants;
        this.acessibilidade = accessibility;
    }
}

module.exports = Activity;
