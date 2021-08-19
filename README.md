
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jeremy-lipszyc/)


![First Epoch](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/logo.png)
<!-- PROJECT LOGO -->
<br />
<p align="center">
    

  <h3 align="center">Hackaton Bayer</h3>

  <p align="center">
    Project done during the hackaton weekend organize by Bayer.
    <br />
    <a href="https://www.bayerhackathon.com/#"><strong> Event Page </strong></a>
    <br />
    <br />
    <a href="https://vimeo.com/556297205/d7d7c271d7">Video Presentation</a>

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Conclusion</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Hunger For None][product-screenshot]](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/logo2.png)

This hackathon took place during last weekend of May 2021, with more than 400 participation. 
The purpose of this project is to use object detection 
and image processing in order to give the type of disease that the plant have. The farmer will with this information
have the possibility to threat it accurately.

I would like to precise that this project has been done during the second month of my bootcamp
in BeCode and any of these technologies have been seen before.

We use the PlantVillage dataset [1] by Hughes et al. consists of about 87,000 healthy and unhealthy leaf images divided 
into 38 categories by species and disease. Here we provide a subset of our experiments on working with this data. 
We also end up transfer learning from MobileNet and use the weights from pre-training on ImageNet.




### Built With

To achieve this challenge, here are the main framework use in it:

* [tensorflow](https://www.tensorflow.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [cv2](https://opencv.org/)



<!-- GETTING STARTED -->
## Getting Started



### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install NPM packages
   ```sh
   pip install requirement.txt
   ```
   or
   ```sh
   pip3 install requirement.txt
   ```
3. Data Sources
   
    * To add to main directory : https://www.kaggle.com/vipoooool/new-plant-diseases-dataset



<!-- USAGE EXAMPLES -->
## Usage

First, we will need to train the model by running model.py in app directory. 

Modelling steps:
   * Preprocessing Images
     * randomly translate pictures vertically or horizontally
      * rescale
      * randomly applying shearing transformations
      * randomly zooming inside pictures
      * fill_mode : filling in newly created pixels
   * generate batches of image data 
     
   * Training
     * get the base MobileNet model without including the top layers
      * create a small upstream model on top of the MobileNet using the functional API
      * Add Adam Optimizer
      * Training the model
      ![First Epoch](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/epoch1.png)
        ![Last Epoch](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/epoch25.png)
      * Review the process (plot)
        ![review](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/review.png)
      * Save the model    
   * Train Model on our dataset
   * Plotting Loss/Accuracy graph (informative purpose)
   * Saving Model

Flask api :

   * Run app.py
   * Loading Model
   * Add images from the list of test fruit and see result

![review](https://github.com/jeroux/Hackaton-Bayer/blob/main/app/images/SPOILER_Capture_decran_de_2021-05-29_16-50-28.png)




<!-- ROADMAP -->
## Conclusion

This project has been an amazing experience and very stressful one. I had the opportunity to learn
so much in a short period of time.  
This is a disappointment that Covid-19 is still with us at this time and that i was unable to attempt 
other hackathon in Belgium as they all have been canceled.

Even with the fact that this project is not finished, it will stay as it is to keep the spirit of the
hackathon time limit.




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Jérémy Lipszyc - [@Linkedin](https://www.linkedin.com/in/jeremy-lipszyc/) - jeremylipszyc@gmail.com



[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
