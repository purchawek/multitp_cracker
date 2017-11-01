full:
	g++ -c -fPIC src/findclosest.cc -o bin/findclosest.o && g++ -shared -Wl,-soname,bin/libfindclosest.so -o bin/libfindclosest.so bin/findclosest.o && python3 src/main.py

test:
	python3 -m unittest tests.testmain

test_old:
	g++ -c -fPIC src/findclosest.cc -o bin/findclosest.o && g++ -shared -Wl,-soname,bin/libfindclosest.so -o bin/libfindclosest.so bin/findclosest.o && python3 src/read_cryp.py "tests/crypto01"
