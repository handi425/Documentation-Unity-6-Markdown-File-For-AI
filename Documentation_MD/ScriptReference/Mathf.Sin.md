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

#  [Mathf](Mathf.html).Sin

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

public static float Sin(float f);

### Parameters

f | The input angle, in radians.  
---|---  
  
### Returns

**float** The return value between -1 and +1.

### Description

Returns the sine of angle `f`.

**Note:** If using very large numbers with this function, there is an
acceptable range for input angle values for this method, beyond which the
calculation will fail. On windows, the acceptable range is approximately
between -9223372036854775295 to 9223372036854775295. This range may differ on
other platforms. For values outside of the acceptable range, the Sin method
returns the input value, rather than throwing an exception.  
  
Additional resources: [Cos](Mathf.Cos.html), [Tan](Mathf.Tan.html)

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class PolyDrawExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public int numberOfSides;
        public float polygonRadius;
        public [Vector2](Vector2.html) polygonCenter;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            DebugDrawPolygon(polygonCenter, polygonRadius, numberOfSides);
        }  
      
        // Draw a polygon in the XY plane with a specfied position, number of sides
        // and radius.
        void DebugDrawPolygon([Vector2](Vector2.html) center, float radius, int numSides)
        {
            // The corner that is used to start the polygon (parallel to the X axis).
            [Vector2](Vector2.html) startCorner = new [Vector2](Vector2.html)(radius, 0) + center;  
      
            // The "previous" corner point, initialised to the starting corner.
            [Vector2](Vector2.html) previousCorner = startCorner;  
      
            // For each corner after the starting corner...
            for (int i = 1; i < numSides; i++)
            {
                // Calculate the angle of the corner in radians.
                float cornerAngle = 2f * [Mathf.PI](Mathf.PI.html) / (float)numSides * i;  
      
                // Get the X and Y coordinates of the corner point.
                [Vector2](Vector2.html) currentCorner = new [Vector2](Vector2.html)([Mathf.Cos](Mathf.Cos.html)(cornerAngle) * radius, [Mathf.Sin](Mathf.Sin.html)(cornerAngle) * radius) + center;  
      
                // Draw a side of the polygon by connecting the current corner to the previous one.
                [Debug.DrawLine](Debug.DrawLine.html)(currentCorner, previousCorner);  
      
                // Having used the current corner, it now becomes the previous corner.
                previousCorner = currentCorner;
            }  
      
            // Draw the final side by connecting the last corner to the starting corner.
            [Debug.DrawLine](Debug.DrawLine.html)(startCorner, previousCorner);
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

