class Animal{
    constructor() {
        this.cnt_hair = 80000;
    }


    eatWell() {
        this.cnt_hair += 100;
    }
}

module.exports = Animal;

if (require.main === module) {

    var ani = new Animal();

    console.log("", ani.cnt_hair);
    ani.eatWell();
    console.log("", ani.cnt_hair);
}


