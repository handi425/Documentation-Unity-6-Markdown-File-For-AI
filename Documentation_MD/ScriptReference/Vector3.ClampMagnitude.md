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

#  [Vector3](Vector3.html).ClampMagnitude

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

public static [Vector3](Vector3.html) ClampMagnitude([Vector3](Vector3.html)
vector, float maxLength);

### Description

Returns a copy of `vector` with its magnitude clamped to `maxLength`.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Move the object around with the arrow keys but confine it
        // to a given radius around a center point.  
      
        public [Vector3](Vector3.html) centerPt;
        public float radius;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Get the new position for the object.
            [Vector3](Vector3.html) movement = new [Vector3](Vector3.html)([Input.GetAxis](Input.GetAxis.html)("Horizontal"), 0, [Input.GetAxis](Input.GetAxis.html)("Vertical"));
            [Vector3](Vector3.html) newPos = transform.position + movement;  
      
            // Calculate the distance of the new position from the center point. Keep the direction
            // the same but clamp the length to the specified radius.
            [Vector3](Vector3.html) offset = newPos - centerPt;
            transform.position = centerPt + [Vector3.ClampMagnitude](Vector3.ClampMagnitude.html)(offset, radius);
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

