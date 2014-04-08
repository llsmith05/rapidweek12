difference(){
color("darkorange")
linear_extrude(height = 2)
square([8,15]);

color("coral")
translate([1, 1, 1.5])
square([6,12]);
}

color("coral")
translate([4,14,1.7])
circle(.7);