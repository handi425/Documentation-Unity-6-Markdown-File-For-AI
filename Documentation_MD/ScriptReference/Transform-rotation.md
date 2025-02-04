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

#  [Transform](Transform.html).rotation

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

public [Quaternion](Quaternion.html) rotation;

### Description

A [Quaternion](Quaternion.html) that stores the rotation of the Transform in
world space.

[Transform.rotation](Transform-rotation.html) stores a
[Quaternion](Quaternion.html). You can use [rotation](Transform-rotation.html)
to rotate a GameObject or provide the current rotation. Do not attempt to
edit/modify [rotation](Transform-rotation.html).
[Transform.rotation](Transform-rotation.html) is less than 180 degrees.  
  
[Transform.rotation](Transform-rotation.html) has no gimbal lock.  
  
To rotate a [Transform](Transform.html), use
[Transform.Rotate](Transform.Rotate.html), which uses Euler Angles.  
  
If you want to match values you see in the Inspector, use the
[Quaternion.eulerAngles](Quaternion-eulerAngles.html) property on the returned
[Quaternion](Quaternion.html).

    
    
    using UnityEngine;  
      
    // [Transform.rotation](Transform-rotation.html) example.  
      
    // [Rotate](UIElements.Rotate.html) a [GameObject](GameObject.html) using a [Quaternion](Quaternion.html).
    // Tilt the cube using the arrow keys. When the arrow keys are released
    // the cube will be rotated back to the center using Slerp.  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        float smooth = 5.0f;
        float tiltAngle = 60.0f;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Smoothly tilts a transform towards a target rotation.
            float tiltAroundZ = [Input.GetAxis](Input.GetAxis.html)("Horizontal") * tiltAngle;
            float tiltAroundX = [Input.GetAxis](Input.GetAxis.html)("Vertical") * tiltAngle;  
      
            // [Rotate](UIElements.Rotate.html) the cube by converting the angles into a quaternion.
            [Quaternion](Quaternion.html) target = [Quaternion.Euler](Quaternion.Euler.html)(tiltAroundX, 0, tiltAroundZ);  
      
            // Dampen towards the target rotation
            transform.rotation = [Quaternion.Slerp](Quaternion.Slerp.html)(transform.rotation, target,  [Time.deltaTime](Time-deltaTime.html) * smooth);
        }
    }
    

In the above example, the [rotation](Transform-rotation.html) is described by
a quaternion. For more advice, see [Rotation and Orientation in
Unity](../Manual/QuaternionAndEulerRotationsInUnity.html).

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

