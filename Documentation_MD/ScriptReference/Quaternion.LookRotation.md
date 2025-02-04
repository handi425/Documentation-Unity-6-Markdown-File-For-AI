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

#  [Quaternion](Quaternion.html).LookRotation

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

## Declaration

public static [Quaternion](Quaternion.html)
LookRotation([Vector3](Vector3.html) forward, [Vector3](Vector3.html) upwards
= Vector3.up);

### Parameters

forward | The direction to look in.  
---|---  
upwards | The vector that defines in which direction up is.  
  
### Description

Creates a rotation with the specified `forward` and `upwards` directions.

Z axis will be aligned with `forward`, X axis aligned with cross product
between `forward` and `upwards`, and Y axis aligned with cross product between
Z and X.  
  
Returns identity if the magnitude of `forward` is zero.  
If `forward` and `upwards` are colinear, or if the magnitude of `upwards` is
zero, the result is the same as
[Quaternion.FromToRotation](Quaternion.FromToRotation.html) with
`fromDirection` set to the positive Z-axis (0, 0, 1) and `toDirection` set to
the normalized `forward` direction.

    
    
    // You can also use transform.LookAt  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Transform](Transform.html) target;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            [Vector3](Vector3.html) relativePos = target.position - transform.position;  
      
            // the second argument, upwards, defaults to [Vector3.up](Vector3-up.html)
            [Quaternion](Quaternion.html) rotation = [Quaternion.LookRotation](Quaternion.LookRotation.html)(relativePos, [Vector3.up](Vector3-up.html));
            transform.rotation = rotation;
        }
    }
    

Additional resources: [SetLookRotation](Quaternion.SetLookRotation.html).

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

