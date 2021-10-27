let bug = [];//array of Jitter objects
let numberOfBugs = 1000;

function setup(){
    createCanvas(700,400);
    //Create objects

    for (let i=0; i < numberOfBugs; i++)
}

function draw(){
    background(255,0,0);

    bug.move();
    bug.display();
}

class Jitter{

    constructor(){
        this.x = random(width);
        this.y = random(height);
        this.diameter = 100;
        this.speed = 10;
    }

    move(){
        this.x += 1;
        this.y +=1;
    }

    display(){
        ellipse(this.x, this.y, this.diameter)
    }

    changecolor(){


    }


}