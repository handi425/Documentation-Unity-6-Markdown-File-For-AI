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

#  [Menu](Menu.html).GetChecked

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

public static bool GetChecked(string menuPath);

### Description

Gets the check status of a menu item.

    
    
        using [UnityEditor](UnityEditor.html);
        using UnityEngine;  
      
        public class CheckMenuTest: [MonoBehaviour](MonoBehaviour.html)
        {
            // Add a menu item named "MenuTest" to MyMenu in the main menu.    
            [[MenuItem](MenuItem.html)("MyMenu/MenuTest")]
            static void DoSomething()
            {
                [Debug.Log](Debug.Log.html)("A placeholder menu item.");         
            }
            
            // Add a menu item that you can click to add a check to the "MenuTest" menu item in MyMenu in the main menu. 
            [[MenuItem](MenuItem.html)("MyMenu/Check menu item")]
            static void CheckMenu()
            {
                [Menu.SetChecked](Menu.SetChecked.html)("MyMenu/MenuTest", true);
                [Debug.Log](Debug.Log.html)("Checked 'MenuTest'");            
            }
            
            // Add a menu item that you can click to clear the check from the "MenuTest" menu item in MyMenu in the main menu. 
            [[MenuItem](MenuItem.html)("MyMenu/Clear check from menu")]
            static void ClearCheck()
            {
                [Menu.SetChecked](Menu.SetChecked.html)("MyMenu/MenuTest", false);
                [Debug.Log](Debug.Log.html)("Cleared check from menu");
            }  
      
            // Add a menu item that you can click to determine if the "MenuTest" in the main menu is checked.
            [[MenuItem](MenuItem.html)("MyMenu/Is MenuTest checked?")]
            static void GetChecked()
            {  
            if ([Menu.GetChecked](Menu.GetChecked.html)("MyMenu/MenuTest"))
            {
                [Debug.Log](Debug.Log.html)("MenuTest is checked");
            }
                else
            {
                [Debug.Log](Debug.Log.html)("MenuTest is not checked");
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

