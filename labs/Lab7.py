from gooey import Gooey, GooeyParser
import time

@Gooey()
def main():
        error_parser = GooeyParser(description='This demo is designed to raise an error!')
        #This gives the user a choice of whether to error or not
        error_parser.add_argument(
            "error",
            metavar='Should I error?',
            help="Whether or not to raise error",
            choices=['Yes', 'No'],
            default='Yes')
        #This provides a flag for the argument above
        error_parser.add_argument(
                '-f', '--foo',
                metavar='Example Flag',
                action='store_true',
                help='Example Flag (does not affect outcome)')
        #This is how Gooey parses the arguments depending on what choice is given
        args = error_parser.parse_args()
        if 'yes' in args.error.lower():
                print('Will error in')
                for i in range(5, 0, -1):
                    print(i)
                    time.sleep(1)
                raise Exception("Looks like you've errored!")

        print("Success! You've avoided an error!")
#This runs the program
if __name__ == '__main__':
    main()
