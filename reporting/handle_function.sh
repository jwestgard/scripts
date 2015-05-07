function handle () { 
	for pid in "$@"; do
		echo Fetching handle for "$pid"\.\.\.
		curl -# http://fedora.lib.umd.edu/handle/?action=lookup&pid=$pid \
	   | awk '/<handlehttp>/ {b=13; e=(length($0)-25); print substr($0,b,e)}'
	done
	}