#!/usr/bin/perl
print "Content-type: text/html\n\n";

use CGI; 
use Switch; 
my $q = CGI->new;


my $firstConvert = $q->param('first'); 
my $secondConvert = $q->param('second'); 

my $convertFrom = $q->param('convertFrom');
my $convertTo = $q->param('convertTo'); 

my $flagOne;
my $flagTwo;

my $feetToMeters = .3048; 
my $feetToMiles = 0.000189394;
my $feetToKilometers = 0.000304800097536;

my $metersToFeet = 3.28084; 
my $metersToMiles = 0.000621371;
my $metersToKilometers = 0.001;

my $milesToFeet = 5280;
my $milesToMeters = 1609.34;
my $milesToKilometers = 1.60933999997549;

my $kilometersToFeet = 3280.84;
my $kilometersToMeters = 1000; 
my $kilometersToMiles = 0.621371;

my $secondsToMinutes = .016667; 
my $secondsToHours = 0.000277778;
my $secondToDays = .000011574; 

my $minutesToSeconds = 60; 
my $minutesToHours = .0166667; 
my $minutesToDays = 0.000694444; 

my $hoursToSeconds = 3600; 
my $hoursToMinutes = 60; 
my $hoursToDays = .0416667; 

my $dayToSeconds = 86400; 
my $daysToMinutes = 1440; 
my $daysToHours = 24; 






sub checkInput{
	my $flag = 1;

	print "so you want to convert $convertFrom $firstConvert to $convertTo $secondConvert<br>";
	#Grabs the right commands
	if (($convertFrom or $convertTo) < 0){
		print "you cant give me negative numbers that doesnt make sense!<br>"; 
		$flag = 0;
	} 

	if (($convertTo or $convertFrom) == /[[:alpha:]]/) {
		print "you cant put a letter in there!<br>";
		$flag = 0;
	}  

	switch($firstConvert){
		case 'kilometers' {$flagOne = 1}
		case 'meters' 	  {$flagOne = 1}
		case 'feet'		  {$flagOne = 1}
		case 'miles'	  {$flagOne = 1}
		case 'celsius'    {$flagOne = 2}
		case 'fahrenheit' {$flagOne = 2}
		case 'kelvin'     {$flagOne = 2}
		case 'hours'      {$flagOne = 3}
		case 'minutes'    {$flagOne = 3}
		case 'second'     {$flagOne = 3}
		case 'days'       {$flagOne = 3}
		else			  {print "you giving me something I cant use man\n"; 
							}
	}

	switch($secondConvert){
		case 'kilometers' {$flagTwo = 1}
		case 'meters' 	  {$flagTwo = 1}
		case 'feet'		  {$flagTwo = 1}
		case 'miles'	  {$flagTwo = 1}
		case 'celsius'    {$flagTwo = 2}
		case 'fahrenheit' {$flagTwo = 2}
		case 'kelvin'     {$flagTwo = 2}
		case 'hours'      {$flagTwo = 3}
		case 'minutes'    {$flagTwo = 3}
		case 'second'     {$flagTwo = 3}
		case 'days'       {$flagTwo = 3}
		else			  {print "you giving me something I cant use man<br>"}
	}


	if ($flagOne != $flagTwo) {
		print "you cant compute those two\n";
		$flag = 0; 
	}



	return $flag;


}

sub doMetric {
	if ($firstConvert eq 'feet'){
		if ($secondConvert eq 'meters') {

			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $feetToMeters; 
			print "Your answer is $ans\n";

		} elsif ($secondConvert eq 'miles'){

			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $feetToMiles; 
			print "Your answer is $ans\n"; 

		} elsif ($secondConvert eq 'kilometers') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $feetToKilometers; 
			print "Your answer is $ans\n"; 
		}
	}

	elsif ($firstConvert eq 'meters') {
		if ($secondConvert eq 'feet') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $metersToFeet; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'miles'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $metersToMiles; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'kilometers'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $metersToKilometers; 
			print "Your ans is $ans\n"; 
		}
	}
	elsif ($firstConvert eq 'miles') {
		if ($secondConvert eq 'feet') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $milesToFeet; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'meters'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $milesToMeters; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'kilometers'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $milesToKilometers; 
			print "Your ans is $ans\n"; 
		}
	}

	elsif ($firstConvert eq 'kilometers') {
		if ($secondConvert eq 'feet') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $kilometersToFeet; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'meters'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $kilometersToMeters; 
			print "Your ans is $ans\n"; 
		} elsif ($secondConvert eq 'miles'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $kilometersToMiles; 
			print "Your ans is $ans\n"; 
		}
	}
}

sub doTemp {
	if ($firstConvert eq 'fahrenheit') {
		if ($secondConvert eq 'celsius') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = ($convertFrom  - 32) * .5555;
			print "Youre Answer is $ans\n";
		} elsif ($secondConvert eq 'kelvin'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = (($convertFrom  - 32) * .5555) + 273.15;
			print "Youre Answer is $ans\n";
		}
	} 

	elsif ($firstConvert eq 'celsius'){
		if ($secondConvert eq 'fahrenheit') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = ($convertFrom * 1.8) + 32; 
			print "Youre Answer is $ans\n";	

		} elsif ($secondConvert eq 'kelvin'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			$convertFrom + 273.15;
			print "Youre Answer is $ans\n";	

		}
	}

	elsif ($firstConvert eq 'kelvin'){
		if ($secondConvert eq 'celsius') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			$convertFrom - 273.15;
			print "Youre Answer is $ans\n";			
		} elsif ($secondConvert eq 'fahrenheit'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			($convertFrom * 1.8) - 459.67;
			print "Youre Answer is $ans\n";	
		}
	}
}

sub doTime {
	if ($firstConvert eq 'second'){
		if ($secondConvert eq 'minutes') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $secondsToMinutes; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'hours'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $secondsToHours; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'days'){
			print "Converting $firstConvert to $secondConvert\n"; 
			my $ans = $convertFrom * $secondToDays; 
			print "Your answer is $ans\n";
		}
	}


	if ($firstConvert eq 'hours'){
		if ($secondConvert eq 'second') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $hoursToSeconds; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'minutes'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $hoursToMinutes; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'days'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $hoursToDays; 
			print "Your answer is $ans\n";
		}
	}


	if ($firstConvert eq 'minutes'){
		if ($secondConvert eq 'second') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $minutesToSeconds; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'hours'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $minutesToHours; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'days'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $minutesToDays; 
			print "Your answer is $ans\n";
		}
	}

	if ($firstConvert eq 'days'){
		if ($secondConvert eq 'second') {
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $dayToSeconds; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'hours'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $daysToHours; 
			print "Your answer is $ans\n";
		} elsif ($secondConvert eq 'minutes'){
			print "Converting $firstConvert to $secondConvert<br>"; 
			my $ans = $convertFrom * $daysToMinutes; 
			print "Your answer is $ans\n";
		}
	}

}


sub main{
	print "Welcome to Conversion Tool! v1.0<br>"; 
	checkInput();
	if ($firstConvert eq $secondConvert) {
	 	print "Its already converted<br>";
	 } 
	elsif ($flagOne && $flagTwo == 1){
		doMetric(); 
	} elsif ($flagOne && $flagTwo == 2){
		doTemp(); 
	} elsif ($flagOne && $flagTwo == 3){
		doTime();
	}
}






main();


