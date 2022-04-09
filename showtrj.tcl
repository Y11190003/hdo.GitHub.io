draw color blue
proc sh {fps1 fps2 space selection} {             
set selnow [atomselect top $selection frame $fps1]
set selnext [atomselect top $selection frame $fps1]
set num [$selnow num]
for {set fps $fps1} {$fps<$fps2} {incr fps $space} {
$selnow frame $fps
$selnext frame [expr $fps+$space]
$selnow update
$selnext update
for {set i 0} {$i<$num} {incr i 1} {
draw line [lindex [$selnow get {x y z}] $i] [lindex [$selnext get {x y z}] $i] width 1
draw sphere [lindex [$selnext get {x y z}] $i] radius 0.13
}
puts "Frame $fps done"
}
}
