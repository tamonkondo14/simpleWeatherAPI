# simpleWeatherAPI
Using Tkinter and requests, I made a simple weather application utilizing Open Weather's API!

Originally I utilized the API and printed out the result in the terminal, but I realized that it looked a little too boring.

Using Tkinter, I created a simple GUI and users can input the city they are trying to look up the weather for! In the examples below, I used San Francisco as it was part of my local time zone(PST) since datetime utilizes the machine's local time zone(New York's sunrise would be at 2:52 am as opposed to 5:52 am). After users press the generate button, it will take them to a new window, which features the following:
1. Weather
2. Weather Description
3. Wind Speed
4. Temperature in both C and F
5. Sun Rise and Sun Down

![Preview] (https://github.com/tamonkondo14/simpleWeatherAPI/blob/e66331a1921a65b1af71f8aac62d23b849803bf0/Screen%20Shot%202023-07-16%20at%201.12.20%20PM.png)

![Preview](./simpleWeatherAPI/Screen Shot 2023-07-16 at 1.12.20 PM.png)

![Preview](./simpleWeatherAPI/Screen Shot 2023-07-16 at 1.12.52 PM.png)

As for requests, with Open Weather's API being compatible with JSON, I created a JSON and printed it to the terminal to see what data was being pulled and the units of measurement. Determining which data users would most likely see, I returned the values I wanted from the getWeather() function.
