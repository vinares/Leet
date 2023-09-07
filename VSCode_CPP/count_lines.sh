printf "%-18s %s\n" "#lines=$(find . -type f -exec cat {} + | grep -v "code=start\|code=end" | wc -l)"  
printf "%-12s %s\n" "#problems=$(ls | wc -l)" 
