#
#  Import LIBRARIES
import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

#  Import FILES
#  ______________________
#


def fetch_data(param: int) -> str:  # This is now a sync function!
    print(f"Do something with {param}...", flush=True)
    time.sleep(param)  # Suspends current task till 'sleep' is completed
    # await asyncio.sleep(param) # Suspends current task till 'sleep' is completed
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"


async def main() -> list[str]:
    #  Run in Threads
    task1: asyncio.Task[str] = asyncio.create_task(coro=asyncio.to_thread(fetch_data, 1))
    task2: asyncio.Task[str] = asyncio.create_task(coro=asyncio.to_thread(fetch_data, 2))
    result1: str = await task1
    print("Thread 1 fully completed")
    result2: str = await task2
    print("Thread 2 fully completed")

    #  Run in process pool
    loop: asyncio.AbstractEventLoop = asyncio._get_running_loop()

    with ProcessPoolExecutor() as executor:
        task_1: asyncio.Future[str] = loop.run_in_executor(executor, fetch_data, 1)
        task_2: asyncio.Future[str] = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task_1
        print("Process 1 fully completed")
        result2 = await task_2
        print("Process 2 fully completed")

    return [result1, result2]


if __name__ == "__main__":
    t1: float = time.perf_counter()

    print("Start running main")
    results: list[str] = asyncio.run(main=main())
    print(results)

    t2: float = time.perf_counter()
    print(f"Finished in {t2 - t1: .2f} seconds")


# def main():
#     print("Hello from async-cs-y!")


# if __name__ == "__main__":
#     main()
