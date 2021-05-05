# SETUP
* create a virtual env using **python -m venv .venv**;
* active the virtualenv: **source .venv/bin/activate**;
* if you have *make* instaled, you can run **make install** or you can run **pip install -e .**.

# TESTS
* after run setup step, run **make test** or **pytest**.

# TO RUN
* python uk_postcode/cli.py or flask run

# USAGE
## cli
* python uk_postcode/cli.py -c ASCN1ZZ

## api
* flask run
* http://127.0.0.1:5000/postcode/a999aa