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

#  [Quaternion](Quaternion.html).operator *

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

[Switch to Manual](../Manual/class-Quaternion.html "Go to Quaternion Component
in the Manual")

public static [Quaternion](Quaternion.html) operator
*([Quaternion](Quaternion.html) lhs, [Quaternion](Quaternion.html) rhs);

### Parameters

lhs | Left-hand side quaternion.  
---|---  
rhs | Right-hand side quaternion.  
  
### Description

Combines rotations `lhs` and `rhs`.

Rotating by the product `lhs` * `rhs` is the same as applying the two
rotations in sequence: `lhs` first and then `rhs`, relative to the reference
frame resulting from `lhs` rotation. Note that this means rotations are not
commutative, so `lhs` * `rhs` does not give the same rotation as `rhs` *
`lhs`.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        float rotateSpeed = 90;  
      
        // Applies a rotation of 90 degrees per second around the local Y axis
        void [Update](PlayerLoop.Update.html)()
        {
            float angle = rotateSpeed * [Time.deltaTime](Time-deltaTime.html);
            transform.rotation *= [Quaternion.AngleAxis](Quaternion.AngleAxis.html)(angle, [Vector3.up](Vector3-up.html));
        }
    }
    

* * *

public static [Vector3](Vector3.html) operator *([Quaternion](Quaternion.html)
rotation, [Vector3](Vector3.html) point);

### Description

Rotates the point `point` with `rotation`.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Start()
        {
            //Creates an array of three points forming a triangle
            [Vector3](Vector3.html)[] points = new [Vector3](Vector3.html)[]
            {
                new [Vector3](Vector3.html)(-1, -1, 0),
                new [Vector3](Vector3.html)(1, -1, 0),
                new [Vector3](Vector3.html)(0, 1, 0)
            };  
      
            //Creates a [Quaternion](Quaternion.html) rotation of 5 degrees around the Z axis
            [Quaternion](Quaternion.html) rotation = [Quaternion.AngleAxis](Quaternion.AngleAxis.html)(5, [Vector3.forward](Vector3-forward.html));  
      
            //Loop through the array of Vector3s and apply the rotation
            for (int n = 0; n < points.Length; n++)
            {
                [Vector3](Vector3.html) rotatedPoint = rotation * points[n];
                //Output the new rotation values
                [Debug.Log](Debug.Log.html)("Point " + n + " rotated: " + rotatedPoint);
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

