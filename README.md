<h1>Requirements</h1>
<ul>
<li>Run STM32 Application in windows automatically</li>
<li>Collect Average data generated from STM32 application for different modes</li>
</ul>
<h1>Architecture</h1>
<img src="https://drive.google.com/uc?export=view&id=1GP8sPyUHjt-v0cNfwVyZP6_40oGMuqHQ">
<ul>
<li>In UI user/customer will give input configuration</li>
<li>RPi will collect these input values[ different modes] and change RE01 modes</li>
<li>RPi will also collect camera stream and send to UI</li>
<li>RPi will start UiPath which will automate STM32 application to collect average current</li> 
</ul>
<h1>Design</h1>
<h2>Components in Laptop</h2>
<ul>
<li>STM32 Application to measure average current</li>
<li>UiPath Program for STM32 application Automation</li>
<li>Mini Fabric[Python program] to communicate with RPi</li>
</ul>
<h2>UiPath Design</h2>
<img src="https://drive.google.com/uc?export=view&id=1mIztpzCtHUC1RMV4axuppdAIxI4iUiqw">
<ul>
<li>S1 : It is a initial state here UiPath appliaction is called by Mini Fabric</li>
<li>S2 : At this State UiPath Will open STM32 Application and assign defult values for aquisition</li>
<li>S3 : This state will look for commands in commands.csv file which will be written by Mini Fabric</li>
<li>S4 : If command.csv have START command then UiPath will start aquisition in STM32 application and collect the average current and store it int output_avg.csv.when collecting 
average current UiPath will check command.csv if command.csv file have any command other than START reading average values will be stopped 
and stop aquisition is pressed in STM32 Application</li>
<li>S5 : If command.csv file have END command then UiPath will stay in idle state.This state is used so that UiPath can start reading average current after mode in board is 
changed</li>
<li>S6 : If command.csv file have EXIT command then UiPath will close STM32 Application and UiPath will get terminated</li>
</ul>
