#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for x in names:
        if x[:2] != "__":
            print(x)
