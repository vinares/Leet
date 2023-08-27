find . -type f -exec cat {} + | grep -v "code=start\|code=end" |  wc -l 
