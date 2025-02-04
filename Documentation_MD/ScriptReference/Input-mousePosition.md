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

#  [Input](Input.html).mousePosition

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

public static [Vector3](Vector3.html) mousePosition;

### Description

The current mouse position in pixel coordinates. (Read Only).

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
[Input.mousePosition](Input-mousePosition.html) is a [Vector3](Vector3.html)
for compatibility with functions that have [Vector3](Vector3.html) arguments.
The z component of the [Vector3](Vector3.html) is always 0.  
  
The bottom-left of the screen or window is at (0, 0). The top-right of the
screen or window is at ([Screen.width](Screen-width.html),
[Screen.height](Screen-height.html)).  
  
Note: [Input.mousePosition](Input-mousePosition.html) reports the position of
the mouse even when it is not inside the Game View, such as when
[Cursor.lockState](Cursor-lockState.html) is set to
[CursorLockMode.None](CursorLockMode.None.html). When running in windowed mode
with an unconfined cursor, position values smaller than 0 or greater than the
screen dimensions ([Screen.width](Screen-width.html),[Screen.height](Screen-
height.html)) indicate that the mouse cursor is outside of the game window.  
  
In the following example, the x and y coordinates of the mouse position are
printed when the “Fire1” button is clicked.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("Fire1"))
            {
                [Vector3](Vector3.html) mousePos = [Input.mousePosition](Input-mousePosition.html);
                {
                    [Debug.Log](Debug.Log.html)(mousePos.x);
                    [Debug.Log](Debug.Log.html)(mousePos.y);
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

