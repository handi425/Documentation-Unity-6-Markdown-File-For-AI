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

#  [Transform](Transform.html).position

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

public [Vector3](Vector3.html) position;

### Description

The world space position of the Transform.

The [position](Transform-position.html) property of a
[GameObject](GameObject.html)’s [Transform](Transform.html), which is
accessible in the Unity Editor and through scripts. Alter this value to move a
[GameObject](GameObject.html). Get this value to locate the
[GameObject](GameObject.html) in 3D world space.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        //movement speed in units per second
        private float movementSpeed = 5f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            //get the [Input](Input.html) from Horizontal axis
            float horizontalInput = [Input.GetAxis](Input.GetAxis.html)("Horizontal");
            //get the [Input](Input.html) from Vertical axis
            float verticalInput = [Input.GetAxis](Input.GetAxis.html)("Vertical");  
      
            //update the position
            transform.position = transform.position + new [Vector3](Vector3.html)(horizontalInput * movementSpeed * [Time.deltaTime](Time-deltaTime.html), verticalInput * movementSpeed * [Time.deltaTime](Time-deltaTime.html), 0);  
      
            //output to log the position change
            [Debug.Log](Debug.Log.html)(transform.position);
        }
    }
    

The example gets the Input from Horizontal and Vertical axes, and moves the
GameObject up/down or left/right by changing its position.

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

