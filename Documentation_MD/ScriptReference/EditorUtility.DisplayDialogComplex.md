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

#  [EditorUtility](EditorUtility.html).DisplayDialogComplex

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

public static int DisplayDialogComplex(string title, string message, string
ok, string cancel, string alt);

### Parameters

title | Title for dialog.  
---|---  
message | Purpose for the dialog.  
ok | Dialog function chosen.  
cancel | Close dialog with no operation.  
alt | Choose alternative dialog purpose.  
  
### Returns

**int** Returns the ID of a button. IDs are 0, 1, or 2 and they correspond to
the `ok`, `cancel` and `alt` buttons respectively. An ID of 1, which
corresponds to `cancel`, returns if the dialog is closed or the user presses
the Escape key.

### Description

Displays a modal dialog with three buttons.

Use it for displaying message boxes in the Editor.  
  
`DisplayDialogComplex` is similar to
[DisplayDialog](EditorUtility.DisplayDialog.html). This `DisplayDialogComplex`
member shows a dialog with three buttons. These buttons represent `ok`,
`cancel` and `alt`. `DisplayDialogComplex` returns an integer 0, 1 or 2
corresponding to the `ok`, `cancel` and `alt` buttons.  
  
The `ok` button is the default option, and can also be activated by pressing
Enter.  
  
The `cancel` button is considered the "cancel" button and should usually not
perform any action. On a PC, this can also be activated by pressing Escape or
by clicking the dialog window close button. On a Mac, this can also be
activated by pressing Escape, provided the button is called "Cancel".  
  
The `alt` button allows you to provide the user with an alternative choice in
addition to the `ok` and `cancel` buttons. This button does not have a fixed
keyboard shortcut.  
  
For compliance with platform UI guidelines, the actual display order of the
buttons is platform-dependent:

  * On Windows, the display order is: `ok`, `alt`, then `cancel`.
  * On macOS, the display order is: `alt`, `cancel`, then `ok`.

Additional resources: [DisplayDialog](EditorUtility.DisplayDialog.html).  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityDisplayDialogComplex-osx.png)  
_macOS display dialog buttons for the example below._  
  
  
![](../StaticFiles/ScriptRefImages/EditorUtilityDisplayDialogComplex-pc.png)  
_PC display dialog buttons for the example below._  
  
The script reference example below creates a complex display dialog. The
chosen button causes a Unity [EditorApplication](EditorApplication.html)
static function to be called.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class DisplayDlgComplexExample : [EditorWindow](EditorWindow.html)
    {
        // Lets you save or not before quitting, or cancel.  
      
        [[MenuItem](MenuItem.html)("Example/Quit")]
        static void Init()
        {
            int option = [EditorUtility.DisplayDialogComplex](EditorUtility.DisplayDialogComplex.html)("Unsaved Changes",
                "Do you want to save the changes you made before quitting?",
                "Save",
                "Cancel",
                "Don't Save");  
      
            switch (option)
            {
                // Save.
                case 0:
                    EditorApplication.SaveScene(EditorApplication.currentScene);
                    [EditorApplication.Exit](EditorApplication.Exit.html)(0);
                    break;  
      
                // Cancel.
                case 1:
                    break;  
      
                // Don't Save.
                case 2:
                    [EditorApplication.Exit](EditorApplication.Exit.html)(0);
                    break;  
      
                default:
                    [Debug.LogError](Debug.LogError.html)("Unrecognized option.");
                    break;
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

