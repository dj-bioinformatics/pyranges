import pytest

from pyranges.pyranges import GRanges
import pyranges as pr

import pandas as pd

from io import StringIO

@pytest.fixture
def cs():

    cs = pr.load_dataset("chipseq")
    return cs



@pytest.fixture
def bg():

    bg = pr.load_dataset("chipseq_background")
    return bg


@pytest.fixture
def expected_result_regular_intersection():

    c = """chr1	226987603	226987617	U0	0	+
chr8	38747236	38747251	U0	0	-
chr15	26105515	26105518	U0	0	+"""

    return pd.read_table(StringIO(c), header=None, names="Chromosome Start End Name Score Strand".split())


def test_advanced_intersection(cs, bg, expected_result_regular_intersection):

    result = cs.intersection(bg)

    print("Actual")
    print(result.df)
    print("Expected")
    print(expected_result_regular_intersection)

    assert expected_result_regular_intersection.equals(result.df)

@pytest.fixture
def expected_result_intersection_same_strand():

    c = """chr15	26105515	26105518	U0	0	+"""

    return pd.read_table(StringIO(c), header=None, names="Chromosome Start End Name Score Strand".split())

def test_advanced_intersection_stranded(cs, bg, expected_result_intersection_same_strand):

    result = cs.intersection(bg, strandedness="same")

    print(result.df)
    print(expected_result_intersection_same_strand)

    assert expected_result_intersection_same_strand.equals(result.df)


@pytest.fixture
def expected_result_intersection_opposite_strand():

    c = """chr1	226987603	226987617	U0	0	+
chr8	38747236	38747251	U0	0	-"""

    return pd.read_table(StringIO(c), header=None, names="Chromosome Start End Name Score Strand".split())


def test_advanced_intersection_opposite_stranded(cs, bg, expected_result_intersection_opposite_strand):

    result = cs.intersection(bg, strandedness="opposite")

    print(result.df)
    print(expected_result_intersection_opposite_strand)

    assert expected_result_intersection_opposite_strand.equals(result.df)