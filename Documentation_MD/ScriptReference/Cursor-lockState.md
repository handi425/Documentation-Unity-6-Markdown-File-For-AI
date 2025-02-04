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

#  [Cursor](Cursor.html).lockState

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

public static [CursorLockMode](CursorLockMode.html) lockState;

### Description

Determines whether the hardware pointer is locked to the center of the view,
constrained to the window, or not constrained at all.

A locked cursor is positioned in the center of the view and cannot be moved.
The cursor is invisible in this state, regardless of the value of
[Cursor.visible](Cursor-visible.html). **Note** : Locking the cursor prevents
the user from interacting with UI elements.  
  
A confined cursor behaves normally, but it is confined to the view. For
example, if the application is running in a window, the a confined cursor
cannot leave that window. The confined cursor mode is only supported on
Windows and Linux standalone builds.  
  
The recommended best practice for a positive user experiences is to only to
lock or confine the cursor because of a user's action, such as pressing a
button.  
  
The cursor state can be changed by the operating system or the Editor. For
example, check the state of the cursor when the application regains focus or
the state of a game changes to reveal a UI.  
  
In the Editor, the cursor loses focus in Game mode when you press Escape or
when you switch an application. In the Standalone Player, you have full
control over the mouse cursor, but if you switch applications, the cursor goes
out of focus.

    
    
    using UnityEngine;  
      
    public class CursorLockExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            //Press the space bar to apply no locking to the [Cursor](Cursor.html)
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.Space](KeyCode.Space.html)))
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.None](CursorLockMode.None.html);
        }  
      
        void OnGUI()
        {
            //Press this button to lock the [Cursor](Cursor.html)
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 50), "Lock [Cursor](Cursor.html)"))
            {
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.Locked](CursorLockMode.Locked.html);
            }  
      
            //Press this button to confine the [Cursor](Cursor.html) within the screen
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(125, 0, 100, 50), "Confine [Cursor](Cursor.html)"))
            {
                [Cursor.lockState](Cursor-lockState.html) = [CursorLockMode.Confined](CursorLockMode.Confined.html);
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

