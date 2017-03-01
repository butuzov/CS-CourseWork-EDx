# CS50 Speller

	`make && ./speller _text_Monty_Python_and_the_Holy_Grail.txt`

# Questions

  1.  __What is pneumonoultramicroscopicsilicovolcanoconiosis?__

    _Shortly - silicosis, word it self is a latin name for a lung disease.  Word made up by some guy  who was a president of [National Puzzlers' League](https://en.wikipedia.org/wiki/National_Puzzlers%27_League) and after some time and promoting in a puzzle book its also was included to major dictionaries. Read more at its wikipedia page - [Pneumonoultramicroscopicsilicovolcanoconiosis](https://en.wikipedia.org/wiki/Pneumonoultramicroscopicsilicovolcanoconiosis)_

  2.  __According to its man page, what does `getrusage` do?__

    _get information about resource utilization_

  3.  __Per that same man page, how many members are in a variable of type struct rusage?__

    Struct `rusage` has 16 members. Here is a full representation of struct.

  ```c
  	struct rusage {
  		struct timeval ru_utime; /* user time used */
  		struct timeval ru_stime; /* system time used */
  		long ru_maxrss;          /* max resident set size */
  		long ru_ixrss;           /* integral shared text memory size */
  		long ru_idrss;           /* integral unshared data size */
  		long ru_isrss;           /* integral unshared stack size */
  		long ru_minflt;          /* page reclaims */
  		long ru_majflt;          /* page faults */
  		long ru_nswap;           /* swaps */
  		long ru_inblock;         /* block input operations */
  		long ru_oublock;         /* block output operations */
  		long ru_msgsnd;          /* messages sent */
  		long ru_msgrcv;          /* messages received */
  		long ru_nsignals;        /* signals received */
  		long ru_nvcsw;           /* voluntary context switches */
  		long ru_nivcsw;          /* involuntary context switches */
    };
  ```

  4.  __Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we’re not changing their contents?__

    I guess it faster to work with a memory, instead a creating 8 additional variables and calculate difference each time.

  5.  __Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function’s `for` loop works.__

    C-type `for` loop has a 3 sections -> initiation; condition ; and post execution operation.
    At INITIATION part we initiating our start variables. In out case it's get next character from FILE pointer. At CONDITION we do check a condition for loop execution IN out case its EOF , which stands for End Of File. EOF is symbolic macro returned if scenario end-of-file occurred. And POST_EXECUTION scenario in our case is to read one more character... until we stuck into EOF.

  6.  __Why do you think we used `fgetc` to read each word’s characters one at a time rather than use `fscanf` with a format string like "`%s`" to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?__

    Out solution is to read data one character by one only proccesing sequences [a-z']\\0, while using `fscanf` we can deal with same set of characters + extra cases like pubctuation signs etc... Reason to use `fgetc` is a moe control for us - like we need to track only 28 characters (a-z ' and \\0 ).

  7.  __Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?__

    Variables declared in that way a immutables for this function scope, so its kind a "readonly" protection.
