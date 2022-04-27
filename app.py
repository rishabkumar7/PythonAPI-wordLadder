# Python3 program to find length of the
# shortest chain transformation from source
# to target
from collections import deque
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, request

app = Flask(__name__)
api = Api(app)

startWord = None
targetWord = None
# Returns length of shortest chain
# to reach 'target' from 'start'
# using minimum number of adjacent
# moves. D is dictionary


def shortestChainLen(start, target, D):

    if start == target:
        return 0
    # If the target is not
    # present in the dictionary
    if target not in D:
        return 0

    # To store the current chain length
    # and the length of the words
    level, wordlength = 0, len(start)

    # Push the starting word into the queue
    Q = deque()
    Q.append(start)

    # While the queue is non-empty
    while (len(Q) > 0):

        # Increment the chain length
        level += 1

        # Current size of the queue
        sizeofQ = len(Q)

        # Since the queue is being updated while
        # it is being traversed so only the
        # elements which were already present
        # in the queue before the start of this
        # loop will be traversed for now
        for i in range(sizeofQ):

            # Remove the first word from the queue
            word = [j for j in Q.popleft()]
            # Q.pop()

            # For every character of the word
            for pos in range(wordlength):

                # Retain the original character
                # at the current position
                orig_char = word[pos]

                # Replace the current character with
                # every possible lowercase alphabet
                for c in range(ord('a'), ord('z')+1):
                    word[pos] = chr(c)

                    # If the new word is equal
                    # to the target word
                    if ("".join(word) == target):
                        return level + 1

                    # Remove the word from the set
                    # if it is found in it
                    if ("".join(word) not in D):
                        continue

                    del D["".join(word)]

                    # And push the newly generated word
                    # which will be a part of the chain
                    Q.append("".join(word))

                # Restore the original character
                # at the current position
                word[pos] = orig_char

    return 0


class Api(Resource):
    def get(self):
        startWord = request.args.get('start')
        targetWord = request.args.get('target')
        wordData = "Length of shortest chain is: " + \
            str(shortestChainLen(startWord, targetWord, D))
        print(startWord, targetWord)
        return {'Data': wordData}, 200


api.add_resource(Api, '/api')


@app.route("/")
def index():
    return render_template("index.html")


# Driver code
if __name__ == '__main__':

    # Make dictionary
    D = {}
    D["humic"] = 1
    D["humid"] = 1
    D["wane"] = 1
    D["jade"] = 1
    D["molt"] = 1
    D["moll"] = 1
    D["want"] = 1
    D["slag"] = 1
    D["wade"] = 1
    D["mist"] = 1
    D["dolt"] = 1
    D["doll"] = 1
    D["mate"] = 1
    D["fade"] = 1
    D["maze"] = 1
    D["wart"] = 1
    D["jake"] = 1
    D["wary"] = 1
    D["mitt"] = 1
    D["wake"] = 1
    D["gate"] = 1
    D["mite"] = 1
    D["wait"] = 1
    D["faze"] = 1
    D["malt"] = 1
    D["hemic"] = 1
    D["male"] = 1
    D["molten"] = 1
    D["faded"] = 1

    app.run()
