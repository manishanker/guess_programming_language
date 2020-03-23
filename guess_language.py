#!/usr/bin/env python3

import os
from guesslang import Guess
import warnings
warnings.filterwarnings("ignore")
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


g = Guess()


def guess_lang(text):
    """
        text: input text
        return: predicted progamming language
    """
    lang = g.language_name(text)
    return lang


if __name__ == "__main__":
    sample_lang = """
    % Quick sort

    -module (recursion).
    -export ([qsort/1]).

    qsort([]) -> [];
    qsort([Pivot|T]) ->
          qsort([X || X <- T, X < Pivot])
          ++ [Pivot] ++
          qsort([X || X <- T, X >= Pivot]).
    """

    sample_lang1 = """
    try:
        from tensorflow.python.util import module_wrapper as deprecation
    except ImportError:
        from tensorflow.python.util import deprecation_wrapper as deprecation
    deprecation._PER_MODULE_WARNING_LIMIT = 0"""

    sample_lang2 = """
    SELECT column_name(s)
    FROM table1
    RIGHT JOIN table2
    ON table1.column_name = table2.column_name;
    """

    target_lang = guess_lang(sample_lang)
    print("firt input code is :", sample_lang)
    print("\n\n")
    print("First Programming language could be: ", target_lang)

    print("\n\n\n")

    target_lang1 = guess_lang(sample_lang1)
    print("input code is :", sample_lang1)
    print("\n\n")
    print("Second Programming language could be: ", target_lang1)

    print("\n\n\n")

    target_lang2 = guess_lang(sample_lang2)
    print("input code is :", sample_lang2)
    print("\n\n")
    print("Third Programming language could be: ", target_lang2)
