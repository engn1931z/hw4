# hw4
Homework 4 Assignment for ENGN1931Z

To this point, we have learned how to control instruments that were specifical designed for programmatic control, e.g. by SCPI. However, it is often the case that we may need to control devices that were not designed with this purpose. For example, there are many computer controlled instruments where the manufacturers intend for you to control their device using specific software. This includes cases where they did not imagine a need for automation or where they may wish for you to purchase additional software from them to enable automation.

Thankfully, many computer controlled devices use serial communication that can be easily monitored and decoded. (This includes many motor controllers and simple sensors that have USB connections, but use a USB-RS232 converter chip for operation.) The key to this procedure is finding a way to monitor (sniff) the serial port, and then carefully considering the commands that you send to the instrument. 

To monitor the port, I would recommend the `socat` method that we explored in class (and is [described here on SO](http://unix.stackexchange.com/a/225904/192231)). Remember that PTY is a pseudoterminal, so if you want to setup a virtual device at `/dev/ttyUSB0`, then you would use `PTY,link=/dev/ttyUSB0,raw,echo=0` as one of the socat ends. Finally, to read the resulting traffic (e.g. in your input/output text file logs), I would encourage you to use `xxd` to create hex dumps that will show you non-printable characters.

As demonstrated in class, the `hw4` file is an executable that can control a Thorlabs PRM1Z8 motorized rotation stage. Your goal for this assignment is to learn the serial commands that this program uses to control the stage, and demonstrate this knowledge by writing a python script that passes a set of precise motion commands to an virtual PRM1Z8 device online.

The final submission code for the auto-grader will be posted shortly. For now, you can begin to download the `hw4` executable and test it to decipher the command structure.  (**Note that to run the executable, you can use the following terminal command: `sudo ./hw4` in the directory with the file.** The `./` prefix adds the current directory to the path when looking for executables, and sudo will probably be helpful when you are trying to sniff the port.)
