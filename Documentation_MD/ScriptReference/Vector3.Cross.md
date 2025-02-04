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

#  [Vector3](Vector3.html).Cross

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

public static [Vector3](Vector3.html) Cross([Vector3](Vector3.html) lhs,
[Vector3](Vector3.html) rhs);

### Description

Cross Product of two vectors.

The cross product of two vectors results in a third vector which is
perpendicular to the two input vectors. The result's magnitude is equal to the
magnitudes of the two inputs multiplied together and then multiplied by the
sine of the angle between the inputs. You can determine the direction of the
result vector using the "left hand rule".  
  
![](../StaticFiles/ScriptRefImages/LeftHandRuleDiagram.png)  
_The left hand rule applied to Cross(a, b)._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Get the normal to a triangle from the three corner points a, b, and o, where o is the origin point of vectors a and b.
        [Vector3](Vector3.html) GetNormal([Vector3](Vector3.html) a, [Vector3](Vector3.html) b, [Vector3](Vector3.html) o)
        {
            // Find vectors corresponding to two of the sides of the triangle.
            [Vector3](Vector3.html) side1 = a - o;
            [Vector3](Vector3.html) side2 = b - o;  
      
            // Cross the vectors to get a perpendicular vector, then normalize it. This is the [Result](Networking.UnityWebRequest.Result.html) vector in the drawing above.
            return [Vector3.Cross](Vector3.Cross.html)(side1, side2).normalized;
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

