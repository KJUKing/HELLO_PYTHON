var Animal = require('./animal')

class Human extends Animal{

    constructor() {
        super();
        this.lang =0;
    }

    momstouch(stroke) {
        this.lang += stroke;
    }
}

module.exports = Human;

var human = new Human();
console.log("cnt_hair", human.cnt_hair);
console.log("lang", human.lang);

human.eatWell();
console.log("cnt_hair", human.cnt_hair);

human.momstouch(100);
console.log("lang", human.lang);
