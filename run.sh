sudo chmod 666 /dev/ttyACM0
chmod +x main.py # Give the python file execute rights
echo -n "Enter language: " # Enter the language for the tts
read lang

while true # Run the file, looping in bash because it's easier
do
    ./main.py $lang
done
