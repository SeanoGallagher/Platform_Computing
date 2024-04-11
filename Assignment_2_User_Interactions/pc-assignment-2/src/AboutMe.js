import React from "react"
import PixelParry from './IMG/PixelParry.PNG'
import CoreClassicArcade from './IMG/CoreClassicArcade.PNG'

function AboutMe() {
    return (
        <div className="About Me">
      <div id="title">
        <h1 id="title">About Me</h1>
      </div>

      <div id="body">
        <p>My name is Sean Gallagher. I am a CSE - Game Development major at California State University of San Bernardino.
          I will be graduating Spring of 2024 and I am excited to enter the workforce. I started my college path after three years of working after high school.
          I applied to Chaffey College in Rancho Cucamonga during the pandemic of 2020. Starting college during the pandemic was a big adjustment,
          but online courses gave me the opportunity to make my own schedule and continue working.
          I transferred to CSUSB in the fall of 2022 and decided to stop working and fully commit to my studies.
          However, during the fall semester I was offered an internship working on Automotive Testing at a company called TonDone that lasted about 6 months.
          Since then I have prioritized my studies and working on projects.
        </p>

        <img class="image" src={PixelParry} width="300" height="200" alt="Picture of Pixel Parry Game"></img>

        <p>I am very passionate about making games and have made a few projects while in school and on my own. My favorite project I have made is a game called Pixel Parry (pictured above).
          It is a 2D sword fighting game against a machine learning agent. The agent was trained against itself for over 12 hours so it should be very good at the game, however it is not.
          For some reason the AI is very bad, so the project is flawed at its core. If you would like to play the game you can follow the link
          <a href="https://drive.google.com/drive/folders/1qABzjI2wCzLHD2qUVXHj44OgWrQx71Ri?usp=sharing"> here </a>
          to download.
          Unfortunately, it is only for windows devices. The overall project is an arcade machine (pictured below)
          I made with a group for a school project. It features remakes of old games as well as my original game.
        </p>

        <img src={CoreClassicArcade} width="300" height="200" alt="Picture of Core Classic Arcade"></img>

        <p>My passion for games does not stop at making games, I am also very passionate when it comes to playing them.
          I play a lot of competitive games including: Valorant, League of Legends, Counter Strike, and Call of Duty.
          However, my competitive background mostly comes from playing Call of Duty with my friends and it is definitely the game I am the best at.
          I am currently on the COD team for our school and will be competing in leagues and tournaments throughout the semester.
        </p>
      </div>

      <div>
        <button onClick={clickMe}>Do not click me</button>
      </div>

      <div id="footer">
        <a href="https://github.com/SeanoGallagher">Github</a>
      </div>
    </div>
    );
}

function clickMe() {
    alert('hello there')
}

export default AboutMe;