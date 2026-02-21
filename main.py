# 
#  Import LIBRARIES
import asyncio
import time
#  Import FILES
#  ______________________
# 

async def fetch_data (param):
    print(f"Do something with {param}...") 
    await asyncio.sleep(param) # Suspends current task till 'sleep' is completed 
    print(f"Done with {param}") 
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))  
    print("Task 1 created")
    task2 = asyncio.create_task(fetch_data(2.1)) 
    print("Task 2 created")
    # print("Busy for 2.50 seconds")
    # await asyncio.sleep(2.5)
    # print("Done with the 2.50 seconds")
    result2 = await task2 # Suspends main()and yields control to the event loop that perform coroutine fetch_data
    print ("Task 2 fully completed") 
    result1 = await task1  # Suspends main()and yields control to the event loop (main coroutine suspended till task1 completed)
    print ("Task 1 fully completed")
    return [result1, result2]



t1 = time.perf_counter()  # Start the counter

results = asyncio.run(main())  # Create an EVENT LOOP
print(results)

t2 = time.perf_counter ()  # Stop the counter
print(f"Finished in {t2 - t1:.2f} seconds")
print(".")







# def main():
#     print("Hello from async-cs-y!")


# if __name__ == "__main__":
#     main()
