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

#  [Vector3](Vector3.html).SignedAngle

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

public static float SignedAngle([Vector3](Vector3.html) from,
[Vector3](Vector3.html) to, [Vector3](Vector3.html) axis);

### Parameters

from | The vector from which the angular difference is measured.  
---|---  
to | The vector to which the angular difference is measured.  
axis | A vector around which the other vectors are rotated.  
  
### Returns

**float** Returns the signed angle between `from` and `to` in degrees.

### Description

Calculates the signed angle between vectors `from` and `to` in relation to
`axis`.

The angle returned is the angle of rotation from the first vector to the
second, when treating these first two vector inputs as directions. These two
vectors also define the plane of rotation, meaning they are parallel to the
plane. This means the axis of rotation around which the angle is calculated is
the [cross product](Vector3.Cross.html) of the first and second vectors (and
not the 3rd "axis" parameter). You can use the ["left hand
rule"](Vector3.Cross.html) to determine the axis of rotation, given the two
input vectors. The third input (named the “axis” parameter), gives you a way
to provide a contextual direction to include in the calculation. This has the
result of flipping the sign of the result depending on whether this third
vector that you supply falls above or below the plane of rotation defined by
the first two input vectors. Therefore the sign of the final result depends on
two things: the order in which you supply the "from" and "to" vector, and the
direction of the third "axis" vector.  
Note: The angle returned will always be between -180 and 180 degrees, because
the method returns the smallest angle between the vectors. That is, it will
never return a reflex angle.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) targetDir = target.position - transform.position;
            [Vector3](Vector3.html) forward = transform.forward;
            float angle = [Vector3.SignedAngle](Vector3.SignedAngle.html)(targetDir, forward, [Vector3.up](Vector3-up.html));
            if (angle < -5.0F)
                print("turn right");
            else if (angle > 5.0F)
                print("turn left");
            else
                print("forward");
        }
    }
    

Additional resources: [Angle](Vector3.Angle.html) function.

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

