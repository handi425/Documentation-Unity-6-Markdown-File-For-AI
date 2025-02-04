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

#  [Input](Input.html).GetButton

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

public static bool GetButton(string buttonName);

### Parameters

buttonName | The name of the button such as Jump.  
---|---  
  
### Returns

**bool** True when an axis has been pressed and not released.

### Description

Returns true while the virtual button identified by `buttonName` is held down.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
Think auto fire - this will return true as long as the button is held down.
Use this only when implementing events that trigger an action, eg, shooting a
weapon. The `buttonName` argument will normally be one of the names in
[InputManager](../Manual/class-InputManager.html) such as Jump or Fire1.
[GetButton](Input.GetButton.html) will return to `false` when it is released.  
  
**Note:** Use [GetAxis](Input.GetAxis.html) for input that controls continuous
movement.

    
    
    // Instantiates a projectile every 0.5 seconds,
    // if the Fire1 button (default is Ctrl) is pressed.  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) projectile;
        public float fireDelta = 0.5F;  
      
        private float nextFire = 0.5F;
        private [GameObject](GameObject.html) newProjectile;
        private float myTime = 0.0F;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            myTime = myTime + [Time.deltaTime](Time-deltaTime.html);  
      
            if ([Input.GetButton](Input.GetButton.html)("Fire1") && myTime > nextFire)
            {
                nextFire = myTime + fireDelta;
                newProjectile = Instantiate(projectile, transform.position, transform.rotation) as [GameObject](GameObject.html);  
      
                // create code here that animates the newProjectile  
      
                nextFire = nextFire - myTime;
                myTime = 0.0F;
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

