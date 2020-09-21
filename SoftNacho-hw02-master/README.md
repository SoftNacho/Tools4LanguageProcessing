HW02
==============

During this semester, you will be required to gain proficiency with at least one command line text editor. The two most widely used command line text editors are [GNU Emacs](https://www.gnu.org/software/emacs/) and [Vim](http://www.vim.org/). There are others (such as [nano](http://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/), but in this class you will be expected to become proficient with at least one of Emacs or Vim.

In this assignment you will play the first levels of [an online VIM tutorial game](http://vim-adventures.com). The game is designed to teach you proficiency in the most important keyboard shortcuts needed to efficiently use Vim. There is a paid version that costs $25, and provides more in-depth tutorial lessons. In this assignment you only need to play the free levels.

In this part you will also practice more use of the Linux command line, and will upload a file to the class server.


Do the following:

* Go to [VIM Adventures](http://vim-adventures.com)
* Play the game through the end of the free levels
* When you get to the end of the free levels, it should look something like this:

![this](assets/img/vim1.png)


* At the bottom of the screen, select "User Statistics Screen": 

![this](assets/img/vim2.png)


* You should now see the "User Statistics Screen": 

![this](assets/img/vim3.png)

* Take a screenshot of your entire screen, including the "User Statistics Screen". Save the screenshot as hw02.jpg. If your screenshot program saved the file as something other than a JPEG, open it with an image editor and save it as a JPEG, with the exact file name hw02.jpg
* Open a [terminal](https://en.wikipedia.org/wiki/Terminal_emulator). On Mac OS X, this will be a program called [Terminal](https://en.wikipedia.org/wiki/Terminal_(OS_X)) in your Applications/Utilities folder. On Windows, you will likely need to download and set up a third-party program such as [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html). On Linux, this will be the [GNOME Terminal](https://en.wikipedia.org/wiki/GNOME_Terminal) or [KDE Konsole](https://en.wikipedia.org/wiki/Konsole), or [the equivalent](https://en.wikipedia.org/wiki/List_of_terminal_emulators).

* At the [command line](https://en.wikipedia.org/wiki/Command-line_interface) within the terminal emulator, use [scp](http://linuxcommand.org/man_pages/scp1.html) to upload hw02.jpg to the cl.linguistics.illinois.edu server:

```bash
scp hw02.jpg yourActualNetID@cl.linguistics.illinois.edu:~/hw02.jpg
```

If you're using Windows, instead of doing the above, you'll probably need to use a different third-party SCP client for Windows such as [WinSCP](https://winscp.net/eng/download.php) to upload the file.


* At the [command line](https://en.wikipedia.org/wiki/Command-line_interface) within the terminal emulator, connect to the cl.linguistics.illinois.edu server using [ssh](http://linuxcommand.org/man_pages/ssh1.html). Your username is your NetID, and your password should be your [NetID password](https://techservices.illinois.edu/services/netid-password). Note: to connect to the server from off campus, you may first need to connect to the campus network using an approved [VPN client](https://techservices.illinois.edu/services/virtual-private-networking-vpn/download-and-set-up-the-vpn-client).

```bash
ssh yourActualNetID@cl.linguistics.illinois.edu
```

* Use [ls](http://linuxcommand.org/man_pages/ls.html) to verify that you successfully uploaded the file:

```bash
ls -l ~/
```

You should see a file listed called hw02.jpg, with a date and timestamp that corresponds to when you uploaded the files. If you don't, that probably means you did not successfully upload hw02.jpg. You should also see a directory called hw02, which is where you created hello.sh in Part 1 above.

* Use [mv](http://linuxcommand.org/man_pages/mv.html) to move hw02.jpg into the hw02 directory:

```bash
mv ~/hw02.jpg ~/YOUR_GITHUB_USERNAME-hw02/
```

* Use [ls](http://linuxcommand.org/man_pages/ls.html) to verify that you successfully moved the file:

```bash
ls -l ~/YOUR_GITHUB_USERNAME-hw02
```

You should see a file listed called hw02.jpg, with a date and timestamp. If you don't, that probably means you did not successfully move hw02.jpg into the hw02 directory.

Use cd to navigate into the hw02 directory

```bash
cd ~/YOUR_GITHUB_USERNAME-hw02
```

* Use git add to add hw02.jpg
* Use git commit. Use a meaningful commit message.
* Use git push to turn in the assignment
