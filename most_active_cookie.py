import argparse # cli-parsing library

"""
Builds the command line parser that stores the arguments specified by the
command line.

Outputs: parser -  the parser needed to process and store argument values
"""
def make_parser():

    # prepare the command line parser
    parser = argparse.ArgumentParser(prog="Cookie Log Parser",
        description="Parses cookie logs for relevant information.")
    parser.add_argument("cookie_log", type=str,
        help="the name of the cookie log file")
    parser.add_argument("-d", "--date", type=str,
        help="the date to search through for the most active cookie")

    return parser


"""
Parses a log file of cookies and outputs the most active cookie on a given date.
Assumes the cookie log file has the column names as its first line

Inputs: args   - the dictionary containing arguments passed from the terminal
                 which includes:
            args.cookie_log - the name of the cookie log file (assumed to be in
                              the folder as the script itself)
            args.date       - the date in which to find the most active cookie
        header - whether the first line contains the column names, default
                 assumption is that it does

Outputs: query_result  - the query result specified by the flags
"""
def parse_log(args, header=True):

    query_result = []

    # open and read the file into memory
    with open(args.cookie_log) as log:
        data = log.readlines()

    # omit the header if it exists
    if header:
        data = data[1:]

    # query on date
    if args.date:

        cookie_counts = {}

        # process and filter for that date only
        for line in data:
            row = line.split(',')

            # separate the date from the time
            cookie = row[0]
            date_time = row[1]
            date = date_time[:date_time.index('T')]

            # tally cookie if it has the right date
            if args.date == date:
                if cookie not in cookie_counts:
                    cookie_counts[cookie] = 0
                cookie_counts[cookie] += 1

        # get the max occurences
        max_occ = max(cookie_counts.values(), default=0)

        # return the list of cookies
        query_result = [cookie for cookie, ct in cookie_counts.items() if ct == max_occ]

    return query_result

def main():

    parser = make_parser()
    args = parser.parse_args()

    # no file, print help and return
    if not args.cookie_log:
        parser.print_help()
        return

    # no query specified, print help and return
    if not args.date:
        print("No queries were specified.")
        parser.print_help()
        return

    query_result = parse_log(args)

    # query specified, print query result
    if query_result:
        for cookie in query_result:
            print(cookie)
    else:
        print("No cookies were found on the date.")

if __name__ == "__main__":
    main()
