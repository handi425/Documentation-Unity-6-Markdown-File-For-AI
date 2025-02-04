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

#  [Input](Input.html).GetButtonDown

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

public static bool GetButtonDown(string buttonName);

### Description

Returns true during the frame the user pressed down the virtual button
identified by `buttonName`.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
Call this function from the [Update](MonoBehaviour.Update.html) function,
since the state gets reset each frame. It will not return true until the user
has released the key and pressed it again.  
  
Use this only when implementing action like events IE: shooting a weapon.  
Use [Input.GetAxis](Input.GetAxis.html) for any kind of movement behaviour.  
  
To edit, set up, or remove buttons and their names (such as "Fire1"): 1\. Go
to **Edit** > **Project Settings** > **Input Manager** to bring up the Input
Manager. 2\. Expand **Axis** by clicking the arrow next to it. This shows the
list of the current buttons you have. You can use one of these as the
parameter "buttonName". 3\. Expand one of the items in the list to access and
change aspects such as the button's name and the key, joystick or mouse
movement that triggers it. 4\. For more information about buttons, see the
[Input Manager](../Manual/class-InputManager.html) page.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) projectile;
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButtonDown](Input.GetButtonDown.html)("Fire1"))
                Instantiate(projectile, transform.position, transform.rotation);
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

