set space {7 8.5 10 11.5 }
foreach j $space {
set fps1 0
set fps2 20001
set myfile [open /home/liuchangwei/vmd-1.9.3/Ni-num/$j.txt  w]

for {set i $fps1} {$i<$fps2} {incr i 1} {
set comni [measure center [atomselect top "type 1" frame $i]]
set comx [lindex $comni 0]
set comy [lindex $comni 1]
set comz [lindex $comni 2]

if {$j>7} {
set selh [atomselect top "((x-$comx)**2+(y-$comy)**2+(z-$comz)**2) < ($j **2) and ((x-$comx)**2+(y-$comy)**2+(z-$comz)**2) > (($j-1.5) **2) and type 1" frame $i]
puts $myfile "$i [$selh num]"
} else {
set sell [atomselect top "((x-$comx)**2+(y-$comy)**2+(z-$comz)**2) < ($j **2) and type 1" frame $i]
puts $myfile "$i [$sell num]"
}
}
close $myfile
}
puts "finish!"
