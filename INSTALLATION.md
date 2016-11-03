Command-Line Tools Installation Guide
=============

### Pip Installation ###

~~~
$ sudo apt-get install python-pip python-dev --yes
~~~

### Tool Installation ###

1. Burrows-Wheeler Alignment

    ~~~
    $ sudo apt-get install bwa
    ~~~
    
2. SAMtools

    ~~~
    $ sudo apt-get install samtools
    ~~~

3. Picard Tools

    > Picard requires at least Java version 1.8 to work properly. If "java -version" shows no version installed or is below "1.8.x" then follow the Java installation instructions:
    
    ~~~
    $ sudo add-apt-repository ppa:webupd8team/java
    $ sudo apt-get update
    $ sudo apt-get install oracle-java8-installer
    $ sudo apt-get install oracle-java8-set-default
    $ java –version
    ~~~
    
    > To build Picard, first clone the repository then use gradle to build the jar file.
    
    ~~~
    $ git clone https://github.com/broadinstitute/picard.git
    $ cd picard/
    $ ./gradlew shadowJar
    ~~~
    
    > The resulting jar file will be located in `picard/build/libs`. 
    > To test the installation, navigate to the built jar file and run the following:
    
    ~~~
    $ cd picard/build/libs
    $ java -jar picard.jar -h
    ~~~
    
    > Successful installation will result in the command displaying all of the functions available to Picard.

4. More instructions to be added as needed.
