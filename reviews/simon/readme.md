My data set consist of data received from a web site that has users in three geographic locations. The data however represents data from other regions (e.g. MUB really is Asia ) so an initial cleaning needs to be done.

The data set also shows how many users have signed legal agreements and also the last time the they logged in and off for either web, application or mobile device.

the real question is to better understanding the user base and what conclusions can be drawn from the data set - or what other data would be required to get a better understanding of the user base.

The first part is to clean the data and try and find correlations or clusters of users that have certain characteristics based on this data set. this includes removing NAN data and converting data.

As much of the data is in the following form

	Created Date            object
	Last Modified Date      object
	FX Read-Only              bool
	E-Agreement Date        object
	E-Agreement Flag        object
	ALGO Execution          object
	FXO Read-Only           object
	 Last Logon             object
	 Last Logoff            object
	Sales Region            object
	 Web On-line            object
	 Web Last Logon         object
	 Web Last Logoff       float64
	 Direct On-line         object
	Direct Last Logon       object
	 Direct Last Logoff    float64
	Mobile On-line         float64
	 Mobile Last Logon      object
	Mobile Last Logoff     float64
	Mobile Read-Only        object
	dtype: object


Indentify and try and use each of the topics that we have learn't whilst either identify the issues with the data set or missing compontenets that would make the solution more a more practical use of compents learned in the course.
…