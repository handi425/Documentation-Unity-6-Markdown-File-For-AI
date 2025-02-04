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

#  [Transform](Transform.html).InverseTransformDirection

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

public [Vector3](Vector3.html)
InverseTransformDirection([Vector3](Vector3.html) direction);

### Description

Transforms a `direction` from world space to local space. The opposite of
[Transform.TransformDirection](Transform.TransformDirection.html).

This operation is not affected by scale or position of the transform. The
transformed vector has the same length as the original.  
  
If you need the inverse operation to transform from local space to world space
you can use [Transform.TransformDirection](Transform.TransformDirection.html)  
  
You should use
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html) if the
vector represents a position in space rather than a direction.  
  
If you need to transform many directions at once consider using
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html)
instead as it is much faster than repeatedly calling this function.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // transform the world forward into local space:
            [Vector3](Vector3.html) relative;
            relative = transform.InverseTransformDirection([Vector3.forward](Vector3-forward.html));
            [Debug.Log](Debug.Log.html)(relative);
        }
    }
    

Additional
resources:[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html),
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html),
[Transform.InverseTransformVector](Transform.InverseTransformVector.html).

* * *

## Declaration

public [Vector3](Vector3.html) InverseTransformDirection(float x, float y,
float z);

### Description

Transforms the direction `x`, `y`, `z` from world space to local space. The
opposite of [Transform.TransformDirection](Transform.TransformDirection.html).

This operation is not affected by scale or position of the transform. The
transformed vector has the same length as the original.  
  
If you need the inverse operation to transform from local space to world space
you can use [Transform.TransformDirection](Transform.TransformDirection.html)  
  
You should use
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html) if the
vector represents a position in space rather than a direction.  
  
If you need to transform many directions at once consider using
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html)
instead as it is much faster than repeatedly calling this function.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // transform the world forward into local space:
            [Vector3](Vector3.html) relative;
            relative = transform.InverseTransformDirection([Vector3.forward](Vector3-forward.html));
            [Debug.Log](Debug.Log.html)(relative);
        }
    }
    

Additional
resources:[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html),
[Transform.InverseTransformPoint](Transform.InverseTransformPoint.html),
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

