import os
import luigi
import time
import redis

fileName = str(time.time())

class Task1(luigi.Task):
    task_namespace = 'tasks'

    def output(self):
        print("Task1: output")
        return luigi.LocalTarget("intermediate/" + fileName + ".txt")

    def run(self):
        print("Task1: run")
        with self.output().open("w") as target:
            target.write(f"This file was generated by Task1 at {time.asctime()}.")

class Task2(luigi.Task):
    task_namespace = 'tasks'

    def requires(self):
        print("Task2: requires")
        return Task1()

    def output(self):
        print("Task2: output")

    def run(self):
        print("Task2: run")
        with self.input().open("r") as intermediate:
            task1_text = intermediate.read()
            r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=os.environ['REDIS_DB_NO'])
            r.set("redis-key-" + str(time.time()), task1_text)
            result = r.get("batch-test-key")
            print(result)


if __name__ == '__main__':
    luigi.run(['tasks.Task2', '--workers', '1', '--local-scheduler'])