# Get AWS Cost via python

### Prepare your server
python3 -m venv .venv \
pip3 install tabulate \
pip install boto3 \
python3 get_monthly_cost2.py


## Sample output
```
+---------+------------+------------+-----------------+-----------+
| Account | Start Date |  End Date  |   Cost Amount   | Cost Unit |
+---------+------------+------------+-----------------+-----------+
| account1| 2025-02-01 | 2025-02-28 | 1815.2360318166 |    USD    |
| sccount2| 2025-02-01 | 2025-02-28 | 188.6328402146  |    USD    |
+---------+------------+------------+-----------------+-----------+
```
