package jan24.com.revature.app;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class App {

	/*
	Create a function that will test if a string is a valid PIN or not via a regular expression.
	
	A valid PIN has:
	
	Exactly 4 or 6 characters.
	Only numeric characters (0-9).
	No whitespace.
	Examples
	validate("121317") ➞ true
	
	validate("1234") ➞ true
	
	validate("45135") ➞ false
	
	validate("89abc1") ➞ false
	
	validate("900876") ➞ true
	
	validate(" 4983") ➞ false
	
	Notes:
	Empty strings should return 'false' when tested.
	 */
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = 0; //TODO: remove this
		while (true) {
			//get input
			System.out.print("Enter pin: ");
			String pin = s.nextLine();
			
			//validate input and output validation message
			System.out.println("The pin is " + (validate(pin) ? "valid" : "invalid"));
			
			//ask user if they would like to continue
			String contInput = "";
			while (!inStringArray(contInput, new String[] {"Y", "N", "YES", "NO"})) {
				System.out.print("Would you like to enter another pin (Y or N)? ");
				contInput = s.nextLine();
			}
			
			//if the user entered 'n' or 'no', break the loop
			//otherwise, do nothing (the loop will continue)
			if (contInput.equalsIgnoreCase("n") || contInput.equalsIgnoreCase("no")) break;
		}
		
		System.out.println("\nThank you for using the program,\nGoodbye!");
		s.close(); //close the scanner
	}
	
	public static boolean validate(String pin) {
		Pattern validPinPattern = Pattern.compile("^\\d{4}$", Pattern.CASE_INSENSITIVE); //exactly 4 digits
		Pattern validPinPattern2 = Pattern.compile("^\\d{6}$", Pattern.CASE_INSENSITIVE); //exactly 6 digits
		return validPinPattern.matcher(pin).find() || validPinPattern2.matcher(pin).find();
	}
	
	public static boolean inStringArray(String userInput, String[] validInput) {
		for (String s : validInput) if (userInput.equalsIgnoreCase(s)) return true; //return true if the user input is in the validInput array
		return false; //if the for loop completes, the userInput is not in the validInput array
	}
}
