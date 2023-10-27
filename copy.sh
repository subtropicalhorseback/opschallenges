array1=()

func() {
    for ((i=1; i<5; i++));
    do
        array1+=(dir$i)
    done  

    mkdir ${array1[@]}

--
    touch ${array1[@]}/file.txt    
--

}

func
# mkdir [folder1] [folder2] [folder3]
# array = (dir1 dir2 dir3 dir4)
# touch dir1 dir2 dir3 dir4/file.txt