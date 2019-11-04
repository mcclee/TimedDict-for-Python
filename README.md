# TimedDict-for-Python
This is a HashMap which will remove the outdated keys. The default limitation is 100sec. Please note the TimedDict is not thread safe.
It supports:
  1. Like builtedin Dict, use [] to set and query according to the key. But if the key dosen't exsit, TimedDict will return None. You can use "key in TimedDict" to check a key is in or not.
  2. print(TimedDict), the output is the same as Dict but it is in order of time.
  3. get_first_key(), return the earliest key, None if it is empty.
  4. get_last_key(), return the latest key, None if it is empty.
  5. keys(), return a list of all current keys.
  6. values(), return a list of all exsiting values.
  7. clear(), set the TimedDict to empty.
  8. Get(), Put() are the same function as TimedDict[].
