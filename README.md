

Django-Gallery-App is an application intended allow users view pictures/photographs along with share what they like with others.

## USER STORIES TARGETED 

The users are targeted to:
1. view the different photos that interest them
2. Click ona  single photo snd expand it to view the details of the photo
    The photo details as well must appear on a modal within the same route of the main page
3. search for different categories of photos
4. copy a link to the photo to share with friends
5. view photos based on the location they were taken. 



## User interface model/design snippet 
[Click here for Design in Figma](https://www.figma.com/file/7QEvjl2wj57PUzkeAqcpyP/Untitled?node-id=0%3A1)

Landing Page
![image description](static/images/Untitled%20(8).png)

Landing page with modal
![image description](static/images/Untitled%20(9).png)









## Behavior Driven Development 



 <table>
    <thead>
      <tr>
        <th>Behaviour</th>
        <th></th>
        <th>Input</th>
         <th></th>
        <th>keepUpperCase is true</th>
      </tr>
    </thead>
    <tbody>
        <tr>
            <td>1. Application starts</td>
            <td></td>
            <td><code>Application  loads </code></td>
            <td><code></code></td>
            <td>see all available images</td>
        </tr>
         <tr>
            <td>2. Click-image</td>
            <td></td>
            <td><code>The Modal shows relatively as designed:
            a)the image displayed 
            b) the image description and title show
            c) the option to share the image is shown
            </code></td>
            <td><code></code></td>
            <td>Any user can access this and needs no authorizations </td>
        </tr>
    </tbody>
  </table>

The following is a live link to the project:

## Installation process

To access my repository link:

[Click here](https://github.com/Charity-Mutembei/Django-Gallery-App)

​

*To clone this repository locally, type the following command on your terminal.*

​git clone 'https://github.com/Charity-Mutembei/Django-Gallery-App'

If using HTTP keys, type:

​below is the git repository link

`https://github.com/Charity-Mutembei/Django-Gallery-App'


​


​

On running the commands successfully, you should have a local version of this repository.

Navigate to the target directory and open it with a prefered IDE :

1. On running the application, type the following on the terminal;
+ `python3.8 manage.py runserver`

run the application:


2. To test the application;

+ `python3.8 manage.py test gallery`

​

3. To navigate to a local browser, Type this on a preferred browser:

+ `127.0.0.1:8000`

## Technologies used

* [Python3.8](https://www.python.org/)

* [Django]

* [Heroku](https://heroku.com)

## Known-Bugs

The application is yet to be launched to Heroku.However, the link to the blog is unresponsive, the navbar cannot display the signin and signout option due to constant crashing of the code. 
The roles of users and writers are defined but yet to to complete the user stories/needs as requested. 

## Contact information

+ Author E-mail ; `charity.mutembei@student.moringaschool.com`

+ Phone Number: +254 718020830.

## Copyright and License

Copyright (c) 2022 Mutembei Charity

​

`MIT LICENSE`

​

Copyright (c) 2022 

​

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

​

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

​

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.




