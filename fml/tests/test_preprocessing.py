from fml.preprocessing import detect_types_dataframe, SimplePreprocessor
import pandas as pd

X_cat = pd.DataFrame({'a': ['b', 'c', 'b'],
                      'second': ['word', 'no' , '']})


def test_detect_types_dataframe():
    res = detect_types_dataframe(X_cat)
    assert len(res) == 2
    assert res.categorical.all()
    assert ~res.continuous.any()


def test_simple_preprocessor():
    sp = SimplePreprocessor()
    sp.fit(X_cat)
    trans = sp.transform(X_cat)