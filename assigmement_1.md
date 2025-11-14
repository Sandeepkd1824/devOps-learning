<!-- cd /mnt/d -->

1. Creating and Renaming Files/Directories

Commands:

    mkdir test_dir
    cd test_dir
    touch example.txt
    mv example.txt renamed_example.txt

Explanation:

mkdir test_dir – Creates a new directory named test_dir.

touch example.txt – Creates an empty file called example.txt inside test_dir.

mv example.txt renamed_example.txt – Renames example.txt to renamed_example.txt.



2. Viewing File Contents

Commands:

    cat /etc/passwd
    head -n 5 /etc/passwd
    tail -n 5 /etc/passwd


Explanation:

cat /etc/passwd – Displays the entire contents of /etc/passwd.

head -n 5 /etc/passwd – Shows only the first 5 lines of /etc/passwd.

tail -n 5 /etc/passwd – Shows only the last 5 lines of /etc/passwd.

3. Searching for Patterns

Command:

    grep "root" /etc/passwd


Explanation:

grep "root" /etc/passwd – Searches for all lines containing the word root in /etc/passwd.


4. Zipping and Unzipping

Commands:

    zip -r test_dir.zip test_dir
    unzip test_dir.zip -d unzipped_dir

Explanation:

zip -r test_dir.zip test_dir – Compresses the test_dir directory into a zip file named test_dir.zip.

unzip test_dir.zip -d unzipped_dir – Extracts the contents of test_dir.zip into a new directory called unzipped_dir.


5. Downloading Files

Command:

wget https://example.com/sample.txt


Explanation:

wget https://example.com/sample.txt – Downloads the file sample.txt from the specified URL to the current directory.

6. Changing Permissions

Commands:

touch secure.txt
chmod 444 secure.txt


Explanation:

touch secure.txt – Creates an empty file named secure.txt.

chmod 444 secure.txt – Changes permissions so that the file is read-only for everyone.

7. Working with Environment Variables

Command:

export MY_VAR="Hello, Linux!"


Explanation:

export MY_VAR="Hello, Linux!" – Sets a new environment variable named MY_VAR with the value "Hello, Linux!".