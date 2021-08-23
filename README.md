# A-PIE-
Abstraction, Polymorphism, Inheritance and Encapsulation: Object Oriented Programming Principles, and Refactoring of Functions



With this code we will introduce the Principles of Object Oriented Programming (POO), which are the following:

    -Abstraction

    -Encapsulation

    -Polymorphism

    -Inheritance

Of these principles, only "**Inheritance**" will not be addressed for our code, which follows the route of using Asset Market Data for its Quantitative Analysis. By obtaining Graphic Visualizations, visualization of Databases, obtaining Returns and Risk Metrics.

We will start by creating a Function that is in charge of making the Graphical Visualization, making the main code cleaner. When a Quant Developer wants to have code automation algorithms that should NOT necessarily be viewed by a Quan User, he only creates `Functions` and `Classes` that store some of the code necessary for financial calculations, but that the User Quan is not going to use.

![APIE1](https://user-images.githubusercontent.com/86130991/130494203-1a304fb8-d20b-47a7-a017-40314e5cb480.png)

The Code will import `Function` to load the code that is responsible for making the` Plots`. In the functions, the `path` to the repertoire where the Databases will be stored will also be stored.

![APIE2](https://user-images.githubusercontent.com/86130991/130494735-b88ccf0a-eb68-4aa3-82ef-221982eb11de.png)

The `stream_functions` Script is the code that should be named to import the instructions necessary for displaying and accessing Databases. Like the rest of the functions, we can add the default Parameters or establish new ones when we call it.

Finally, we can see that `Variable Explorer` continues to work without any problem. All data displays continue to work with POO. And inside the `funtion load_time_series` are the instructions that previously could be displayed in the main Script. But now they are better ordered in a Script than functions only for the declaration of functions.

