all:	test.html

test.html: dcf.py dcf.html
	rm -f test.html
	python dcf.py > test.html
	open test.html

clean:
	rm -f test.html
