set fps1 19000
set fps2 20001
set myfile [open /home/liuchangwei/vmd-1.9.3/Ni-num/111.txt  w]
set nni [llength [lsort -unique [[atomselect top "type 1"]]]]

for {set i 1} {$i<=$nni} {incr i 10} {
set comni [measure center [atomselect top "type 1" frame $i]]
set comx [lindex $comni 0]
set comy [lindex $comni 1]
set comz [lindex $comni 2]

#set ni [atomselect top "type 1" frame $i]
set que [expr ([$x]-$comx)**2+([$y]-$comy)**2+([$z]-$comz)**2]
puts $myfile "$i  $que "
}
close $myfile
puts "finish!"

