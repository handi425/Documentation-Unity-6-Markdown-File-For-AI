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

#  [Transform](Transform.html).InverseTransformPoint

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

## Declaration

public [Vector3](Vector3.html) InverseTransformPoint([Vector3](Vector3.html)
position);

### Description

Transforms `position` from world space to local space.

This function is essentially the opposite of
[Transform.TransformPoint](Transform.TransformPoint.html) which is used to
convert from local to world space.  
  
Note that the returned position is affected by scale. Use
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html)
if you are dealing with direction vectors rather than positions.  
  
If you need to transform many points at once consider using
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html)
instead as it is much faster than repeatedly calling this function.

    
    
    // Calculate the transform's position relative to the camera.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) cam;
        public [Vector3](Vector3.html) cameraRelative;  
      
        void Start()
        {
            cam = Camera.main.transform;
            [Vector3](Vector3.html) cameraRelative = cam.InverseTransformPoint(transform.position);  
      
            if (cameraRelative.z > 0)
                print("The object is in front of the camera");
            else
                print("The object is behind the camera");
        }
    }
    

Additional
resources:[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html),
[Transform.InverseTransformVector](Transform.InverseTransformVector.html).

* * *

## Declaration

public [Vector3](Vector3.html) InverseTransformPoint(float x, float y, float
z);

### Description

Transforms the position `x`, `y`, `z` from world space to local space.

This function is essentially the opposite of
[Transform.TransformPoint](Transform.TransformPoint.html) which is used to
convert from local to world space.  
  
Note that the returned position is affected by scale. Use
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html)
if you are dealing with direction vectors rather than positions.  
  
If you need to transform many points at once consider using
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html)
instead as it is much faster than repeatedly calling this function.

    
    
    // Calculate the world origin relative to this transform.
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Vector3](Vector3.html) relativePoint = transform.InverseTransformPoint(0, 0, 0);  
      
            if (relativePoint.z > 0)
                print("The world origin is in front of this object");
            else
                print("The world origin is behind this object");
        }
    }
    

Additional
resources:[Transform.TransformPoint](Transform.TransformPoint.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html),
[Transform.InverseTransformVector](Transform.InverseTransformVector.html).

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

