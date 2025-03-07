print("Hello world!")
print("Hello world!")
print("Name: [Jay Marc Custodio]")
print("Course: [BSIT]")
print("Interests in programming: [Your Interests]")
python3 hello.py > output.txt

if grep -q "Hello world!" output.txt && grep -qF "$(cat intro.txt)" output.txt; then
    echo "Output Passed"
else
    echo "Output Failed"
    exit 1
fi