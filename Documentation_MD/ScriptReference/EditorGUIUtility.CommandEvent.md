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

#  [EditorGUIUtility](EditorGUIUtility.html).CommandEvent

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

public static [Event](Event.html) CommandEvent(string commandName);

### Parameters

commandName | The command to be sent.  
---|---  
  
### Description

Creates an event that can be sent to another window.

    
    
    // Sends a paste event to an [EditorWindow](EditorWindow.html), as if Paste
    // was selected from the Edit menu.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CommandEventExample : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/CommandEvent example")]
        static void commandEventExample()
        {
            CommandEventExample window = [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<CommandEventExample>(new [Rect](Rect.html)(0, 0, 150, 40));
            window.Show();
        }  
      
        void OnGUI()
        {
            if ([GUILayout.Button](GUILayout.Button.html)("Paste"))
            {
                [Event](Event.html) e = [EditorGUIUtility.CommandEvent](EditorGUIUtility.CommandEvent.html)("Paste");
                [EditorWindow](EditorWindow.html) ew = [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<CommandEventTest>(true);
                ew.SendEvent(e);
            }
        }
    }
    

The script below receives the Paste message sent from CommandEventExample
above.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CommandEventTest : [EditorWindow](EditorWindow.html)
    {
        private int eventCount = 0;  
      
        [[MenuItem](MenuItem.html)("Examples/Example that receives a paste event")]
        static void test()
        {
            CommandEventTest window = [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<CommandEventTest>(new [Rect](Rect.html)(0, 0, 100, 40));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(10, 10, 90, 30), "Paste: " + eventCount.ToString());  
      
            if (Event.current.type == [EventType.ExecuteCommand](EventType.ExecuteCommand.html))
            {
                [Event](Event.html) e = [Event.current](Event-current.html);
                if (e.commandName == "Paste")
                {
                    eventCount = eventCount + 1;
                }
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

