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

#  [Quaternion](Quaternion.html).FromToRotation

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
FromToRotation([Vector3](Vector3.html) fromDirection, [Vector3](Vector3.html)
toDirection);

### Parameters

fromDirection | A non-unit or unit vector representing a direction axis to rotate.  
---|---  
toDirection | A non-unit or unit vector representing the target direction axis.  
  
### Returns

**Quaternion** A unit quaternion which rotates from `fromDirection` to
`toDirection`.

### Description

Creates a rotation from `fromDirection` to `toDirection`.

Use this method to rotate a transform so that one of its axes, such as the
y-axis, follows the target direction, `toDirection`, in world space.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            // Sets the rotation so that the transform's y-axis goes along the global y-axis and the transform's z-axis goes along the global z-axis
            transform.rotation *= [Quaternion.FromToRotation](Quaternion.FromToRotation.html)(transform.up, [Vector3.up](Vector3-up.html));
            transform.rotation *= [Quaternion.FromToRotation](Quaternion.FromToRotation.html)(transform.forward, [Vector3.forward](Vector3-forward.html));
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

