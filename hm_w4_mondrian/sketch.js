// By Sukky Yan
// Generative art in the style of painter Piet Mondrian

var colors;

// having only a certain number of available sizes makes things more Mondrian-y
var sizes = [50, 100, 150, 200];

function setup() {
  createCanvas(500, 700);
  background(255);

  // only primary colors(r,y,b) and white
  colors = [
    color(255, 255, 255),
    color(255, 0, 0),
    color(255, 255, 0),
    color(0, 0, 255),
  ];

  // make lines really thick
  strokeWeight(10);
  var y = 0;
  var x = 0;

  var currHeight = random(sizes);
  var currWidth = random(sizes);

  while (y < height) {
    x = 0;
    while (x < width) {
      fill(random(colors));
      rect(x, y, currWidth, currHeight);
      x = x + currWidth;
      currWidth = random(sizes);
    }
    y = y + currHeight;
    currHeight = random(sizes);
  }
}

function draw() {}
