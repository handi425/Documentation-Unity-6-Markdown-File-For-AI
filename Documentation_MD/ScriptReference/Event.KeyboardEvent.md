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

#  [Event](Event.html).KeyboardEvent

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

public static [Event](Event.html) KeyboardEvent(string key);

### Parameters

key | A string representing keyboard keys and modifiers.  
---|---  
  
### Returns

**Event** A new Event with [EventType.KeyDown](EventType.KeyDown.html) and the
requested [KeyCode](KeyCode.html) and optional EventModifier.

### Description

Create a keyboard event.

This is useful when you need to check if a certain key has been pressed -
possibly with modifiers. The syntax for the key string is a key name (same as
in the Input Manager), optionally prefixed by any number of modifiers:  
& = Alternate, ^ = Control, % = Command/Windows key, # = Shift  
Examples: &f12 = Alternate + F12, "^[0]" = Control + keypad0 .  
  
  
See the [Input Manager](../Manual/class-InputManager.html) manual page for
more information on key names.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Detects if the Enter key was pressed
        void OnGUI()
        {
            [GUILayout.Label](GUILayout.Label.html)("Press Enter To Start Game");  
      
            if (Event.current.Equals([Event.KeyboardEvent](Event.KeyboardEvent.html)("[enter]")))
            {
                Application.LoadLevel(1);
            }  
      
            if (Event.current.Equals([Event.KeyboardEvent](Event.KeyboardEvent.html)("return")))
            {
     		[Debug.Log](Debug.Log.html)("I said enter, not return - try the keypad");
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

