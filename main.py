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
    task2 = asyncio.create_task(fetch_data(2.1) ) 
    result2 = await task2
    print ("Task 2 fully completed") # Yield control to the event loop (main coroutine suspended till task1 completed)
    result1 = await task1  # Yield control to the event loop (main coroutine suspended till task1 completed)
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
