## Linspace function
- - - 

- Syntax: linspace(start, stop , num = 50, endpoint = True, retstep = False, dtype = None, axis = 0)

### Why use linspace()?

- The linspace() function is a simple and efficient method for generating linearly spaced values, offering a useful solution for a variety of scenarios where specific numerical ranges are needed, such as in data visualization, simulations, and even in the fine-tuning of algorithms. Here are a few examples of where linspace() can be used:

  - Data visualization tasks: For example, when creating a line graph to represent the trajectory of a satellite over time, linspace() can be used to generate the time intervals at which the position data is sampled, ensuring a smooth and continuous line on the graph.
  - Simulations: In financial modeling, to assess the impact of varying interest rates on bond pricing, linspace() can produce a range of interest rates from the lowest possible to the highest anticipated, allowing for a comprehensive analysis across the entire spectrum.
  - Scientific research: While studying the effects of global warming on polar ice caps, researchers might use linspace() to create a series of evenly spaced time intervals over several decades. At each interval, they could simulate the average global temperature increase and its impact on ice melt rates.


- Parameters: 
  - start: Starting value (default 0)
  - stop: Ending value of the range
  - num: Number of values to generate (default 50)
  - endpoint: Includes stop if True (default True)
  - retstep: Returns step size if True (default False)
  - dtype: Output array data type
  - axis: Axis for generation when inputs are array-like (default 0)


- By default the linspace() includes the stop value as the element of the array, if you want we can exclude the last element by just specifying " endpoint = False "

        import numpy as np
        b = np.linspace(0, 1, num=10, endpoint=False)
        print(b)
        
        OUTPUT- 

        [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]


- To get the step size of an array we can just specify " retstep = True"
  
      import numpy as np
      array, c = np.linspace(0, 10, num=5, retstep=True)
      print("Step Size:", c)
        
      OUTPUT-
        
      Step Size: 2.5
- To generate a multi-dimensional array, first generate a 1D array and reshape it to the desired dimension by using ".reshape()"
        
        import numpy as np
        d = np.linspace(0, 1, num=16).reshape(4, 4)
        print(d)

        OUTPUT- 
        
        [[0.         0.06666667 0.13333333 0.2       ]
        [0.26666667 0.33333333 0.4        0.46666667]
        [0.53333333 0.6        0.66666667 0.73333333]
        [0.8        0.86666667 0.93333333 1.        ]]

