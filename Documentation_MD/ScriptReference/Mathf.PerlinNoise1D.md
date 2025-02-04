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

#  [Mathf](Mathf.html).PerlinNoise1D

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

[Switch to Manual](../Manual/class-Mathf.html "Go to Mathf Component in the
Manual")

## Declaration

public static float PerlinNoise1D(float x);

### Parameters

x | The X-coordinate of the given sample point.  
---|---  
  
### Returns

**float** A value in the range of 0.0 and 1.0. The value might be slightly
higher or lower than this range.

### Description

Generates a 1D pseudo-random pattern of float values across a 2D plane.

Although the noise plane is two-dimensional, you can use a single one-
dimensional line through the pattern to good effect, for example for animation
effects. The result of PerlinNoise1D(x) is equivalent to PerlinNoise(x, 0),
but the former is faster.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // "Bobbing" animation from 1D Perlin noise.  
      
        // Range over which height varies.
        float heightScale = 1.0f;  
      
        // Distance covered per second along X axis of Perlin plane.
        float xScale = 1.0f;  
      
    
        void [Update](PlayerLoop.Update.html)()
        {
            float height = heightScale * [Mathf.PerlinNoise1D](Mathf.PerlinNoise1D.html)([Time.time](Time-time.html) * xScale);
            [Vector3](Vector3.html) pos = transform.position;
            pos.y = height;
            transform.position = pos;
        }
    }
    

**Note:** It is possible for the return value to be slightly less than 0.0f or
slightly exceed 1.0f. You may need to clamp the return value if the 0.0 to 1.0
range is important to you.

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

