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

4. GATK

    > To download the necessary tools from GATK, registering for a username and password is required. Do that here: http://gatkforums.broadinstitute.org/gatk
    
    > Once you have signed up, navigate to https://software.broadinstitute.org/gatk/download/ and download the newest version of GATK via the link.
    
    > The file will come in the **tar.bz2** file format and can be uncompressed using the following command.
    
    ~~~
    $ tar -xvjf *filename*.tar.bz2
    ~~~
    
    > This will result in the executable jar file that is called when using GATK commands.
    
5. R Programming

    ~~~
    $ sudo apt-get install r-base --yes
    ~~~
    
6. Perl

    > If using a Linux server, such as Ubuntu 16.04, Perl comes pre-installed. Use the following command to check the version of Perl.
    
    ~~~
    $ perl -v
    ~~~
    
7. Varscan

    > Varscan's executable jar file can be downloaded from the following link: http://varscan.sourceforge.net/ after following the link, navigate to the download page and download the newest version. This is the jar file that is called when using Varscan commands.
    
8. Annovar

    > Similar to GATK, Annovar requires pre-registration to download the latest version from the following: http://www.openbioinformatics.org/annovar/annovar_download_form.php
    
    > After registering and following the instructions, a very good **Quick Start-Up Guide** can be found at: http://annovar.openbioinformatics.org/en/latest/user-guide/startup/
    
    
