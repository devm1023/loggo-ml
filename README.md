# Python Logger
This is a python standard output printing helper which prefixes useful info to the message to be printed. Can be used in long running operations as an indication of progress and running time. Has several options which can be configured through constructor. All options have sensible defaults, so that you can just instantiate an object and start using.

## Motivation
As I was working on a ML problem, there were many bits of code which really took long time. I started adding print() statements to log and track the progress. Then I included timestamp in every print, helps when a same message is printed in a long running loop. Then I added elapsed time. Then made a helper function to prefix the metadata - timestamp, elapsed time, etc. in print statement. And, as the ML program was still training, one hour later, this is what a single line of code turned into!
