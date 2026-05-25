force -freeze sim:/majority1/A 0 0
force -freeze sim:/majority1/B 0 0
force -freeze sim:/majority1/C 0 0
run

force -freeze sim:/majority1/A 0 0
force -freeze sim:/majority1/B 0 0
force -freeze sim:/majority1/C 1 0
run

force -freeze sim:/majority1/A 0 0
force -freeze sim:/majority1/B 1 0
force -freeze sim:/majority1/C 0 0
run

force -freeze sim:/majority1/A 0 0
force -freeze sim:/majority1/B 1 0
force -freeze sim:/majority1/C 1 0
run

force -freeze sim:/majority1/A 1 0
force -freeze sim:/majority1/B 0 0
force -freeze sim:/majority1/C 0 0
run

force -freeze sim:/majority1/A 1 0
force -freeze sim:/majority1/B 0 0
force -freeze sim:/majority1/C 1 0
run

force -freeze sim:/majority1/A 1 0
force -freeze sim:/majority1/B 1 0
force -freeze sim:/majority1/C 0 0
run

force -freeze sim:/majority1/A 1 0
force -freeze sim:/majority1/B 1 0
force -freeze sim:/majority1/C 1 0
run
