set sel [atomselect top "type 5 and pbwithin 1.8 of type 3"]
set file [open /home/liuchangwei/lammps/sus-shengwuzhi/bondnums/1-1.txt w]
for {set i 0 } {$i < 20002} {incr i 10} {
$sel frame $i
$sel update
puts $file "$i [$sel num]"
}
close $file
puts "finsihed!!"
