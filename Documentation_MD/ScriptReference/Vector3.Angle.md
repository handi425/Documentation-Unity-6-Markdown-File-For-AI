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

#  [Vector3](Vector3.html).Angle

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

public static float Angle([Vector3](Vector3.html) from,
[Vector3](Vector3.html) to);

### Parameters

from | The vector from which the angular difference is measured.  
---|---  
to | The vector to which the angular difference is measured.  
  
### Returns

**float** The angle in degrees between the two vectors.

### Description

Calculates the angle between two vectors.

The angle returned is the angle of rotation from the first vector to the
second, when treating these two vector inputs as directions.  
Note: The angle returned will always be between 0 and 180 degrees, because the
method returns the smallest angle between the vectors. That is, it will never
return a reflex angle.

    
    
    using UnityEngine;  
      
    public class AngleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;  
      
        // prints "close" if the z-axis of this transform looks
        // almost towards the target  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) targetDir = target.position - transform.position;
            float angle = [Vector3.Angle](Vector3.Angle.html)(targetDir, transform.forward);  
      
            if (angle < 5.0f)
                print("Close");
        }
    }
    

Additional resources: [SignedAngle](Vector3.SignedAngle.html) function.

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

