#!/usr/bin/node
// A script that create a rectangle class then have a print method

class Rectangle {
  /* class that defines a Rectangle object */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
	    let row = ''; 
	    for (let j =0; j < this.width; j++) {
		    row += 'X';
	    }
	    console.log(row);
    }
  }
}
module.exports = Rectangle;
