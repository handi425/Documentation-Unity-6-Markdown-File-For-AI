[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [TouchScreenKeyboard](TouchScreenKeyboard.html).Open

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

## Declaration

public static [TouchScreenKeyboard](TouchScreenKeyboard.html) Open(string
text, [TouchScreenKeyboardType](TouchScreenKeyboardType.html) keyboardType =
TouchScreenKeyboardType.Default, bool autocorrection = true, bool multiline =
false, bool secure = false, bool alert = false, string textPlaceholder = "",
int characterLimit = 0);

### Parameters

text | Text to edit.  
---|---  
keyboardType | Type of keyboard (eg, any text, numbers only, etc).  
autocorrection | Is autocorrection applied?  
multiline | Can more than one line of text be entered?  
secure | Is the text masked (for passwords, etc)?  
alert | Is the keyboard opened in alert mode?  
textPlaceholder | Text to be used if no other text is present.  
characterLimit | How many characters the keyboard input field is limited to. 0 = infinite. (Android and iOS only)  
  
### Description

Opens the native keyboard provided by OS on the screen.

The `autocorrection` determines whether the input tracks unknown words and
suggests a more suitable replacement candidate to the user, replacing the
typed text automatically unless the user explicitly overrides the action. The
`multiline` determines if user can input more than one line of text. The
`secure` identifies whether the keyboard is used for password. Text in the
input field will be hidden from the user except the recently typed character.
The keyboard can be opened in the `alert` mode too. The `placeholder` string
will be displayed when there is no other text in the input field of the
keyboard.  
  
Additional resources: [Alert keyboard](../Manual/MobileKeyboard.html#alert)  
  

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string stringToEdit = "Hello World";
        private [TouchScreenKeyboard](TouchScreenKeyboard.html) keyboard;  
      
        // Opens native keyboard
        void OnGUI()
        {
            stringToEdit = [GUI.TextField](GUI.TextField.html)(new [Rect](Rect.html)(10, 10, 200, 30), stringToEdit, 30);  
      
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 50, 200, 100), "Default"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.Default](TouchScreenKeyboardType.Default.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 150, 200, 100), "ASCIICapable"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.ASCIICapable](TouchScreenKeyboardType.ASCIICapable.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 250, 200, 100), "Numbers and Punctuation"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.NumbersAndPunctuation](TouchScreenKeyboardType.NumbersAndPunctuation.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 350, 200, 100), "URL"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.URL](TouchScreenKeyboardType.URL.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 450, 200, 100), "NumberPad"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.NumberPad](TouchScreenKeyboardType.NumberPad.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 550, 200, 100), "PhonePad"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.PhonePad](TouchScreenKeyboardType.PhonePad.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 650, 200, 100), "NamePhonePad"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.NamePhonePad](TouchScreenKeyboardType.NamePhonePad.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 750, 200, 100), "EmailAddress"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.EmailAddress](TouchScreenKeyboardType.EmailAddress.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 850, 200, 100), "Social"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.Social](TouchScreenKeyboardType.Social.html));
            }
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 950, 200, 100), "Search"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.Search](TouchScreenKeyboardType.Search.html));
            }
            // Only supported on [iOS](PlayerSettings.iOS.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 1050, 200, 100), "One [Time](Time.html) Code"))
            {
                keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)("", [TouchScreenKeyboardType.OneTimeCode](TouchScreenKeyboardType.OneTimeCode.html));
            }
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

